from datetime import datetime
from flask import render_template
from http import HTTPStatus
from typing import Dict

from app.lib.utils.url_composer import (
    url_for_css, url_for_img, url_for_js,
    url_for_common_css, url_for_common_img, url_for_common_js
)

from .response import Response


_TEMPLATE_EXTENSION = '.html.j2'
_LAYOUTS_FOLDER = 'layouts/'
_MACROS_FOLDER = 'macros/'
_PAGES_FOLDER = 'pages/'


def _normalize_template_name(template_name: str) -> str:
    if not template_name.endswith(_TEMPLATE_EXTENSION):
        template_name += _TEMPLATE_EXTENSION
    return template_name


def _layout(layout_name: str) -> str:
    return f'{_LAYOUTS_FOLDER}{_normalize_template_name(layout_name)}'


def _macro(macro_name: str) -> str:
    return f'{_MACROS_FOLDER}{_normalize_template_name(macro_name)}'


def render_page(page_name: str, data: Dict[str, object] = {}, status_code: int = HTTPStatus.OK) -> Response:
    last_slash_index = page_name.rfind('/')
    if last_slash_index != - 1:
        page_part, module_part = page_name[last_slash_index + 1:], f'{page_name[:last_slash_index]}/'
    else:
        page_part, module_part = page_name, ''
    normalized_page_name = f'{module_part}{_PAGES_FOLDER}{_normalize_template_name(page_part)}'
    context = {
        'layout': lambda layout_name: f'{module_part}{_layout(layout_name)}',
        'common_layout': _layout,
        'macro': lambda macro_name: f'{module_part}{_macro(macro_name)}',
        'common_macro': _macro,
        'css': url_for_css,
        'common_css': url_for_common_css,
        'img': url_for_img,
        'common_img': url_for_common_img,
        'js': url_for_js,
        'common_js': url_for_common_js,
        'current_datetime': datetime.now(),
        **data
    }
    return render_template(normalized_page_name, **context), status_code
