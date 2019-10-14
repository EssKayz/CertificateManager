import os
from src import db

from sqlalchemy.sql import text


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = "equipment"
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    model_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)
    serialnumber = db.Column(db.String(134))

    isbroken = db.Column(db.Boolean, nullable=False)
    model = db.relationship("Product")

    def __init__(self, snum):
        self.serialnumber = snum

    def get_id(self):
        return self.id
