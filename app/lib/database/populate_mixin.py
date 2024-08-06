from flask_wtf import FlaskForm


class PopulateMixin():
    def populate_form(self, form: FlaskForm) -> None:
        for field in form:
            if hasattr(self, field.name):
                field.data = getattr(self, field.name)

    def populate_obj(self, obj: object) -> None:
        for attr in obj.__dict__:
            if hasattr(self, attr):
                value = getattr(self, attr)
                setattr(obj, attr, value)
