from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from app.Models.Acteur import Acteur
from app.Models.Regisseur import Regisseur
from wtforms.validators import DataRequired, ValidationError


class CreateFilm(FlaskForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.acteur.choices = [(acteur.id, acteur.voornaam + ' ' + acteur.achternaam) for acteur in Acteur.query.all()]
        self.regisseur.choices = [(regisseur.id, regisseur.voornaam + ' ' + regisseur.achternaam) for regisseur in
                                  Regisseur.query.all()]

    titel = StringField('Titel:', validators=[DataRequired()])
    regisseur = SelectField('Regisseur:', coerce=int, validators=[DataRequired()])
    acteur = SelectField('Acteur:', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Toevoegen')

    def validate_regisseur(self, field):
        if not Regisseur.query.filter_by(id=field.data):
            raise ValidationError('Deze regisseur bestaat niet')

    def validate_acteur(self, field):
        if not Regisseur.query.filter_by(id=field.data):
            raise ValidationError('Deze regisseur bestaat niet')
