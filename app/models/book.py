from app import db
import csv

class Book(db.Model):

    isbn = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.String(120), index=True)
    author = db.Column(db.String(120), index=True, unique=True)
    year = db.Column(db.Integer)
    book_review = db.relationship('Review', backref='book_review', lazy='dynamic')


    def importbooks(file):

        f = open(file)
        reader = csv.reader(f)

        for isbn, title, author, year in reader:
            book = Book(isbn=isbn, title=title, author=author, year=year)
            db.session.add(book)

        db.session.commit()


    def __repr__(self):
        return '<Book {}>'.format(self.title)