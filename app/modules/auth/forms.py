from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class _AuthForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Length(1, 50)])
    password = PasswordField(validators=[DataRequired(), Length(1, 255)])


class LoginForm(_AuthForm):
    submit = SubmitField('Login')


class RegisterForm(_AuthForm):
    name = StringField(validators=[DataRequired(), Length(1, 50)])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password'), Length(1, 50)])
    submit = SubmitField()
