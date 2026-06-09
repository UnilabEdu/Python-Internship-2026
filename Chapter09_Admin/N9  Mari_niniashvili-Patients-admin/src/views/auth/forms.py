from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms .fields import StringField,SelectField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length,EqualTo,ValidationError
from src.models.user import User



class RegisterForm(FlaskForm):
    name = StringField("სახელი და გვარი",validators =[DataRequired()] )
    password1 = PasswordField("პაროლი",validators =[DataRequired(),Length(min=4,max=10)] )
    password2 = PasswordField("გაიმეორე პაროლი",validators =[DataRequired(),EqualTo("password1", message="პაროლები უნდა ეთხვეოდეს")] )
    countries = SelectField("აირჩიე ქალაქი",choices=[("GE", "საქართველო"), ("DE", "გერმანია"), ("IT", "იტალია")],validators =[DataRequired()])
    remember_me = BooleanField("დამიმახსოვრე")
    submit = SubmitField("რეგისტრაცია")


class LoginForm(FlaskForm):
    name = StringField("სახელი და გვარი",validators =[DataRequired()] )
    password1 = PasswordField("პაროლი",validators =[DataRequired()] )
    submit = SubmitField("შესვლა")

    def validate_name(self,field):
        user = User.query.filter_by(name=field.data).first() 

        if not user:
            raise ValueError('არასწორი სახელი ან პაროლი')
        
    def validate_password(self,field):
        user = User.query.filter_by(name=self.name.data).first() 

        if  user or not check_password_hash(user.password,field.data):
            raise ValidationError('არასწორი სახელი ან პაროლი')