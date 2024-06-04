from flask import Blueprint, Flask
from importlib import import_module
from os import listdir

from app.constants import APP_MODULE_FOLDER, APP_MODULES_FOLDER, APP_MODULE_PATH, RES_MODULE_STATIC_FOLDER, RES_MODULE_TEMPLATES_FOLDER


def configure_modules(app: Flask) -> None:
    for module_name in listdir(APP_MODULES_FOLDER):
        module_folder = APP_MODULE_FOLDER.format(module_name)
        if '__init__.py' in listdir(module_folder):
            module_path = APP_MODULE_PATH.format(module_name)
            module = import_module(module_path)
            for _, item in module.__dict__.items():
                if isinstance(item, Blueprint):
                    item.static_folder = RES_MODULE_STATIC_FOLDER.format(item.name)
                    item.static_url_path = f'/{module_path}'
                    item.template_folder = RES_MODULE_TEMPLATES_FOLDER.format(item.name)
                    app.register_blueprint(item)
                    break
