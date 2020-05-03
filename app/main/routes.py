from flask import render_template
from flask_login import current_user, login_user, logout_user
from app.main import bp

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

