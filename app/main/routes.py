from flask import render_template, redirect, flash, url_for, request, current_app as app
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import secure_filename
from app.main import bp
from app.models import Book
from app.main.forms import ImportForm
import os

@bp.route('/')
@bp.route('/index')
def index():

    if current_user.is_anonymous:
        user='Stranger'
    else:
        user= current_user.username
    return render_template('index.html', name=user)

@bp.route('/book')
def book():
    return render_template('book.html')

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
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Uploaded Successfully!')
    else:
        filename=None
    return render_template('import.html', form=form, filename=filename)


# @bp.route('/upload', methods=['GET','POST'])
# def upload():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))

#         Book.importbooks(f)
#         return 'File Upload Success'





