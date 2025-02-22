from flask import url_for, render_template, redirect, flash, request, json
from flask_login import current_user, login_required
from app.search.forms import SearchForm
from app.models import Book
from sqlalchemy import or_, and_
from app.search import bp
import os, requests
from app import db



@bp.route('/', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    results = ''
    grParams={'key':os.environ['GOODREADS_API_KEY']}
    if form.validate_on_submit():
        results = Book.query.filter(or_(Book.isbn.contains(form.searchQuery.data), Book.author.contains(form.searchQuery.data), Book.title.contains(form.searchQuery.data))).all()
        if not results:
            flash('No entries found')

    return render_template('search.html', form=form, results=results)
