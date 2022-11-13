from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        #User logs in with email and password when selecting 'Login'
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('You are logged in!', category = 'success')
                login_user(user, remember=True)
                #Remember user and redirect to home page on successful login
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect email or password, please try again.', category = 'error')
        else:
            flash('Incorrect email or password, please try again.', category = 'error')
    return render_template('login.html', user = current_user)

#Logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    #Logout redirects to login page
    return redirect(url_for('auth.login'))

#Sign up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        #Confirms password so, two input requests for password are neeeded
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        #Criteria for email and passwords
        if user:
            flash ('Email already in use, please use another or try logging in', category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name)< 2:
            flash('Name must be longer than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match, please try again.', category='error')
        elif password1 < 7:
            flash('Password must be longer than 7 characters.', category='error')
        else:
            #Hashes password before commiting to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account successfully created!', category='success')
            #Redirect to home page or secure profile for Pi board
            return redirect(url_for('home.html'))
    return render_template('sign_up.html', user=current_user)