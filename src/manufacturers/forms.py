from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ManufacturerForm(FlaskForm):
    name = StringField("Manufacturer name", [validators.Length(min= 2)])
 
    class Meta:
        csrf = False