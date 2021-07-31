from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.integer, primary_key = True)
    username = db.Column(db.string(50))
    password = db.Column(db.string(50))
    def __init__(self, username: str , password: str):
        self.username = username
        self.password = password
    @classmethod
    def find_by_username(cls, username: str):
        return cls.query.filter_by(username = username)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()