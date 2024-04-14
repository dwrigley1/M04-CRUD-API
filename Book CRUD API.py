# Dakota Wrigley
# M04 CRUD API for a Book model

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.string(80), nullable=False)

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "deleted"}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(id=request.json['id'],
                  book_name=request.json['book_name'],
                  author=request.json['author'],
                  publisher=request.json['publisher'])
    db.session.add(Book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'id': book.id, 
                     'name': book.name,
                     'author': book.author,
                     'publisher': book.publisher}
        output.append(book_data)
    return {"books": output}

@app.route('/books', methods=['PUT'])
def update_books(id):
    books = Book.query.get(id)
    for book in books(id):
        book_data = {'id': book.id, 
                     'name': book.name,
                     'author': book.author,
                     'publisher': book.publisher}
        db.session.commit()
        return {'message': 'This book has been updated!'}
    else:
        return {'message': 'Cannot update this book'}