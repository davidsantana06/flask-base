from app.lib.core.jinja import render_page
from . import home


@home.get('/')
def index():
    return render_page('home/index')
