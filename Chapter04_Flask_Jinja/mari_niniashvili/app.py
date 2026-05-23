from flask import Flask,render_template,url_for,request


app =Flask(__name__)

class Product():
    def __init__(self,id,name,price, img):
        self.id = id
        self.name = name
        self.price = price
        self.img = img
piano1 = Product(0,"ელექტრო პიანინო CASIO AP-270BNC2","₾7,099.00","https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg" )
piano2 = Product(1,"ელექტრო პიანინო sonate MH-178 white MAT digital piano", "₾1,399", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano3 = Product(2,"ელექტრო პიანინო YAMAHA YDP-165R","₾4,099.00","https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg" )
piano4 = Product(3,"ელექტრო პიანინო SONATE MPH-188 BEAGE digital piano","₾3,259.00","https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg" )
piano5 = Product(4,"ელექტრო პიანინო CASIO AP-270BNC2","₾1,099.00","https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg" )
piano6 = Product(5,"ელექტრო პიანინო sonate MH-178 white MAT digital piano", "₾1,900", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano7 = Product(6,"ელექტრო პიანინო YAMAHA YDP-165R","₾1,099.00","https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg" )
piano8 = Product(7,"ელექტრო პიანინო SONATE MPH-188 BEAGE digital piano","₾4,259.00","https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg" )

pianos = [piano1,piano2,piano3,piano4,piano5,piano6,piano7, piano8]


@app.route("/")
def index():
    return render_template("index.html",title = "    this is a demo version",  products = pianos, count = len(pianos))

@app.route("/products")
def products():
     return render_template("products.html",products=pianos)

@app.route("/products/<int:id>")
def product(id):
    return render_template("product.html",id=id)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/register")
def register():
    return render_template("register.html")


app.run(debug = True,port = 5001)