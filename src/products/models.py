from src import db
from src.classification.models import ClassificationProduct

from sqlalchemy.sql import text


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'),
                                nullable=False)
    eol = db.Column(db.Boolean, nullable=False)

    classifications = db.relationship(
        "Classification",
        secondary=ClassificationProduct,
        backref=db.backref("Product", lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, name):
        self.name = name
        self.eol = False

    def __repr__(self):
        return self.name

    @staticmethod
    def listByBrokenPercent():
        stmt = text("SELECT product.id, product.name, "
                    " 100.0 * (SELECT COUNT(*) FROM equipment WHERE equipment.model_id = product.id AND equipment.isbroken) / "
                    "(SELECT COUNT(*) FROM equipment WHERE equipment.model_id = product.id) as brokenAvg "
                    "FROM product WHERE brokenAvg not NULL GROUP BY product.id ORDER BY brokenAvg asc LIMIT 10"
                    )

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(
                {"id": row[0], "name": row[1], "brokenAvg": row[2]})
        return response


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
