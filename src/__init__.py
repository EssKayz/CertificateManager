from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)

#Import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_ECHO"] = True
    
db = SQLAlchemy(app)

#Import views
from src import views
from src.manufacturers import views
from src.products import views
from src.classification import views
from src.equipment import views

#Import database models
from src.manufacturers import models
from src.products import models
from src.classification import models
from src.equipment import models

#Import user auth
from src.auth import models
from src.auth import views


#Logins
from src.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)
 
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


db.create_all()

