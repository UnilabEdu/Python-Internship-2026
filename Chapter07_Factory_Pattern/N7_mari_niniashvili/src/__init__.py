
from flask import Flask
from src.config import Config
from src.ext import db,migrate
from src.models.patient import Patient
from src.views.main.routes  import  main_bp
from src.views.auth.routes  import  auth_bp
from src.views.patient.routes  import patient_bp
from src.commands import init_db,populate_db

blueprints=[main_bp,auth_bp,patient_bp]
commands = [init_db, populate_db]

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

   
    register_blueprint(app)
    register_extentions(app)
    register_commands(app)
    
    return app

def register_extentions(app):
    db.init_app(app)
    migrate.init_app(app,db)
    
def register_blueprint(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def register_commands(app):
    for command in commands:
        app.cli.add_command(command)
   



    