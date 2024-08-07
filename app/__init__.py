from flask import Flask
from .config import configure_app_env, configure_modules, configure_extensions


def create_app() -> Flask:
    app = Flask(__name__)
    configure_app_env(app)
    configure_modules(app)
    configure_extensions(app)
    return app
