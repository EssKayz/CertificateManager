from flask import render_template, session, request, redirect, url_for
from flask_login import current_user, login_required
from src import app, db

from src.products.models import Product
from src.equipment.forms import EquipmentAddForm


@app.route("/")
def index():
    return render_template("index.html", modelsExist=Product.query.count() > 0, form=EquipmentAddForm())