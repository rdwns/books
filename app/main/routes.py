from flask import render_template, redirect, flash, url_for, request, current_app as app, json
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import secure_filename
from app.main import bp
from app.models import Book, Review
from app.main.forms import ImportForm, ReviewForm
import os, requests
from app import db

@bp.route('/')
@bp.route('/index')
def index():

    if current_user.is_anonymous:
        user='Stranger'
    else:   
        user= current_user.username
    return render_template('index.html', name=user)

@bp.route('/book/<isbn>', methods=['GET', 'POST'])
def book(isbn):
    grParams = {'isbns': isbn , 'key':os.environ['GOODREADS_API_KEY']}
    ratings = requests.get('https://www.goodreads.com/book/review_counts.json', params=grParams)
    stars = ratings.json()['books'][0]['average_rating']

    form = ReviewForm()
    if form.validate_on_submit():
        preventSecondReview = Review.query.filter(Review.uid==current_user.id).first()
        if preventSecondReview is not None:
            flash('You cannot post two reviews!')
        else:
            review = Review(isbn=isbn, uid=current_user.id, review=form.review.data)
            db.session.add(review)
            db.session.commit()

    bookTitle = Book.query.filter(Book.isbn==isbn).first()
    allReviews = Review.query.filter(Review.isbn==isbn).all()
    return render_template('book.html', form=form, allReviews=allReviews, bookTitle=bookTitle, stars=stars)

@bp.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

@bp.route('/import', methods=['GET', 'POST'])
def import_csv():
    path = '/uploads'
    form = ImportForm()
    if form.validate_on_submit():
        f = form.csvfile.data
        filename = secure_filename(f.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(filepath)
        Book.importbooks(filepath)
        flash('Successfully imported')
    else:
        filename=None
    return render_template('import.html', form=form, filename=filename)


# @bp.route('/upload', methods=['GET','POST'])
# def upload():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))

#
#         return 'File Upload Success'





