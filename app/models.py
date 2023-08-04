from . import db

class Book(db.Model):
    __tablename__ = 'books'
    isbn = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)

    def to_json(self):
        return {
            'isbn': self.isbn,
            'image': self.image,
            'author': self.author,
            'title': self.title,
            'price': self.price
        }

