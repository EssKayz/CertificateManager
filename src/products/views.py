from src import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from src.manufacturers.models import Manufacturer
from src.products.models import Product
from src.products.forms import ModelForm


@app.route("/models", methods=["GET"])
def models_index():
    return render_template("models/list.html", models=Product.query.all(), form=ModelForm(),
                           manufExists=Manufacturer.query.count() > 0, listeroo=Product.listByBrokenPercent() )


@app.route("/models/new/")
@login_required
def models_form():
    if Manufacturer.query.count() == 0:
        return redirect(url_for('manufacturers_index'))

    return render_template("models/new.html", form=ModelForm())


@app.route("/models/<model_id>/", methods=["POST"])
@login_required
def model_setEol(model_id):
    m = Product.query.get(model_id)

    if m.eol:
        m.eol = False
    else:
        m.eol = True
    db.session().commit()

    return redirect(url_for("models_index"))


@app.route("/models/", methods=["POST"])
@login_required
def models_create():
    form = ModelForm(request.form)

    if not form.validate():
        return render_template("models/list.html", form=form, models=Product.query.all(), manufExists=Manufacturer.query.count() > 0, listeroo=Product.listByBrokenPercent())

    t = Product(form.name.data)
    t.manufacturer = form.manufacturer.data
    t.eol = False

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("models_index"))
