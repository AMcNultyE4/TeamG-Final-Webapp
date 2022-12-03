from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # Home page
        #Probbaly have this redirect to a file that hosts the Pi stream and data
        return render_template("home.html", user = current_user)

