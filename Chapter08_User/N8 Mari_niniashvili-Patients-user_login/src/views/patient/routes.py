from flask import Blueprint,render_template,request,url_for,redirect,request
from flask_login import login_required
from src.config import Config
from src.models.patient import Patient
from os import path
from src.views.patient.forms import PatientForm
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

patient_bp=Blueprint('patient',__name__)

@patient_bp.route("/patients")
def patients_list():
    all_patients=Patient.query.all()
    return render_template("patient/patients.html",patients=all_patients)

@patient_bp.route("/patients/<int:id>")
def patient(id):
    patient=Patient.query.get(id)
    return render_template("patient/patient.html",patient = patient)


@patient_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = PatientForm()
    form.img.validators.append(DataRequired())
    if form.validate_on_submit():
        img = form.img.data
        filename=None
        if img:
            filename = img.filename
            upload_path = path.join("src", "static", "uploads", filename)
            img.save(upload_path)

        patient = Patient(
            name=form.name.data,
            id_number=form.id_number.data,
            age=form.age.data,
            gender=form.gender.data,
            img=f"/static/uploads/{filename}"  if filename else None )
        patient.create()

        return "პაციენტი დამატებულია"

    else:
        if form.is_submitted():
            print("ფორმის შეცდომები:", form.errors)

    return render_template("patient/create.html", form=form)

@patient_bp.route("/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    patient = Patient.query.get(id)
    form = PatientForm()
    form.img.validators=[FileAllowed(['jpg','png','jpeg'])]

    if request.method == "POST":
        if form.validate_on_submit():

            if form.img.data :
                img = form.img.data
                filename = img.filename
                upload_path = path.join(Config.UPLOAD_PATH, filename)
                img.save(upload_path)
 
      
            patient.name = form.name.data
            patient.id_number = form.id_number.data
            patient.age = form.age.data
            patient.gender = form.gender.data

            patient.save()
            return "მონაცემები რედაქტირებულია"

        else:
            print("ფორმის შეცდომები:", form.errors)

    else:
       
            form.name.data=patient.name
            form.id_number.data=patient.id_number
            form.age.data=patient.age
            form.gender.data=patient.gender


    return render_template("patient/create.html", form=form, patient=patient)



@patient_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    patient = Patient.query.get(id)
    patient.delete()

    return redirect(url_for('patient.patients_list'))