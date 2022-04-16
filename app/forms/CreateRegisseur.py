from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CreateRegisseur(FlaskForm):
    voornaam = StringField('Voornaam:')
    achternaam = StringField('Achternaam:')
    submit = SubmitField('Toevoegen')
