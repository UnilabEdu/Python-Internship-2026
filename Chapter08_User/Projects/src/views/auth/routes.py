from flask import render_template, Blueprint, redirect, url_for, request
from flask_login import login_user, logout_user

from src.views.auth.forms import RegisterForm, LoginForm
from src.models import User
from src.views.auth.forms import RegisterForm, LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(name=form.name.data, password=form.password.data)

        user.create()

        return redirect(url_for('auth.login'))
    else:
        print(form.errors)

    return render_template('auth/register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        login_user(user)

        if request.args.get('next'):
            return redirect(request.args.get('next'))

        return redirect(url_for('main.index'))

    else:
        print(form.errors)

    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))