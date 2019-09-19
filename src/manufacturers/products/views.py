from src import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from src.manufacturers.products.models import Model
from src.manufacturers.products.forms import ModelForm

@app.route("/models", methods=["GET"])
def models_index():
    return render_template("models/list.html", models = Model.query.all())
	
@app.route("/models/new/")
@login_required
def models_form():
    return render_template("models/new.html", form = ModelForm())

@app.route("/models/", methods=["POST"])
@login_required
def models_create():
    form = ModelForm(request.form)
    
    if not form.validate():
        return render_template(url_for('models_form'), form = form)
    
    t = Model(form.name.data)    
    t.manufacturer = form.manufacturer.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("models_index"))