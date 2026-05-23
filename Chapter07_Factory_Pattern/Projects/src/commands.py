import click
from flask.cli import with_appcontext
from click import command

from src.models.product import Product, Category
from src.models.film import Film, Actor, FilmActor
from src.ext import db

@command('init_db')
@with_appcontext
def init_db():
    click.echo('Initializing database...')

    db.drop_all()
    db.create_all()

    click.echo('Done!')

@command('populate_db')
@with_appcontext
def populate_db():
    click.echo('Populating database...')
    category1 = Category(name='პიანინო')
    category2 = Category(name='როიალი')
    category3 = Category(name='ციფრული')
    category4 = Category(name='სხვა')
    categories = [category1, category2, category3, category4]
    for category in categories:
        category.create()

    piano1 = Product(name="ელექტრო პიანინო CASIO AP-270BNC2", price=10099.00,
                     img="https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg", category_id=category1.id)
    piano2 = Product(name="ელექტრო პიანინო AP-270BNC2", price=599.00,
                     img="https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg", category_id=category2.id)
    piano3 = Product(name="ელექტრო CASIO AP-270BNC2", price=9.00,
                     img="https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg", category_id=category3.id)
    piano4 = Product(name="პიანინო CASIO AP-270BNC2", price=99.00,
                     img="https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg", category_id=category1.id)

    pianos = [piano1, piano2, piano3, piano4]

    for piano in pianos:
        piano.create()

    Film(name='Avengers').create()
    Film(name='Avengers End Game').create()
    Film(name='Not Avengers').create()
    Actor(name='Jason momoa').create()
    Actor(name='Steheam').create()
    Actor(name='Bret Pit').create()

    FilmActor(actor_id=1, film_id=1).create()
    FilmActor(actor_id=2, film_id=1).create()
    FilmActor(actor_id=2, film_id=2).create()
    FilmActor(actor_id=3, film_id=2).create()
    FilmActor(actor_id=1, film_id=3).create()

    click.echo('Done!')
