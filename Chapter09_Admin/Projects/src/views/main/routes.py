from flask import render_template, Blueprint

from src.models.product import Product

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    pianos = Product.query.all()
    return render_template("main/index.html", title='პროდუქტები', products=pianos)