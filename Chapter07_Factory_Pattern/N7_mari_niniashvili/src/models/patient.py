
from src.ext import db
from src.models.base import BaseModel


class Patient(BaseModel):

    __tablename__= "patients"

    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())
    id_number = db.Column(db.String())
    age = db.Column(db.Integer())
    country=db.Column(db.String())
    gender = db.Column(db.String())
    img = db.Column(db.String())

