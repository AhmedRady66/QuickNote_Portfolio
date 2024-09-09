from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """create app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jhfrhbfkjsbdnk khdjssbndm' # secret key for the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(path.abspath(path.dirname(__file__)), DB_NAME)}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """load user using id"""
        return User.query.get(int(id))

    return app


def create_database(app):
    """create database"""
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')


