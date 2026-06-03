from flask_wtf import FlaskForm
from wtforms .fields import StringField,SelectField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length,EqualTo




class RegisterForm(FlaskForm):
    name = StringField("სახელი და გვარი",validators =[DataRequired()] )
    password1 = PasswordField("პაროლი",validators =[DataRequired(),Length(min=4,max=10)] )
    password2 = PasswordField("გაიმეორე პაროლი",validators =[DataRequired(),EqualTo("password1", message="პაროლები უნდა ეთხვეოდეს")] )
    countries = SelectField("აირჩიე ქვეყანა",choices=[("GE", "საქართველო"), ("DE", "გერმანია"), ("IT", "იტალია")],validators =[DataRequired()])
    remember_me = BooleanField("დამიმახსოვრე")
    submit = SubmitField("რეგისტრაცია")