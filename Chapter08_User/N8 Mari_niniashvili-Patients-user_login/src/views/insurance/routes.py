
from flask import Blueprint,render_template,url_for,redirect,request
from src.config import Config
from src.ext import db
from src.models.insurance_comp import Insurance
from src.views.insurance.forms import InsuranceForm
from wtforms.validators import DataRequired
from flask_login import login_required


insurance=Blueprint('insurance',__name__)

@insurance.route("/insurances")
def insurance_list():
    all_insurances=Insurance.query.all()
    return render_template("insurance/insurances.html",
                            title="სადაზღვევო კომპანიები",
                            insurances_list=all_insurances)

@insurance.route("/insurance",methods=["GET","POST"])
@login_required
def get_insurance():
    form = InsuranceForm()
    if form.validate_on_submit():
        company_name = form.company_name.data
        id_number = form.id_number.data
        city = form.city.data
        address = form.address.data

        new_company=Insurance(
            insurance=company_name,
            id_number= id_number,
            city=city,
            address=address
        )
  
        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for('insurance.insurance_list'))
    return render_template("insurance/insurance.html",form=form)


