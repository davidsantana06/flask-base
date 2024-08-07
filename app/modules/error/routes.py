from . import operations as error_operations, error


@error.app_errorhandler(Exception)
def error_handler(e: Exception):
    code = error_operations.get_code(e)
    description = error_operations.get_description(code)
    return f'E{code}: {description}'
