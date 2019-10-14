from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from src import db
from src.auth.models import User
import sys


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")


class UserCreateForm(FlaskForm):
    name = StringField("name", [
        validators.Length(
            min=3, max=48, message="Name length invalid"),  DataRequired()]
    )
    username = StringField("username", [validators.Length(
        min=4, max=24, message="username length invalid"),  DataRequired()])
    password = PasswordField(
        "password", [validators.Length(min=4, message="password too short")])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
