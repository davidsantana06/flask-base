from os import path


ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))

ENV_FILE = path.join(ROOT_FOLDER, '.env')

APP_FOLDER = path.join(ROOT_FOLDER, 'app')
APP_MODULES_FOLDER = path.join(APP_FOLDER, 'modules')
APP_MODULE_FOLDER = path.join(APP_MODULES_FOLDER, '{}')
APP_MODULE_PATH = 'app.modules.{}'

DATABASE_FOLDER = path.join(ROOT_FOLDER, 'database')
DATABASE_FILE = path.join(DATABASE_FOLDER, 'flask_base.sqlite3')

OUTPUT_FOLDER = path.join(ROOT_FOLDER, 'output')

RESOURCES_FOLDER = path.join(ROOT_FOLDER, 'resources')
RES_COMMON_FOLDER = path.join(RESOURCES_FOLDER, 'common')
RES_COMMON_STATIC_FOLDER = path.join(RES_COMMON_FOLDER, 'static')
RES_COMMON_TEMPLATES_FOLDER = path.join(RES_COMMON_FOLDER, 'templates')
RES_MODULES_FOLDER = path.join(RESOURCES_FOLDER, 'modules')
RES_MODULE_STATIC_FOLDER = path.join(RES_MODULES_FOLDER, '{}', 'static')
RES_MODULE_TEMPLATES_FOLDER = path.join(RES_MODULES_FOLDER, '{}', 'templates')

UPLOADS_FOLDER = path.join(ROOT_FOLDER, 'uploads')
