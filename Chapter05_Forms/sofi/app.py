from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms.fields import StringField, DecimalField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from os import path, makedirs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AAKKKSJDDHDHDHDH%5'
UPLOAD_PATH = path.join('static', 'uploads')
makedirs(UPLOAD_PATH, exist_ok=True)

class Photo():
    def __init__(self, id, title, artist, img):
        self.id = id
        self.title = title
        self.artist = artist
        self.img = img

class PhotoForm(FlaskForm):
    gmail = StringField('Your Gmail Address', validators=[DataRequired()])
    title = StringField('Photo Title', validators=[DataRequired()])
    artist = StringField('Name of the Artist', validators=[DataRequired()])
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


photo1 = Photo(0, "Hand mosaic", "Unknown",
               "https://scontent.ftbs6-2.fna.fbcdn.net/v/t1.15752-9/694531756_858353106637023_2505383973973620837_n.png?_nc_cat=103&ccb=1-7&_nc_sid=9f807c&_nc_ohc=fSMV2d9nMbgQ7kNvwGOILNi&_nc_oc=AdpPA2OgfdMmi-DZBiXiFptF2dAIyVZUDWNIX8zXuHoP5P8U1pyoVPkkKFj-DnUlehA&_nc_zt=23&_nc_ht=scontent.ftbs6-2.fna&_nc_ss=7b2a8&oh=03_Q7cD5QGbJfuGqCMO9JRVNY6LX4RiHd19JKHF9p0j9hEeJnJJaQ&oe=6A2FCD7A")
photo2 = Photo(1, "Street Number Plate", "Unknown",
               "https://scontent.ftbs4-2.fna.fbcdn.net/v/t1.15752-9/694533369_1466854341908792_4842174725836018292_n.png?_nc_cat=105&ccb=1-7&_nc_sid=9f807c&_nc_ohc=0XJLNJhdnHIQ7kNvwEJC9vo&_nc_oc=AdrA0zSoT3ZARWJBAe1Z66ASrX5DypZibqqFjTSV3V39TIYnCiMQ5KBXd_axvMYP4AM&_nc_zt=23&_nc_ht=scontent.ftbs4-2.fna&_nc_ss=7b2a8&oh=03_Q7cD5QGS7wHZiqxilinVndn_p2cE8HpUL2TlTfoQpjUiWt9b8g&oe=6A2FDDE4")
photo3 = Photo(2, "Flower Sculpture Relief", "Unknown",
               "https://scontent.ftbs6-2.fna.fbcdn.net/v/t1.15752-9/693544242_1648723442908907_8796596297526633500_n.png?_nc_cat=106&ccb=1-7&_nc_sid=9f807c&_nc_ohc=Q0n4V9tJEV8Q7kNvwGc5rjN&_nc_oc=AdpT8ra-8rjQNlOFXwFqqsHyUFCH2gBI6CdIfqY2rZMLfS47Q116zOfdLlb2wA6BxEU&_nc_zt=23&_nc_ht=scontent.ftbs6-2.fna&_nc_ss=7a2a8&oh=03_Q7cD5QH_yYK_3DNU-9vQh712XrZdQoUQ5vqqmW0MJJsVwbtxPw&oe=6A2FE70E")
photo4 = Photo(3, "Park Bench Decoration", "Unknown",
               "https://scontent.ftbs4-2.fna.fbcdn.net/v/t1.15752-9/699879303_1293129706270009_2611754670896799763_n.png?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=DL5HmtyUBFIQ7kNvwFhEh02&_nc_oc=AdoyZ1G1nqlXYeACm0yc3cWB6LQMUewBw49oIHK7LgclL-jMTVHVC_MxApcO_SlcmQg&_nc_zt=23&_nc_ht=scontent.ftbs4-2.fna&_nc_ss=7a2a8&oh=03_Q7cD5QEIg7kSx-JAWZg1Y-80N4fzB8pXZZK_Zl_TruZQae_83Q&oe=6A2FB8EA")
photo5 = Photo(4, "Wall Decoration", "Lironism",
               "https://scontent.ftbs6-2.fna.fbcdn.net/v/t1.15752-9/696489407_971447965738608_4451664832830370176_n.png?_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_ohc=_JpE-rowz9sQ7kNvwGXzJ6j&_nc_oc=AdrYLuMtTaz3dN4vOsdApBFaQNuNrx6e8PMQ0FuAWavUzPorAvFKeTTTBc3eUMhCMJc&_nc_zt=23&_nc_ht=scontent.ftbs6-2.fna&_nc_ss=7a2a8&oh=03_Q7cD5QGqkAdZbyc6AEvNfjO_73bLI1Tp3G31a3gReyh5A7T01g&oe=6A2FE367")
photo6 = Photo(5, "Cat Paw Print", "Some random cat",
               "https://scontent.ftbs6-2.fna.fbcdn.net/v/t1.15752-9/667958067_1503340308209344_2076100038851782294_n.png?_nc_cat=108&ccb=1-7&_nc_sid=9f807c&_nc_ohc=4hSJ7ii3HCgQ7kNvwGbFJ4g&_nc_oc=AdoMxytBgl_aZgeqpDTxI3K2MTwa8utBPmYFOfCP-wfzzH7EcFpK7B77piFzlPt1knE&_nc_zt=23&_nc_ht=scontent.ftbs6-2.fna&_nc_ss=7a2a8&oh=03_Q7cD5QEhEbAugQy0LL9YguFPtT91JJvPtOWfFdiPnoaewRkfnw&oe=6A2FD95E")

gallery = [photo1, photo2, photo3, photo4, photo5, photo6]


@app.route('/')
def index():
    return render_template("index.html", title="Gallery", photos=gallery)


@app.route('/photos')
def photos():
    return render_template('photos.html', photos=gallery)


@app.route('/photos/<int:id>')
def photo(id):
    return render_template('photo.html', photo=gallery[id])


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = PhotoForm()
    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(UPLOAD_PATH, img.filename))
        # Fix: use gallery (not photos), and correct field order to match Photo(id, title, artist, img)
        gallery.append(Photo(len(gallery), form.title.data, form.artist.data, path.join('static', 'uploads', img.filename)))
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


app.run(debug=True)
