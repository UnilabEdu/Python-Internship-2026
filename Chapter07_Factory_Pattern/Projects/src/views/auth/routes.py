from flask import render_template, Blueprint

from src.views.auth.forms import RegisterForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
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

    return render_template('auth/register.html', form=form)