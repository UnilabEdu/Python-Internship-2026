from pathlib import Path
from flask_login import current_user

from src.models import Product

def test_products(client):
    response = client.get('/products')

    assert response.status_code == 200

def test_product(client):
    response = client.get('/products/1')

    assert response.status_code == 200


def test_add_product_unauthenticated(client, app):
    img_file = open(Path(__file__).parent / 'resources' / 'piano1.jpg', 'rb')

    response = client.post('/create', data={'name': 'test name', 'price': 100, 'category': 2, 'img': img_file}, follow_redirects=True)

    with app.app_context():
        created_product = Product.query.filter_by(name='test name').first()

    assert not created_product
    assert response.request.path == '/login'
    assert response.status_code == 200

def test_add_product_authenticated(client):
    with client:
        client.post('/login', data={'name': 'admin', 'password': 'Password123!', 'submit': 1})

        print(current_user.is_admin())

        img_file = open(Path(__file__).parent / 'resources' / 'piano1.jpg', 'rb')

        response = client.post('/create', data={'name': 'test name', 'price': 100, 'category': 2, 'img': img_file}, follow_redirects=True)

        created_product = Product.query.filter_by(name='test name').first()

        assert not created_product
        assert response.status_code == 200

