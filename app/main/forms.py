from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, TextAreaField

class ImportForm(FlaskForm):
    csvfile = FileField('Import CSV', validators=[FileRequired(), FileAllowed(['csv', 'png'], 'CSV Files Only')])
    submit = SubmitField('Upload')

class ReviewForm(FlaskForm):
    review = TextAreaField('Share Your Review')
    submit = SubmitField('Share')