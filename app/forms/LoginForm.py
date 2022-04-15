from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('E-mail adres:', validators=[DataRequired()])
    password = PasswordField('Wachtwoord:', validators=[DataRequired()])
    submit = SubmitField('Login')
