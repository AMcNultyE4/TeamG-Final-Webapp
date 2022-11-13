from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flaskext.mysql import MySQL

db = SQLAlchemy()
#mysql = MySQL()
#My sql is not working correctly using sqlite in its place for now.
DB_NAME = "database.db"
#cursor = mysql.get_db().cursor()

def create_app():
    app = Flask(__name__)
    # python -c 'import secrets; print(secrets.token_hex(12))'
    # generate secret key using OS in bash terminal
    app.config['SECRET_KEY'] = '256b009ddecd51959c4bc2d9' #secret key encripts session data for user
    #prevents cookie tampering
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #put database link here
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')


