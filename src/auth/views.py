from flask import render_template, request, redirect, url_for
from flask_login import login_user

from src import app, db
from src.auth.models import User
from src.auth.forms import LoginForm, UserCreateForm

from flask_login import login_user, logout_user


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/users/new/")
def auth_form():
    return render_template("auth/new.html", form=UserCreateForm())


@app.route("/users/", methods=["POST"])
def auth_create():
    form = UserCreateForm(request.form)
    if form.validate_on_submit():
        t = User(form.name.data, form.username.data, form.password.data)
        db.session().add(t)
        db.session().commit()
        return redirect(url_for("manufacturers_index"))
    return render_template('auth/new.html', form=form)
