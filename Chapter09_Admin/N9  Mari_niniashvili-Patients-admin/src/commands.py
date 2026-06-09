import click
from flask.cli import with_appcontext

from src.ext import db
from src.models.patient import Patient


@click.command('init_db')
@with_appcontext
def init_db():
    click.echo('initializing...')

    db.drop_all()
    db.create_all()

    click.echo('Done!')


@click.command('populate_db')
@with_appcontext
def populate_db():

    patients = [
        Patient(name="ტატო", id_number="000", age=22, gender="female",city="თბილისი",
                img="ლიკა.jpg"),

        Patient(name="ლიკა", id_number="1111", age=88, gender="female",city="თბილისი",
                img="https://stock.adobe.com/ge/search?k=person+face+background"),

        Patient(name="ირა", id_number="2222", age=78, gender="female",city="თბილისი",
                img="https://stock.adobe.com/ge/search?k=person+face+background"),

  
    ]

    for patient in patients:
        patient.create()

    click.echo("Patients added!")