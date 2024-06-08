from flask import url_for


_CSS_EXTENSION = '.css'
_CSS_FILE_PATH = 'css/{}'
_JS_EXTENSION = '.js'
_JS_FILE_PATH = 'js/{}'
_IMG_FILE_PATH = 'img/{}'
_OWN_MODULE = '.'


def _url_for_static(file_name: str, module: str) -> str:
    return url_for(f'{module}static', filename=file_name)


def url_for_css(css_name: str, module: str = _OWN_MODULE) -> str:
    if not css_name.endswith(_CSS_EXTENSION):
        css_name += _CSS_EXTENSION
    return _url_for_static(_CSS_FILE_PATH.format(css_name), module)


def url_for_img(img_name: str, module: str = _OWN_MODULE) -> str:
    return _url_for_static(_IMG_FILE_PATH.format(img_name), module)


def url_for_js(js_name: str, module: str = _OWN_MODULE) -> str:
    if not js_name.endswith(_JS_EXTENSION):
        js_name += _JS_EXTENSION
    return _url_for_static(_JS_FILE_PATH.format(js_name), module)
