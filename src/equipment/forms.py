from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
from wtforms.validators import  DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from src.products.models import Product
from src.equipment.models import Equipment

from src import db

class EquipmentAddForm(FlaskForm):
    model = QuerySelectField(label="Model",
                             get_label='name',
                             query_factory=lambda: Product.query.all(),
                             blank_text=u'Select a model...'
                             )
    serialnumber = StringField("Serial Number",  [ DataRequired() ])

    def validate_serialnumber(self, serialnumber):
        serialnumber = Equipment.query.filter_by(
            serialnumber=serialnumber.data).first()
        if serialnumber is not None:
            raise ValidationError('Serialnumber already used')
