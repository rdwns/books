from flask import url_for, render_template, redirect, flash
from flask_login import current_user, login_required
from app.search.forms import SearchForm
from app.models import Book
from sqlalchemy import or_, and_
from app.search import bp
from app import db


@bp.route('/', methods=['GET', 'POST'])
@login_required
def search():

    form = SearchForm()
    results = ''
    if form.validate_on_submit():
        results = Book.query.filter(or_(Book.isbn==form.isbn.data, Book.author.contains(form.author.data), Book.title==form.title.data)).all()

        if not results:
            flash('No entries found')



    return render_template('search.html', form=form, results=results)
