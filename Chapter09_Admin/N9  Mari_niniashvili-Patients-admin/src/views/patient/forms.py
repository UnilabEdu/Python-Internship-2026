from flask_wtf import FlaskForm
from wtforms .fields import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from flask_wtf.file import FileField,FileAllowed
from string import ascii_lowercase,ascii_uppercase,punctuation,digits


class PatientForm(FlaskForm):
    name = StringField("პაციენტის სახელი", validators=[DataRequired()])
    id_number = StringField("პირადი ნომერი", validators=[DataRequired()])
    age = IntegerField("ასაკი", validators=[DataRequired()])
    city = StringField("ქალაქი",validators=[DataRequired()])
    gender = SelectField("სქესი",choices=[("male", "მამრობითი"), ("female", "მდედრობითი")],validators=[DataRequired()])
    img = FileField("დაამატე სურათი", validators=[DataRequired(),FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField("დამატება")



    def validate_password1(self,field):
        has_lower=False
        has_upper=False
        has_digit=False
        has_punctuations=False

        for char in field.data:
            if char in ascii_lowercase:
                has_lower=True
            if char in ascii_uppercase:
                has_upper=True
            if char in digits:
                has_digit=True
            if char in punctuation:
                has_punctuations=True
        

        if not has_lower:
            raise ValidationError("შეიტანეთ პატარა ასოები")
        if not has_upper:
            raise ValidationError("შეიტანეთ დიდი ასოები")
        if not has_digit:
            raise ValidationError("შეიტანეთ ციფრები")
        if not has_punctuations:
            raise ValidationError("შეიტანეთ პუნქტუაციის ნიშნები")
