import os
from . import create_app
from .models import Book
from flask import jsonify
from flask import request
from app import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route("/book/list", methods=["GET"])
def get_books():
    limit = request.args.get('limit', type=int, default=0)
    page = request.args.get('page', type=int, default=-1)
    if limit == 0 or page == -1:
        books = Book.query.all()
        return jsonify([book.to_json() for book in books])
    else:
        books = Book.query
        if limit:
            books = books.limit(limit)
        if page:
            books = books.offset(limit*page)
        return jsonify([book.to_json() for book in books])

@app.route("/book/<int:isbn>", methods=["GET"])
def get_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        os.abort(404)
    return jsonify(book.to_json())


@app.route('/book', methods=['POST'])
def create_book():
    if not request.json:
        os.abort(400)
    book = Book(
        title=request.json.get('title'),
        author=request.json.get('author'),
        price=request.json.get('price')
    )
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_json()), 201


@app.route('/book/<int:isbn>', methods=['PUT'])
def update_book(isbn):
    if not request.json:
        os.abort(400)
    book = Book.query.get(isbn)
    if book is None:
        os.abort(404)
    book.title = request.json.get('title', book.title)
    book.author = request.json.get('author', book.author)
    book.price = request.json.get('price', book.price)
    db.session.commit()
    return jsonify(book.to_json())