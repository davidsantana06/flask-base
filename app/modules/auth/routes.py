from flask import request
from flask_login import logout_user, current_user

from app.lib.core.redirect import redirect

from . import auth


@auth.before_request
def before_request():
    is_checkable_endpoint = not any(endpoint in request.endpoint for endpoint in ['static', 'auth.logout'])
    is_user_authenticated = bool(current_user.is_authenticated)

    if is_checkable_endpoint and is_user_authenticated:
        return redirect('home.index')


@auth.get('/login')
def login():
    return redirect('home.index')


@auth.get('/logout')
def logout():
    logout_user()
    return redirect('.login')
