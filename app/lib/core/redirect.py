from flask import (
    jsonify,
    redirect as redirect_,
    url_for
)
from http import HTTPStatus

from .response import Response


def _retrieve_location(endpoint_or_url: str) -> str:
    return endpoint_or_url if (endpoint_or_url.startswith('/')) else url_for(endpoint_or_url)


def redirect(endpoint_or_url: str, status_code: int = HTTPStatus.FOUND) -> Response:
    location = _retrieve_location(endpoint_or_url)
    redirect_(location, status_code)


def jsonify_redirect(endpoint_or_url: str, status_code: int = HTTPStatus.FOUND) -> Response:
    location = _retrieve_location(endpoint_or_url)
    return jsonify({'redirect': location}), status_code
