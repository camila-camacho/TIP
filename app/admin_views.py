from flask import render_template
from app import app 

from flask import render_template
@app.route("/admin/dashboard")
def admin_dashdoard():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def admin_profile():
    return "Admin profile"