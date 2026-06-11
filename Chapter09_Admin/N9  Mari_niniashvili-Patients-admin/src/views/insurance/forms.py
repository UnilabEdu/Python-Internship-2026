

from flask_wtf import FlaskForm
from wtforms .fields import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from flask_wtf.file import FileField,FileAllowed
from string import ascii_lowercase,ascii_uppercase,punctuation,digits


class InsuranceForm(FlaskForm):
    company_name = StringField("სადაზღვევო კომპანიის სახელი", validators=[DataRequired()])
    id_number = StringField("საიდენტიფიკაციო ნომერი", validators=[DataRequired()])
    city = StringField("ქალაქი",validators=[DataRequired()])
    address = StringField("მისამართი",validators=[DataRequired()])
    submit = SubmitField("დამატება")

