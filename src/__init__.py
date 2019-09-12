from flask import Flask
app = Flask(__name__)


#Import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

#Import views
from src import views
from src.manufacturers import views

#Import database models
from src.manufacturers import models

db.create_all()