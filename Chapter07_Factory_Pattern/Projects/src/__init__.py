from flask import Flask
from src.config import Config
from src.ext import db, migrate
from src.models.product import Product, Category
from src.models.film import Film, Actor, FilmActor
from src.views.main.routes import main_bp
from src.views.auth.routes import auth_bp
from src.views.product.routes import product_bp
from src.commands import init_db, populate_db

blueprints = [main_bp, auth_bp, product_bp]
commands = [init_db, populate_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extentions(app)

    register_blueprints(app)

    register_commands(app)

    return app

def register_extentions(app):
    # initialize database
    db.init_app(app)

    # initialize migration
    migrate.init_app(app, db)


def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in commands:
        app.cli.add_command(command)


