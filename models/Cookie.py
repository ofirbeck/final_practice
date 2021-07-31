from db import db

class CookieModel(db.Model):
    __tablename__ = "cookies"
    id = db.Column(db.integer, primary_key = True)
    flavor = db.Column(db.string(50))
    price = db.Column(db.Float(precision=2))
    box_id = db.Column(db.Integer, db.ForeignKey('box.id'))
    box = db.relationship('BoxModel')
    def __init__(self, flavor: str, price: float, box_id: int):
        self.flavor = flavor
        self.price = price
        self.box_id = box_id
    def json(self):
        return {'flavor': self.flavor, 'price': self.price, 'box_id': self.box_id}
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        

