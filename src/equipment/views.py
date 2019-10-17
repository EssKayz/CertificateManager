from src import app, db

from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from src.products.models import Product
from src.equipment.models import Equipment
from src.equipment.forms import EquipmentAddForm

@app.route("/auth/addEq", methods=["POST"])
@login_required
def equipment_add():
    form = EquipmentAddForm(request.form)
    if not form.validate():
        return render_template("index.html", form=form, modelsExist=Product.query.count() > 0)

    eqpm = Equipment(form.serialnumber.data)
    eqpm.model = form.model.data
    eqpm.isbroken = False

    eqpm.person_id = current_user.id

    db.session().add(eqpm)
    db.session().commit()

    return redirect(url_for("index"))


@app.route("/auth/removeEq/<int:id>", methods=["POST"])
@login_required
def equipment_delete(id):
    eqpm = Equipment.query.filter_by(id=id).first()
    if eqpm in current_user.get_equipment():
        db.session().delete(eqpm)
        db.session().commit()

    return redirect(url_for("index"))

@app.route("/auth/break/<int:id>", methods=["POST"])
@login_required
def equipment_break(id):
    eqpm = Equipment.query.filter_by(id=id).first()
    if eqpm in current_user.get_equipment():
        eqpm.isbroken = not eqpm.isbroken
        db.session().commit()

    return redirect(url_for("index"))
