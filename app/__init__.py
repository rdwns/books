from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

login.login_view = 'auth.login'
login.login_message = 'Please login to access this page'

def create_app():

    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    with app.app_context():

        from app.auth import bp as auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        from app.main import bp as main_bp
        app.register_blueprint(main_bp, url_prefix='/')

        from app.search import bp as search_bp
        app.register_blueprint(search_bp, url_prefix='/search')

        return app

from app import models