from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
#from flaskext.mysql import MySQL
#from sqlalchemy import create_engine

db = SQLAlchemy()
DB_NAME = "pisecure_teamg"

def create_app():
    app = Flask(__name__)
    # python -c 'import secrets; print(secrets.token_hex(12))'
    # generate secret key using OS in bash terminal
    #prevents cookie tampering
    app.config['SECRET_KEY'] = '256b009ddecd51959c4bc2d9' #secret key encripts session data for user
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pisecureteamg@localhost/users'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #db = SQLAlchemy(app)
    db.init_app(app)

#Import other files for app creation
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

"""
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')
"""

