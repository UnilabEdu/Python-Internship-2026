from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    name = StringField('Name and Surname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo("password",
                                                                                     message="Passwords must be equal to each other")])
    countries = SelectField('Country', choices=[("GE", "Georgia"), ("GER", 'Germany'), ("IT", 'Italy')],
                            validators=[DataRequired()])
    remember_me = BooleanField('Remember me', validators=[DataRequired()])
    submit = SubmitField('Register', validators=[DataRequired()])


