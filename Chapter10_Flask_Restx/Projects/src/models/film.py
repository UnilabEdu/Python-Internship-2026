from src.ext import db
from src.models.base import BaseModel

class Actor(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    test = db.Column(db.Boolean)

    films = db.relationship('Film', back_populates='actors', secondary='film_actors')
    def __repr__(self):
        return f"{self.name}"

class FilmActor(BaseModel):
    __tablename__ = 'film_actors'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))

class Film(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    actors = db.relationship('Actor', back_populates='films', secondary='film_actors')
    def __repr__(self):
        return f"{self.name}"