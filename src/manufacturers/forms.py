from flask_wtf import FlaskForm
from wtforms import StringField, validators


class ManufacturerForm(FlaskForm):
    name = StringField("Manufacturer name", [validators.Length(
        min=2, max=24, message="Name length invalid")])

    def validate_name(self, name):
        name = Manufacturer.query.filter_by(
            name=name.data).first()
        if name is not None:
            raise ValidationError('Manufacturer name already used')

    class Meta:
        csrf = False
