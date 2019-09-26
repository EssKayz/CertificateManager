from src import db

from sqlalchemy.sql import text


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    models = db.relationship('Model', backref='manufacturer', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    @staticmethod
    def listByModel():
        stmt = text("SELECT Manufacturer.id, COUNT(Model.name) as count, Manufacturer.name FROM Manufacturer "
                    " LEFT JOIN Model ON Manufacturer.id = Model.manufacturer_id"
                    " GROUP BY Manufacturer.name ORDER BY count DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "count": row[1], "name": row[2]})

        return response
