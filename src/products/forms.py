from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
from wtforms.validators import  DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from src.manufacturers.models import Manufacturer
from src.products.models import Product

from src import db


class ModelForm(FlaskForm):
    name = StringField("Model name", [validators.Length(
        min=2, max=24, message="Model name length invalid"),  DataRequired()])
    manufacturer = QuerySelectField(label="Manufacturer",
                                    get_label='name',
                                    query_factory=lambda: Manufacturer.query.all(),
                                    blank_text=u'Select a manufacturer...'
                                    )

    def validate_name(self, name):
        name = Product.query.filter_by(
            name=name.data).first()
        if name is not None:
            raise ValidationError('Model name already used')
