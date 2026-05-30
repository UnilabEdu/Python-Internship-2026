from src.ext import db
from src.models.base import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Float())
    img = db.Column(db.String())
    is_active = db.Column(db.Boolean())
    created = db.Column(db.DateTime())
    information = db.Column(db.Text())


    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    category = db.relationship("Category", back_populates="products")

    def __repr__(self):
        return f"{self.name}"

class Category(BaseModel):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    products = db.relationship("Product", back_populates="category")

    def __repr__(self):
        return f"{self.name}"