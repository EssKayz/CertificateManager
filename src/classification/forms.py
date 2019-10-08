from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from src.classification.models import Classification
from src.manufacturers.products.models import Product


class ClassificationForm(FlaskForm):
    name = StringField("Name of classification", [validators.Length(
        min=2, max=24, message="Name length invalid")])

    description = StringField("Description of classification", [validators.Length(
        min=2, max=72, message="Description length invalid")])

    def validate_name(self, name):
        name = Classification.query.filter_by(
            name=name.data).first()
        if name is not None:
            raise ValidationError('Classification name already used')

    class Meta:
        csrf = False


class EquipmentAddForm(FlaskForm):
    model = QuerySelectField(label="Product",
                             get_label='name',
                             query_factory=lambda: Product.query.all(),
                             blank_text=u'Select a model...'
                             )

    def validate_duplicate(self, model):
        model = Classification.query.filter_by(
            model=model.data).first()
        if model is not None:
            raise ValidationError('Model already added')

    class Meta:
        csrf = False
