from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from src.manufacturers.models import Manufacturer

from src import db


class ModelForm(FlaskForm):
    name = StringField("Model name", [validators.Length(min=2)])
    manufacturer = QuerySelectField(label="Manufacturer", 
                                    get_label='name' , 
                                    query_factory=lambda: Manufacturer.query.all(),
                                    blank_text=u'Select a manufacturer...'
                                    )

    class Meta:
        csrf=False
