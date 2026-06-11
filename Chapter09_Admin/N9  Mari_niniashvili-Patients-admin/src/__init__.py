
from flask import Flask
from flask_admin.menu import MenuLink
from src.config import Config
from flask import url_for
from src.ext import db, migrate,login_manager,admin

from src.models.patient import Patient
from src.models.insurance_comp import Insurance
from src.models.user import User

from src.views.main.routes import main_bp
from src.views.auth.routes import auth_bp
from src.views.patient.routes import patient_bp
from src.views.insurance.routes import insurance

from src.commands import init_db, populate_db 

from src.admin_views.user import UserView
from src.admin_views.patient import PatientView
from src.admin_views.insurance import InsuranceView
from src.admin_views.base import SecureIndexView

blueprints = [main_bp, auth_bp, patient_bp]
commands = [init_db, populate_db] 



blueprints=[main_bp,auth_bp,patient_bp]
commands = [init_db, populate_db]

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

   
    register_blueprint(app)
    register_extentions(app)
    register_commands(app)
    register_insurance(app)
    
    return app

def register_extentions(app):
    db.init_app(app)
    migrate.init_app(app,db)

    login_manager.init_app(app)
    login_manager.login_view = 'main.index'



    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    admin.init_app(app)
    admin.add_view(UserView(User, db.session))
    admin.add_view(PatientView(Patient, db.session))
    admin.add_view(InsuranceView(Insurance, db.session))
    

    admin.add_link(MenuLink('Logout', url='/logout'))
    admin.add_link(MenuLink('Site', url='/'))

def register_blueprint(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in commands:
        app.cli.add_command(command)
   

def register_insurance(app):
    app.register_blueprint(insurance)

    