from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_restx import Api
from flask_jwt_extended import JWTManager

from src.admin_views.base import SecureIndexView

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin(name='PianoBar', index_view=SecureIndexView())
api = Api(prefix='/api', doc='/api/docs', authorizations={'JsonWebToken': {'type': 'apiKey',
                                                                           'it': 'header',
                                                                           'name': 'Authorization',}})
jwt = JWTManager()