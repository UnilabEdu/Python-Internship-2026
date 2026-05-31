from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from werkzeug.security import check_password_hash

from src.models import User

class RegisterForm(FlaskForm):
    name = StringField('სახელი და გვარი', validators=[DataRequired()])
    password = PasswordField('პაროლი',  validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('გაიმეორე პაროლი',  validators=[DataRequired(), EqualTo("password", message="პაროლები უნდა უდრიდეს ერთმანეთს")])
    countre = SelectField('ქვეყანა', choices=[("GE", "საქართველო"), ("GER",'გერმანია'), ("IT", 'იტალია')], validators=[DataRequired()])
    remember_me = BooleanField('დამიმახსოვრე', validators=[DataRequired()])
    submit = SubmitField('რეგისტრაცია', validators=[DataRequired()])

class LoginForm(FlaskForm):
    name = StringField('სახელი და გვარი', validators=[DataRequired()])
    password = PasswordField('პაროლი',  validators=[DataRequired()])
    submit = SubmitField('შესვლა', validators=[DataRequired()])

    def validate_name(self, field):
        user = User.query.filter_by(name=field.data).first()

        if not user:
            raise ValidationError('სახელი ან პაროლი არასწორია')

    def validate_password(self, field):
        user = User.query.filter_by(name=self.name.data).first()

        if not user or not check_password_hash(user.password, field.data):
            raise ValidationError('სახელი ან პაროლი არასწორია')