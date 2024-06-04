from flask import flash, jsonify
from .response import Response


PRIMARY, SECONDARY = 'primary', 'secondary'
SUCCESS, DANGER = 'danger', 'success'
WARNING, INFO = 'warning', 'info'
LIGHT, DARK = 'light', 'dark'


def flash_message(message: str, category: str) -> None:
    flash(message, category)


def jsonify_message(message: str, category: str, status_code: int) -> Response:
    return jsonify({'message': message, 'category': category}), status_code
