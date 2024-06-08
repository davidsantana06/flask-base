from flask import flash


_SUCCESS, _DANGER = 'success', 'danger'
_WARNING, _INFO = 'warning', 'info'


def flash_success(message: str) -> None:
    flash(message, _SUCCESS)


def flash_danger(message: str) -> None:
    flash(message, _DANGER)


def flash_warning(message: str) -> None:
    flash(message, _WARNING)


def flash_info(message: str) -> None:
    flash(message, _INFO)
