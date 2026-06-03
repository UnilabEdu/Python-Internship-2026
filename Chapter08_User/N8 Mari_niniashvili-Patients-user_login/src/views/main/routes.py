
from flask import Blueprint,render_template
from src.models.patient import Patient

main_bp = Blueprint('main',__name__)

@main_bp.route("/")
def index():

    patients=Patient.query.all()
    return render_template("main/index.html",title="პაციენტები",patients=patients)