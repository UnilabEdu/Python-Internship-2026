from flask_restx import fields

from src.ext import api

film_ns = api.namespace('film', description='Film related operations')

film_model = api.model('film', {'id': fields.Integer,
                                'name': fields.String})

