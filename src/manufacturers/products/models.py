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


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = "equipment"
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())
    
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    serialnumber = db.Column(db.String(134))
    
    
    model = db.relationship("Model")

    def __init__(self, snum):
        self.serialnumber = snum

    def get_id(self):
        return self.id
