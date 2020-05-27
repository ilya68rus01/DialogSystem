from flask_wtf import FlaskForm
from wtforms import Label, StringField, SubmitField
from wtforms.validators import DataRequired


class QAForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
    answer = StringField('Answer')
    submit = SubmitField('Send')