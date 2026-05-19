
from flask import Flask, render_template,url_for,request
app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html")

@app.route("/about")
def about():
    return  render_template("about.html")

@app.route("/register_animal")
def register_animal():
    return  render_template("register_animal.html")


@app.route("/register_owner")
def register_owner():
    return  render_template("register_owner.html")


@app.route("/register")
def register():
    return  render_template("register.html")


@app.route("/questions")
def questions():
    return  render_template("questions.html")




app.run(debug=True)
