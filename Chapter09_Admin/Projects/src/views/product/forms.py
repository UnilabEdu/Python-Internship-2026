from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms.fields import StringField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

class ProductForm(FlaskForm):
    name = StringField('პროდუქტის სახელი', validators=[DataRequired()])
    price = DecimalField('ფასი', validators=[DataRequired()])
    category = SelectField('კატეგორია', choices=[])
    img = FileField('ფოტო', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png']), FileSize(max_size=1024*1024*10)])
    submit = SubmitField('დამატება')

    def validate_password(self, field):
        has_lower = False
        has_upper = False
        has_digit = False
        has_punctuation = False

        for char in field.data:
            if char in ascii_lowercase:
                has_lower = True
            if char in ascii_uppercase:
                has_upper = True
            if char in digits:
                has_digit = True
            if char in punctuation:
                has_punctuation = True

        if not has_lower:
            raise ValidationError('პაროლში საჭიროა პატარა ასოების გამოყენება')

        if not has_upper:
            raise ValidationError('პაროლში საჭიროა დიდი ასოების გამოყენება')

        if not has_digit:
            raise ValidationError('პაროლში საჭიროა რიცხვი')

        if not has_punctuation:
            raise ValidationError('პაროლში საჭიროა პუნქტუაციის გამოყენება')
