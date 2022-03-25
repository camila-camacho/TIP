
from app import app ,dash

from flask import render_template


# dash imports
dash.create_dash_application(app)

@app.route("/")
def home():
    return render_template("public/home.html")

@app.route("/login")
def login():
    return render_template("public/templates/login.html")

@app.route("/raised")
def raised():
    return render_template("public/raised.html")

@app.route("/backlog")
def backlog():
    return render_template("public/backlog.html")

@app.route("/closed")
def closed():
    return render_template("public/closed.html")

@app.route("/admin/dashboard")
def index():
    return render_template("public/index.html")











