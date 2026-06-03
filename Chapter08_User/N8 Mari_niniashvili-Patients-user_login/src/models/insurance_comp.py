from flask_wtf import FlaskForm
from wtforms .fields import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from flask_wtf.file import FileField,FileAllowed
from src.ext import db

class Insurance(db.Model):
    __tablename__ = 'insurance'

    id = db.Column(db.Integer, primary_key=True)
    insurance = db.Column(db.String(100), nullable=False)
    id_number = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)











