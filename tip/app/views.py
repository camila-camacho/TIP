
from app import app 

from flask import render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Lenght, Email 

class LoginForm(FlaskForm):
    email = StringField("email", validators=[Email()])
    password = PasswordField()("password", validators = [Lenght(min=5)])

class SignUp(FlaskForm):
    user = StringField("user")
    email = StringField("email", validators=[Email()])
    password = PasswordField()("password", validators = [Lenght(min=5)])

    
    
    
@app.route("/")
def home():
    return render_template("public/home.html")

@app.route("/login")
def login():
    return render_template("public/templates/login.html")

@app.route("/raised")
def raised():
    return render_template("public/raised.html")

@app.route("/admin/dashboard")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "<h1 style='color:red'>About!!!!'</h1>"