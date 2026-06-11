from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_required
from os import path

from src.config import Config
from src.models.product import Product, Category
from src.views.product.forms import ProductForm

product_bp = Blueprint('prod', __name__)

@product_bp.route('/products')
def products():
    pianos = Product.query.all()
    return render_template('product/products.html', products=pianos)

@product_bp.route('/products/<int:id>')
def product(id):

    piano = Product.query.get(id)
    print(piano.category.products)
    return render_template('product/produc.html', piano=piano)

@product_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = ProductForm()

    categories = Category.query.all()

    form.category.choices = [(category.id, category.name) for category in categories]
    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(Config.UPLOAD_PATH, img.filename))

        piano = Product(name=form.name.data, price=form.price.data, category_id=form.category.data, img=path.join('static', 'uploads', img.filename))
        piano.create()


    else:
        print(form.errors)
    return render_template('product/create.html', form=form)


@product_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    piano = Product.query.get(id)
    form = ProductForm(name=piano.name, price=piano.price, img=piano.img)

    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(Config.UPLOAD_PATH, img.filename))

        piano.name = form.name.data
        piano.price = form.price.data
        piano.img = path.join('static', 'uploads', img.filename)
        piano.save()

    else:
        print(form.errors)
    return render_template('product/create.html', form=form)

@login_required
@product_bp.route('/delete/<int:id>')
def delete(id):
    piano = Product.query.get(id)
    piano.delete()

    return redirect(url_for('prod.products'))
