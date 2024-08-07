from werkzeug.exceptions import HTTPException


def get_code(e: Exception) -> int:
    return e.code if (isinstance(e, HTTPException)) else 500


def get_description(code: int) -> str:
    return {
        400: 'Solicitação inválida.',
        401: 'Acesso não autorizado.',
        403: 'Acesso proibido.',
        404: 'Página não encontrada.',
        405: 'Método HTTP não permitido.',
        500: 'Erro interno do servidor.'
    }.get(code, 'Ocorreu um erro inesperado.')
