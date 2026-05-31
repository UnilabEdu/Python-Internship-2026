from flask import Flask, url_for
from flask_admin.menu import MenuLink
from src.admin_views import UserView, ProductView, CategoryView, FilmView, ActorView, FilmActorView
from src.config import Config
from src.ext import db, migrate, login_manager, admin
from src.models import Product, Category, User, Film, Actor, FilmActor
from src.views import main_bp, auth_bp, product_bp
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

    # initialize login manager
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # initialize admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(CategoryView(Category, db.session))
    admin.add_view(FilmView(Film, db.session))
    admin.add_view(ActorView(Actor, db.session))
    admin.add_view(FilmActorView(FilmActor, db.session))
    admin.add_view(ProductView(Product, db.session))

    admin.add_link(MenuLink('Site', '/'))
    admin.add_link(MenuLink('Logout', '/logout'))


def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in commands:
        app.cli.add_command(command)


