from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from app.models import Book

class SearchForm(FlaskForm):
    searchQuery = StringField('Search Query')

    submit = SubmitField('Search')


    def is_filled(data):
        if data == None:
            return False
        if data == '':
            return False
        if data == []:
            return False
        return True
