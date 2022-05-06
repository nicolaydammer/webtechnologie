from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField('Commentaar:', validators=[DataRequired()])
    submit = SubmitField('Commentaar opslaan')
