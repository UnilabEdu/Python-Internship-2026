from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms.fields import StringField, DecimalField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from os import path

app = Flask(__name__)

app.config["SECRET_KEY"] = "ALFJDSLFJO@##@!AFLJLKDSFL"

UPLOAD_PATH = path.join(path.dirname(__file__), 'static', 'uploads')

class Product():
    def __init__(self, id, name, price, img):
        self.id = id
        self.name = name
        self.price = price
        self.img = img


class ProductForm(FlaskForm):
    name = StringField('პროდუქტის სახელი', validators=[DataRequired()])
    price = DecimalField('ფასი', validators=[DataRequired()])
    category = SelectField('კატეგორია', choices=['როიალი', 'პიანინო', 'ციფრული'])
    img = FileField('ფოტო', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], FileSize(1024*1024*5))])
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

piano1 = Product(0, "ელექტრო პიანინო CASIO AP-270BNC2", "10,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano2 = Product(1, "ელექტრო პიანინო CASIO AP-270BNC2", "5,000.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano3 = Product(2, "ელექტრო პიანინო CASIO AP-270BNC2", "4,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano4 = Product(3, "ელექტრო პიანინო CASIO AP-270BNC2", "6,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")

pianos = [piano1, piano2, piano3, piano4, piano1, piano2, piano3, piano4]

@app.route('/')
def index():
    return render_template("index.html", title='პროდუქტები', products=pianos)

@app.route('/products')
def products():
    return render_template('products.html', products=pianos)

@app.route('/products/<int:id>')
def product(id):
    return render_template('produc.html', piano=pianos[id])

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = ProductForm()
    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(UPLOAD_PATH, img.filename))
        pianos.append(Product(50, form.name.data, form.price.data, path.join('static', 'uploads', img.filename)))
    else:
        print(form.errors)
    return render_template('create.html', form=form)

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

app.run(debug=True)