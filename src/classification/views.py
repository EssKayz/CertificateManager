from src import app, db

from flask import redirect, render_template, request, url_for
from flask_login import login_required

from src.classification.models import Classification
from src.classification.forms import ClassificationForm, EquipmentAddForm
from src.manufacturers.products.models import Product

import string

@app.route("/classifications", methods=["GET"])
def classifications_index():
    return render_template("classifications/list.html",
                           classifications=Classification.query.all(),
                           form=ClassificationForm(), addForm=EquipmentAddForm(), productsExist=Product.query.count() > 0)


@app.route("/classifications/new/")
@login_required
def classifications_form():
    return render_template("classifications/new.html", form=ClassificationForm())


@app.route("/classifications/", methods=["POST"])
@login_required
def classifications_create():
    form = ClassificationForm(request.form)
    if not form.validate():
        return render_template("classifications/list.html", form=form, addForm=EquipmentAddForm(), classifications=Classification.query.all(), productsExist=Product.query.count() > 0)

    t = Classification(form.name.data)
    t.description = form.description.data
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("classifications_index"))


@app.route("/classifications/add/<class_id>", methods=["POST"])
# @login_required
def classifications_link(class_id):
    form = EquipmentAddForm(request.form)
    if not form.validate():
        return redirect(url_for("classifications_index"))

    classif = Classification.query.get(class_id)
    data = form.model.data
    product = Product.query.filter(Product.name==str(data)).first()

    print('-------')
    print(product)
    print('-------')

    classif.add_product(product)
    db.session.commit()
    return redirect(url_for("classifications_index"))
