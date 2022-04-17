from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateActeur(FlaskForm):
    voornaam = StringField('Voornaam:', validators=[DataRequired()])
    achternaam = StringField('Achternaam:', validators=[DataRequired()])
    submit = SubmitField('Toevoegen')
