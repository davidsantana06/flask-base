from . import home


@home.get('/')
def index():
    return 'Flask Base!'
