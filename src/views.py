from flask import render_template, session, request, redirect, url_for
from flask_login import current_user, login_required
from src import app, db

from src.manufacturers.models import Manufacturer
from src.manufacturers.products.models import Model, Equipment
from src.auth.forms import EquipmentAddForm


@app.route("/")
def index():
    return render_template("index.html", modelsExist=Model.query.count() > 0, form=EquipmentAddForm())


@app.route("/auth/addEq", methods=["POST"])
@login_required
def equipment_add():
    form = EquipmentAddForm(request.form)
    if not form.validate():
        return render_template("index.html", form=form)

    eqpm = Equipment(form.serialnumber.data)
    eqpm.model = form.model.data

    eqpm.person_id = current_user.id

    db.session().add(eqpm)
    db.session().commit()

    return redirect(url_for("index"))


@app.route("/auth/removeEq/<int:id>", methods=["POST"])
@login_required
def equipment_delete(id):
    eqpm = Equipment.query.filter_by(id=id).first()

    db.session().delete(eqpm)
    db.session().commit()

    return redirect(url_for("index"))
