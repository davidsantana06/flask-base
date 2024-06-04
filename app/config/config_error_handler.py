from flask import Flask
from werkzeug.exceptions import HTTPException

from app.lib.core.jinja import render_page


_ERROR_MESSAGE = {
    400: 'Invalid request.',
    401: 'Unauthorized access.',
    403: 'Forbidden acess.',
    404: 'Page not found.',
    405: 'HTTP method not allowed.',
    500: 'Internal server error.'
}
_GENERIC_MESSAGE = 'An unexpected error has occurred.'


def _error_handler(e: Exception):
    code = e.code if (isinstance(e, HTTPException)) else 500
    description = _ERROR_MESSAGE.get(code, _GENERIC_MESSAGE)
    return render_page('error', {'code': code, 'description': description}, code)


def configure_error_handler(app: Flask) -> None:
    app.register_error_handler(Exception, _error_handler)
