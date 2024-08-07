from . import operations as user_operations, user


@user.get('/')
def index():
    names = [user.name for user in user_operations.get_all()]
    return f'Users: {names}'


@user.get('/view/<int:id>')
def view(id: int):
    user = user_operations.get_one_by_id(id)
    return f'User: {user.name}'


@user.get('/test')
def test():
    data = [
        {'name': 'David Santanta', 'password': 'dadá'},
        {'name': 'Giovana Silva', 'password': 'gigi'},
        {'name': 'Jesus Cristo', 'password': 'jeje'}
    ]
    for item in data:
        name, password = item['name'], item['password']
        user_operations.create(name, password)
    return 'd0nE!'
