from db import db

class BoxModel(db.Model):
    id = db.Column(db.integer, primary_key = True)
    width = db.Column(db.float(precision=2))
    height = db.Column(db.float(precision=2))
    cookies = db.relationship('CookieModel', lazy = 'dynamic')
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width
    def json(self):
        return {'height': self.height, 'width': self.width, 'cookies': [cookie.json() for cookie in self.cookies.all()]}
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id)
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()