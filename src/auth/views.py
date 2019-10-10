from flask import render_template, request, redirect, url_for
from flask_login import login_user

from src import app, db
from src.auth.models import User
from src.auth.forms import LoginForm, UserCreateForm

from flask_login import login_user, logout_user
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    #If GET request, redirect to the loginform
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    #Otherwise, proceed with logging in
    form = LoginForm(request.form)
    user = User.query.filter_by(
        username=form.username.data).first()
    #Check if user exists with name
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

    #If username exists, check if password exists
    if not bcrypt.check_password_hash(user.password, form.password.data):
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
        t = User(form.name.data, form.username.data,
                 bcrypt.generate_password_hash(form.password.data).decode('utf-8'))
        db.session().add(t)
        db.session().commit()
        return redirect(url_for("auth_login"))
    return render_template('auth/new.html', form=form)
