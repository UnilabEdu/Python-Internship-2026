from flask import Blueprint,render_template,redirect,url_for, flash
from src.views.auth.forms import RegisterForm

auth_bp=Blueprint('auth',__name__)
clinic_stuff = []

@auth_bp.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_stuff={
            "name": form.name.data }
        clinic_stuff.append(new_stuff)

        flash("პერსონალი დარეგისტრირებულია")
        return redirect(url_for("auth.users_list"))
    
    else:
        print(form.errors)
    return render_template("auth/register.html",form=form)

@auth_bp.route("/users",methods=["GET","POST"])
def users_list():
    return render_template("auth/users_list.html",stuff=clinic_stuff)


