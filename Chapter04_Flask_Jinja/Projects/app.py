from flask import Flask, render_template

app = Flask(__name__)

class Product():
    def __init__(self, name, price, img):
        self.name = name
        self.price = price
        self.img = img

piano1 = Product("ელექტრო პიანინო CASIO AP-270BNC2", "10,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano2 = Product("ელექტრო პიანინო CASIO AP-270BNC2", "5,000.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano3 = Product("ელექტრო პიანინო CASIO AP-270BNC2", "4,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")
piano4 = Product("ელექტრო პიანინო CASIO AP-270BNC2", "6,099.00", "https://musicroom.ge/wp-content/uploads/2025/09/s-l1600-3.jpg")

pianos = [piano1, piano2, piano3, piano4, piano1, piano2, piano3, piano4]

@app.route('/gza')
def index():
    return render_template("index.html", title='პროდუქტები', products=pianos)

@app.route('/products')
def products():
    return render_template('products.html', products=pianos)

@app.route('/products/<int:id>')
def product(id):
    return render_template('produc.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/register')
def register():
    return render_template('register.html')


app.run(debug=True)