from flask import Flask,render_template,url_for,request,redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms.fields import StringField, PasswordField,SelectField,BooleanField, SubmitField, DecimalField,IntegerField,DateField
from wtforms.validators import DataRequired, EqualTo,Length,ValidationError
from string import ascii_lowercase, ascii_uppercase,digits,punctuation
from wtforms import TextAreaField
import os
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config["SECRET_KEY"] = "asd1d2g3d;IOISie0w09"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.dirname(__file__),"test.db")
db=SQLAlchemy(app)

class Patient(db.Model):
    __filename__= "patients"
    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())
    id_number = db.Column(db.String())
    age = db.Column(db.Integer())
    gender = db.Column(db.String())
    img = db.Column(db.String())


class PatientForm(FlaskForm):
    name = StringField("პაციენტის სახელი", validators=[DataRequired()])
    id_number = StringField("პირადი ნომერი", validators=[DataRequired()])
    age = IntegerField("ასაკი", validators=[DataRequired()])
    gender = SelectField("სქესი",choices=[("male", "მამრობითი"), ("female", "მდედრობითი")],validators=[DataRequired()])
    img = FileField("დაამატე სურათი", validators=[DataRequired(),FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField("დამატება")

class RegisterForm(FlaskForm):
    name = StringField("სახელი და გვარი",validators =[DataRequired()] )
    password1 = PasswordField("პაროლი",validators =[DataRequired(),Length(min=4,max=10)] )
    password2 = PasswordField("გაიმეორე პაროლი",validators =[DataRequired(),EqualTo("password1", message="პაროლები უნდა ეთხვეოდეს")] )
    countries = SelectField("აირჩიე ქვეყანა",choices=[("GE", "საქართველო"), ("DE", "გერმანია"), ("IT", "იტალია")],validators =[DataRequired()])
    remember_me = BooleanField("დამიმახსოვრე")
    submit = SubmitField("რეგისტრაცია")

    def validate_password1(self,field):
        has_lower=False
        has_upper=False
        has_digit=False
        has_punctuations=False

        for char in field.data:
            if char in ascii_lowercase:
                has_lower=True
            if char in ascii_uppercase:
                has_upper=True
            if char in digits:
                has_digit=True
            if char in punctuation:
                has_punctuations=True
        

        if not has_lower:
            raise ValidationError("შეიტანეთ პატარა ასოები")
        if not has_upper:
            raise ValidationError("შეიტანეთ დიდი ასოები")
        if not has_digit:
            raise ValidationError("შეიტანეთ ციფრები")
        if not has_punctuations:
            raise ValidationError("შეიტანეთ პუნქტუაციის ნიშნები")

with app.app_context():
    all_patients= Patient.query.all()
    print(all_patients)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/patients")
def patients_list():
     all_patients=Patient.query.all()
     return render_template("patients.html",patients=all_patients)

@app.route("/patients/<int:id>")
def patient(id):
    patient=Patient.query.get(id)
    return render_template("patient.html",patient = patient)

@app.route("/create", methods=["GET", "POST"])
def create():
    form = PatientForm()
    if form.validate_on_submit():
        img = form.img.data
        UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'static', 'uploads', img.filename)
        img.save(UPLOAD_PATH)
       
        patient=Patient(name=form.name.data,id_number=form.id_number.data,age=form.age.data,gender=  form.gender.data,img=f"/static/uploads/{img.filename}" )
        db.session.add(patient)
        db.session.commit()
        return "პაციენტი დამატებულია"

    if form.is_submitted():
        print("ფორმის შეცდომები:", form.errors)

    return render_template("create.html", form=form)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    patient = Patient.query.get(id)

    if request.method == "POST":
        form = PatientForm()
    else:
        form = PatientForm(name=patient.name, id_number=patient.id_number, age=patient.age, gender=patient.gender, img=patient.img)

    if form.validate_on_submit():
        if form.img.data:
            img = form.img.data
            UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'static', 'uploads', img.filename)
            img.save(UPLOAD_PATH)
            patient.img = f"/static/uploads/{img.filename}"

        patient.name = form.name.data
        patient.id_number = form.id_number.data
        patient.age = form.age.data
        patient.gender = form.gender.data

        db.session.commit()
        return "მონაცემები რედაქტირებულია"

    else:
        print("ფორმის შეცდომები:", form.errors)

    return render_template("create.html", form=form, patient=patient)


@app.route("/delete/<int:id>")
def delete(id):
    patient = Patient.query.get(id)
    db.session.delete(patient)
    db.session.commit()

    return redirect(url_for('patients_list'))

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return "დამატებულია!"
    else:
        print(form.errors)
    return render_template("register.html",form=form)

if __name__=="__main__":
    app.run(debug = True,port=5001)