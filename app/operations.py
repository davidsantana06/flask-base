from flask_wtf import FlaskForm
from .lib.database import PopulateMixin


def validate_form(form: FlaskForm) -> bool:
    return form.validate_on_submit()


def populate_form(form: FlaskForm, model: PopulateMixin) -> None:
    model.populate_form(form)
