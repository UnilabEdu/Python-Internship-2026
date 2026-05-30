from flask import Flask
from src.config import Config
from src.ext import db, migrate
from src.models.photo import Photo, Category

from src.views.main.routes import main_bp
from src.views.auth.routes import auth_bp
from src.views.photo.routes import photo_bp
import os

blueprints = [main_bp, auth_bp, photo_bp]

def create_app():
    app = Flask(__name__,
                template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))

    app.config.from_object(Config)

    print("Template folder:", app.template_folder)
    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprint(app)

    return app



def register_blueprint(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
