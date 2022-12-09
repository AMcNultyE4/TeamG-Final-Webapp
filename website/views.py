from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("home.html", user = current_user)

''''
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@views.route('/about')
def about():
    return render_template("about.html", user=current_user)

@views.route('/settings')
@login_required
def settings():
    return render_template("settings.html", user=current_user)
'''
## Newer HTML files

@views.route('/newhome')
def newhome():
    return render_template("newhome.html", user=current_user)

@views.route('/newabout')
def newabout():
    return render_template("newabout.html", user=current_user)

@views.route('/newprofile')
@login_required
def newprofile():
    return render_template("newprofile.html", user=current_user)
