from src import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from src.manufacturers.models import Manufacturer
from src.manufacturers.forms import ManufacturerForm

@app.route("/manufacturers", methods=["GET"])
def manufacturers_index():
    return render_template("manufacturers/list.html", 
                           manufacturers = Manufacturer.query.all(), 
                           listeroo=Manufacturer.listByModel(), form=ManufacturerForm())
	
@app.route("/manufacturers/new/")
@login_required
def manufacturers_form():
    return render_template("manufacturers/new.html", form = ManufacturerForm())

@app.route("/manufacturers/", methods=["POST"])
@login_required
def manufacturers_create():
    form = ManufacturerForm(request.form)
    if not form.validate():
        return render_template(url_for('manufacturers_form'), form = form)
    
    t = Manufacturer(request.form.get("name"))
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("manufacturers_index"))