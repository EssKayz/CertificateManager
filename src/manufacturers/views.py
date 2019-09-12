from src import app, db
from flask import redirect, render_template, request, url_for
from src.manufacturers.models import Manufacturer

@app.route("/manufacturers", methods=["GET"])
def manufacturers_index():
    return render_template("manufacturers/list.html", manufacturers = Manufacturer.query.all())
	
@app.route("/manufacturers/new/")
def manufacturers_form():
    return render_template("manufacturers/new.html")

@app.route("/manufacturers/", methods=["POST"])
def manufacturers_create():
    t = Manufacturer(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("manufacturers_index"))