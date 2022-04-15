from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, StringField
from wtforms.validators import DataRequired, ValidationError
from app.Models.User import User


class RegisterForm(FlaskForm):
    email = EmailField('E-mail adres:', validators=[DataRequired()])
    username = StringField('Gebruikersnaam:', validators=[DataRequired()])
    password = PasswordField('Wachtwoord:', validators=[DataRequired()])
    submit = SubmitField('Registreren')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres staat al geregistreerd.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Deze gebruikersnaam is al vergeven, probeer een ander naam!')
