from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    #create unique user ID in DB and set to primary key
    id = db.Column(db.Integer(), primary_key = True)
    #email is required to be unique. Set to max 100 char
    email = db.Column(db.String(100), nullable = False, unique=True)
    password = db.Column(db.String(150), nullable = False) #password set to max 150 char
    first_name = db.Column(db.String(150), nullable = False)# max 150 char
    

