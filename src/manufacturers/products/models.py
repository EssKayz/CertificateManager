from src import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'),
                             nullable=False)
    eol = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.eol = False
    
    def __repr__(self):
                return self.name