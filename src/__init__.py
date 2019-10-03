from flask_login import LoginManager
from os import urandom
from src.auth.models import User
from src.auth import views
from src.auth import models
from src.manufacturers.products import models
from src.manufacturers import models
from src.manufacturers.products import views
from src.manufacturers import views
from src import views
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask
app = Flask(__name__)

bcrypt = Bcrypt(app)

# Import sqlalchemy

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# Import views

# Import database models

# Import user auth

# Logins
app.config["SECRET_KEY"] = urandom(32)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


db.create_all()
