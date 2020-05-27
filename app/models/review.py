from datetime import datetime
from app import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    isbn = db.Column(db.String, db.ForeignKey('book.isbn'), index=True)
    review = db.Column(db.String(240))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<UID, Review {}{}>'.format(self.uid, self.review)