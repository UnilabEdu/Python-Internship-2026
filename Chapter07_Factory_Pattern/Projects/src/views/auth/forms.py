from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):
    name = StringField('სახელი და გვარი', validators=[DataRequired()])
    password = PasswordField('პაროლი',  validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('გაიმეორე პაროლი',  validators=[DataRequired(), EqualTo("password", message="პაროლები უნდა უდრიდეს ერთმანეთს")])
    countre = SelectField('ქვეყანა', choices=[("GE", "საქართველო"), ("GER",'გერმანია'), ("IT", 'იტალია')], validators=[DataRequired()])
    remember_me = BooleanField('დამიმახსოვრე', validators=[DataRequired()])
    submit = SubmitField('რეგისტრაცია', validators=[DataRequired()])