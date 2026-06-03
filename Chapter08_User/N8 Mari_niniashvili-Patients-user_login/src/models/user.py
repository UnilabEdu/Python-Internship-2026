
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from src.models.base import BaseModel
from src.ext import db



class User(BaseModel,UserMixin):
    __tablename__="users0" 
    
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    _password = db.Column(db.String(128))


    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        self._password = generate_password_hash(password)

