from app import db

class Book(db.Model):
    isbn = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.String(120), index=True)
    author = db.Column(db.String(120), index=True, unique=True)
    year = db.Column(db.Integer)
    book_review = db.relationship('Review', backref='book_review', lazy='dynamic')

    def __repr__(self):
        return '<Book {}>'.format(self.title)