from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ModifyRegisseur(FlaskForm):
    voornaam = StringField('Voornaam:', [DataRequired()])
    achternaam = StringField('Achternaam:', [DataRequired()])
    submit = SubmitField('Opslaan', [DataRequired()])
