from flask import Flask

from app.extensions import database, bcrypt, csrf, login_manager
from app.database import *


def _configure_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def _configure_bcrypt(app: Flask) -> None:
    bcrypt.init_app(app)


def _configure_csrf(app: Flask) -> None:
    csrf.init_app(app)


def _configure_login_manager(app: Flask) -> None:
    login_manager.init_app(app)
    login_manager.user_loader(
        lambda user_id: User.find_first_by_id(int(user_id))
    )
    # login_manager.login_message = ''
    # login_manager.login_message_category = ''
    # login_manager.login_view = 'auth.login'


def configure_extensions(app: Flask) -> None:
    _configure_database(app)
    _configure_bcrypt(app)
    _configure_csrf(app)
    _configure_login_manager(app)
