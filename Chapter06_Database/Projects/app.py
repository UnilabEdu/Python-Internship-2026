from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms.fields import StringField, DecimalField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from flask_sqlalchemy import SQLAlchemy
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from os import path


app = Flask(__name__)

app.config["SECRET_KEY"] = "ALFJDSLFJO@##@!AFLJLKDSFL"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(path.dirname(__file__), "test.db")

db = SQLAlchemy(app)

UPLOAD_PATH = path.join(path.dirname(__file__), 'static', 'uploads')

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    films = db.relationship('Film', back_populates='actors', secondary='film_actors')
    def __repr__(self):
        return f"{self.name}"

class FilmActor(db.Model):
    __tablename__ = 'film_actors'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'))
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'))

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    actors = db.relationship('Actor', back_populates='films', secondary='film_actors')
    def __repr__(self):
        return f"{self.name}"

class Product(db.Model):
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

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    products = db.relationship("Product", back_populates="category")

    def __repr__(self):
        return f"{self.name}"


class ProductForm(FlaskForm):
    name = StringField('პროდუქტის სახელი', validators=[DataRequired()])
    price = DecimalField('ფასი', validators=[DataRequired()])
    category = SelectField('კატეგორია', choices=[])
    img = FileField('ფოტო', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png']), FileSize(max_size=1024*1024*10)])
    submit = SubmitField('დამატება')



class RegisterForm(FlaskForm):
    name = StringField('სახელი და გვარი', validators=[DataRequired()])
    password = PasswordField('პაროლი',  validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('გაიმეორე პაროლი',  validators=[DataRequired(), EqualTo("password", message="პაროლები უნდა უდრიდეს ერთმანეთს")])
    countre = SelectField('ქვეყანა', choices=[("GE", "საქართველო"), ("GER",'გერმანია'), ("IT", 'იტალია')], validators=[DataRequired()])
    remember_me = BooleanField('დამიმახსოვრე', validators=[DataRequired()])
    submit = SubmitField('რეგისტრაცია', validators=[DataRequired()])

    def validate_password(self, field):
        has_lower = False
        has_upper = False
        has_digit = False
        has_punctuation = False

        for char in field.data:
            if char in ascii_lowercase:
                has_lower = True
            if char in ascii_uppercase:
                has_upper = True
            if char in digits:
                has_digit = True
            if char in punctuation:
                has_punctuation = True

        if not has_lower:
            raise ValidationError('პაროლში საჭიროა პატარა ასოების გამოყენება')

        if not has_upper:
            raise ValidationError('პაროლში საჭიროა დიდი ასოების გამოყენება')

        if not has_digit:
            raise ValidationError('პაროლში საჭიროა რიცხვი')

        if not has_punctuation:
            raise ValidationError('პაროლში საჭიროა პუნქტუაციის გამოყენება')

@app.route('/')
def index():
    actor = Actor.query.get(1)

    print(actor.films)

    pianos = Product.query.all()
    return render_template("index.html", title='პროდუქტები', products=pianos)

@app.route('/products')
def products():
    pianos = Product.query.all()
    return render_template('products.html', products=pianos)

@app.route('/products/<int:id>')
def product(id):
    piano = Product.query.get(id)
    print(piano.category.products)
    return render_template('produc.html', piano=piano)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = ProductForm()

    categories = Category.query.all()

    form.category.choices = [(category.id, category.name) for category in categories]
    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(UPLOAD_PATH, img.filename))

        piano = Product(name=form.name.data, price=form.price.data, category_id=form.category.data, img=path.join('static', 'uploads', img.filename))
        db.session.add(piano)
        db.session.commit()

    else:
        print(form.errors)
    return render_template('create.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def edit(id):
    piano = Product.query.get(id)
    form = ProductForm(name=piano.name, price=piano.price, img=piano.img)

    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(UPLOAD_PATH, img.filename))

        piano.name = form.name.data
        piano.price = form.price.data
        piano.img = path.join('static', 'uploads', img.filename)
        db.session.commit()

    else:
        print(form.errors)
    return render_template('create.html', form=form)
@app.route('/delete/<int:id>')
def delete(id):
    piano = Product.query.get(id)
    db.session.delete(piano)
    db.session.commit()

    return redirect(url_for('products'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(form.name.data)
        print(form.password.data)
        print(form.password2.data)
        print(form.countre.data)
        print(form.remember_me.data)
    else:
        print(form.errors)

    return render_template('register.html', form=form)

print(__name__)

if __name__ == '__main__':
    app.run(debug=True)
