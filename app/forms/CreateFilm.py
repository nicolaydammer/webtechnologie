from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from app.Models.Acteur import Acteur
from app.Models.Regisseur import Regisseur
from wtforms.validators import DataRequired, ValidationError

regisseurs = Regisseur.query.all()
acteurs = Acteur.query.all()


class CreateFilm(FlaskForm):
    titel = StringField('Titel:', validators=[DataRequired()])
    regisseur = SelectField('Regisseur:', choices=regisseurs, validators=[DataRequired()])
    acteur = SelectField('Acteur:', choices=acteurs, validators=[DataRequired()])
    submit = SubmitField('Toevoegen')

    def validate_regisseur(self, field):
        if not Regisseur.query.filter_by(id=field.data):
            raise ValidationError('Deze regisseur bestaat niet')

    def validate_acteur(self, field):
        if Regisseur.query.filter_by(id=field.data):
            raise ValidationError('Deze regisseur bestaat niet')
