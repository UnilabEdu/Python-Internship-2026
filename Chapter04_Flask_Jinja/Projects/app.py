from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/products')
def products():
    return '<h1>This are my products</h1>'

@app.route('/products/<int:id>')
def product(id):
    return f'<h1>This is product {id}</h1>'

@app.route('/products/<float:currency>')
def example(currency):
    return f'<h1>your total is: {currency} euro</h1>'

@app.route('/youtube/<path:link>')
def example2(link):
    return f'<h1>this is your {link}</h1>'

app.run(debug=True)