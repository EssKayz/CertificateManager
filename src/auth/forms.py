from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from src import db
from src.auth.models import User
from src.manufacturers.models import Manufacturer
from src.manufacturers.products.models import Product, Equipment

import sys


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class UserCreateForm(FlaskForm):
    name = StringField("name", [validators.Length(
        min=3, max=48, message="Name length invalid")])
    username = StringField("username", [validators.Length(
        min=4, max=24, message="username length invalid")])
    password = PasswordField(
        "password", [validators.Length(min=4, message="password too short")])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    class Meta:
        csrf = False


class EquipmentAddForm(FlaskForm):
    model = QuerySelectField(label="Model",
                             get_label='name',
                             query_factory=lambda: Product.query.all(),
                             blank_text=u'Select a model...'
                             )
    serialnumber = StringField("Serial Number")

    def validate_serialnumber(self, serialnumber):
        serialnumber = Equipment.query.filter_by(
            serialnumber=serialnumber.data).first()
        if serialnumber is not None:
            raise ValidationError('Serialnumber already used')

    class Meta:
        csrf = False
