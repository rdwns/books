from flask import url_for, render_template, redirect, flash
from flask_login import current_user, login_user, logout_user
from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from app import db
from app.auth import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.index'))

    return render_template('login.html', title='Login', form=form)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully signed up!')
        return redirect(url_for('auth.login'))

    return render_template('signup.html', title='Sign Up', form=form)

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    if current_user.is_anonymous:
        return redirect(url_for('main.index'))
    logout_user()
    flash ('You have logged out successfully')
    return redirect(url_for('main.index'))