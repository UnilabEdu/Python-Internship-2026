from flask_restx import Resource

from src.ext import api
from src.models import Film
from src.endpoints.film import film_model, film_ns

@film_ns.route('/')
class FilmAPI(Resource):

    @film_ns.marshal_with(film_model)
    def get(self):
        products = Film.query.all()

        return products, 200

