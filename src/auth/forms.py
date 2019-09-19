from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError

from src.auth.models import User


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class UserCreateForm(FlaskForm):
    name = StringField("name", [validators.Length(min=3)])
    username = StringField("username", [validators.Length(min=4)])
    password = PasswordField("password", [validators.Length(min=4)])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    class Meta:
        csrf = False
