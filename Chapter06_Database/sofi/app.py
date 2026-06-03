from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms.fields import StringField, DecimalField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from flask_sqlalchemy import SQLAlchemy
from os import path, makedirs

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AAKKKSJDDHDHDHDH%5'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + path.join(path.dirname(__file__), "test.db")
db = SQLAlchemy(app)

UPLOAD_PATH = path.join('static', 'uploads')
makedirs(UPLOAD_PATH, exist_ok=True)

class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, default="Unknown")
    artist = db.Column(db.String(64))
    img = db.Column(db.String())
    is_active = db.Column(db.Boolean())
    created = db.Column(db.DateTime())
    information = db.Column(db.Text())

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    category = db.relationship("Category", back_populates = "photos")


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())

    photos = db.relationship("Photo", back_populates="category")

    def __repr__(self):
        return f"{self.title}"

class PhotoForm(FlaskForm):
    gmail = StringField('Your Gmail Address', validators=[DataRequired()])
    title = StringField('Photo Title', validators=[DataRequired()])
    artist = StringField('Name of the Artist', validators=[DataRequired()])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    img = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], FileSize(1024 * 1024 * 5))])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    name = StringField('Name and Surname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo("password",
                                                                                     message="Passwords must be equal to each other")])
    countries = SelectField('Country', choices=[("GE", "Georgia"), ("GER", 'Germany'), ("IT", 'Italy')],
                            validators=[DataRequired()])
    remember_me = BooleanField('Remember me', validators=[DataRequired()])
    submit = SubmitField('Register', validators=[DataRequired()])

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
            raise ValidationError('Password requires lower case letters')

        if not has_upper:
            raise ValidationError('Password requires upper case letters')

        if not has_digit:
            raise ValidationError('Password requires digit')

        if not has_punctuation:
            raise ValidationError('Password requires punctuation')


@app.route('/')
def index():
    photos = Photo.query.all()
    return render_template("index.html", title="Gallery", photos=photos)


@app.route('/photos')
def photos():
    photos = Photo.query.all()
    return render_template('photos.html', photos=photos)


@app.route('/photos/<int:id>')
def photo(id):
    p = Photo.query.get_or_404(id)
    return render_template('photo.html', photo=p)


@app.route('/delete/<int:id>')
def delete(id):
    photo = Photo.query.get(id)
    db.session.delete(photo)
    db.session.commit()

    return redirect(url_for('photos'))


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = PhotoForm()
    form.category.choices = [(c.id, c.title) for c in Category.query.all()]

    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(UPLOAD_PATH, img.filename))
        new_photo = Photo(
            title=form.title.data,
            artist=form.artist.data,
            img=path.join('static', 'uploads', img.filename),
            category_id=form.category.data
        )
        db.session.add(new_photo)
        db.session.commit()
        return redirect(url_for('photos'))
    else:
        print(form.errors)
    return render_template('submit.html', form=form)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def edit(id):
    photo = Photo.query.get_or_404(id)
    form = PhotoForm()

    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(UPLOAD_PATH, img.filename))
        photo.title = form.title.data
        photo.artist = form.artist.data
        photo.img = path.join('static', 'uploads', img.filename)
        db.session.commit()
        return redirect(url_for('photos'))
    else:
        print(form.errors)

    return render_template('submit.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(form.name.data)
        print(form.password.data)
        print(form.password2.data)
        print(form.countries.data)
        print(form.remember_me.data)
    else:
        print(form.errors)

    return render_template('register.html', form=form)


print(__name__)

if __name__ == '__main__':
    app.run(debug=True)
