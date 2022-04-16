from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from app.Models.Acteur import Acteur
from app.Models.Regisseur import Regisseur
from wtforms.validators import DataRequired, ValidationError

class CreateActeur(FlaskForm):
    test = ""