
from app import app ,dash

from flask import render_template

from flask import request, session, redirect, url_for

app.config['SECRET_KEY']='JSANDCNDJCNDJCDSJCSD'

# dash imports
dash.create_dash_application(app)

@app.route("/")
def home():
    return render_template("public/home.html")

@app.route("/login", methods=[ "GET","POST"])
def login():
    if request.method == "GET":
        return render_template("public/templates/login.html")
    else:
        username=request.form["username"]
        password=request.form["password"]
    
        if username == "araceli" and password =="tip":
            session["araceli"] = username
            session["tip"] = password
            return redirect(url_for("index"))
        else:
            return render_template("public/templates/login.html")
            


@app.route("/raised")
def raised():
    return render_template("public/raised.html")

@app.route("/backlog")
def backlog():
    return render_template("public/backlog.html")

@app.route("/close")
def closed():
    return render_template("public/close.html")

@app.route("/admin/dashboard")
def index():
    return render_template("public/index.html")











