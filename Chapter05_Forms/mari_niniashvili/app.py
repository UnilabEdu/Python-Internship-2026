from flask import Flask,render_template,url_for,request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed, FileSize
from wtforms.fields import StringField, PasswordField,SelectField,BooleanField, SubmitField, DecimalField,IntegerField
from wtforms.validators import DataRequired, EqualTo,Length,ValidationError
from string import ascii_lowercase, ascii_uppercase,digits,punctuation
from wtforms import TextAreaField
import os


app=Flask(__name__)
app.config["SECRET_KEY"] = "asd1d2g3d;IOISie0w09"

class Product():
    def __init__(self, id, name, price, img):
        self.id = id  
        self.name = name
        self.price = price
        self.img = img

class SaveOrder:
    def __init__(self,user_name,id_name,country,address,zip_code,category,name,price):
       self.user_name=user_name
       self.id_name=id_name
       self.country=country
       self.address=address
       self.zip_code=zip_code
       self.category = category
       self.name = name
       self.price = price
orders = []

class OrderProduct(FlaskForm):
    user_name = StringField("ორგანიზაციის სახელი", validators=[DataRequired()])
    id_name=IntegerField("საიდენტიფიკაციო კოდი", validators=[DataRequired()])
    country = SelectField("აირჩიე ქვეყანა",choices=[("GE", "საქართველო"), ("FR", "საფრანგეთი"), ("IT", "იტალია")],validators =[DataRequired()])
    address = TextAreaField("მისამართი")
    zip_code = IntegerField("შეიყვანეთ საფოსტო ინდექსი", validators=[DataRequired()])
    category = SelectField("აირჩიეთ კატეგორია",choices=['პიანინო','როიალი','დრამი'],validators=[DataRequired()])
    name = StringField("რა პროდუქტი გსურთ? ", validators=[DataRequired()])
    price = DecimalField("ჩაწერეთ ნაქსიმალური ფასი",validators=[DataRequired()])
    headphones = BooleanField("ყურსასმენი")
    wifi=BooleanField("Wi-Fi")
    submit = SubmitField("დამატება")


class ProductForm(FlaskForm):
    name = StringField("პროდუქტის სახელი", validators=[DataRequired()])
    price = DecimalField("პროდუქტის ფასი",validators=[DataRequired()])
    category = SelectField("კატეგორიის სახელი",choices=['პიანინო','როიალი','ციფრული'],validators=[DataRequired()])
    img = FileField("დაამატე სურათი", validators=[DataRequired(),FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField("დამატება")

class RegisterForm(FlaskForm):
    name = StringField("სახელი და გვარი",validators =[DataRequired()] )
    password1 = PasswordField("პაროლი",validators =[DataRequired(),Length(min=4,max=10)] )
    password2 = PasswordField("გაიმეორე პაროლი",validators =[DataRequired(),EqualTo("password1", message="პაროლები უნდა ეთვეოდეს")] )
    countries = SelectField("აირჩიე ქვეყანა",choices=[("GE", "საქართველო"), ("DE", "გერმანია"), ("IT", "იტალია")],validators =[DataRequired()])
    remember_me = BooleanField("დამიმახსოვრე")
    submit = SubmitField("რეგისტრაცია")

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

       


piano0 = Product(0, "ელექტრო პიანინო Piano AP-17", "₾2,111.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano1 = Product(1, "ელექტრო პიანინო CASIO AP-270BNC2", "₾7,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano2 = Product(2, "ელექტრო პიანინო sonate MH-178 white MAT digital piano", "₾1,399", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano3 = Product(3, "ელექტრო პიანინო YAMAHA YDP-165R", "₾4,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano4 = Product(4, "ელექტრო პიანინო SONATE MPH-188 BEAGE digital piano", "₾3,259.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano5 = Product(5, "ელექტრო პიანინო CASIO AP-270BNC2", "₾1,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano6 = Product(6, "ელექტრო პიანინო sonate MH-178 white MAT digital piano", "₾1,900", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano7 = Product(7, "ელექტრო პიანინო YAMAHA YDP-165R", "₾1,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano8 = Product(8, "ელექტრო პიანინო SONATE MPH-188 BEAGE digital piano", "₾4,259.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
pianos = [piano0,piano1,piano2,piano3,piano4,piano5,piano6,piano7, piano8]


@app.route("/")
def index():
    return render_template("index.html",title = "    this is a demo version",  products = pianos, count = len(pianos))

@app.route("/products")
def products():
     return render_template("products.html",products=pianos)

@app.route("/products/<int:id>")
def product(id):
    return render_template("product.html",piano = pianos[id])

@app.route("/create",methods=["GET","POST"])
def create():
    form =ProductForm()
    if form.validate_on_submit():
        img=form.img.data
        UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'static', 'uploads', img.filename)
        img.save(UPLOAD_PATH)
        pianos.append(Product(10, form.name.data, form.price.data, f"/static/uploads/{img.filename}"))
        return "პროდუქტი დამატებულია"
    if form.is_submitted():
        print("ფორმის შეცდომები:", form.errors)  

    return render_template("create.html", form=form)

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return "წარმატებით გაიგზავნა!"
    else:
        print(form.errors)
    return render_template("register.html",form=form)

@app.route('/ordering',methods=["GET","POST"])
def ordering():
    form = OrderProduct()
    if form.validate_on_submit():
        my_order=SaveOrder(
            user_name=form.user_name.data,
            id_name=form.id_name.data,
            country=form.country.data,
            address=form.address.data,
            zip_code=form.zip_code.data,
            category=form.category.data,
            name=form.name.data,
            price=form.price.data   )
        orders.append(my_order)
        return "თქვენი შეკვეთა გაგზავნილია"
    else:
        print (form.errors)
    
    return render_template("ordering.html",form=form)


if __name__=="__main__":
    app.run(debug = True,port=5001)