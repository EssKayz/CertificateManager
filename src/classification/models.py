from src import db

from sqlalchemy.sql import text

ClassificationProduct = db.Table('ClassificationProduct',
                                 db.Column('classification_id', db.Integer,
                                           db.ForeignKey('Classification.id')),
                                 db.Column('product_id', db.Integer,
                                           db.ForeignKey('product.id'))
                                 )


class Classification(db.Model):
    __tablename__ = 'Classification'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    products = db.relationship(
        "Product",
        secondary=ClassificationProduct,
        backref=db.backref("Classification",lazy='dynamic'),
        lazy='dynamic'
        )

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        if not self.check_following_status(product):
            self.products.append(product)

    def check_following_status(self, product):
        return self.products.filter(ClassificationProduct.c.product_id == product.id).count() > 0

    def __repr__(self):
        return self.name
