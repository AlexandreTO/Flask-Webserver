from flask import render_template, jsonify, redirect, url_for, Blueprint, request
from book import Book
from database import db

# Blueprints
routes = Blueprint('routes', __name__)

@routes.route("/")
def index():
    return 'Index Page'

@routes.route("/hello")
def hello_world():
    return render_template('index.html')

@routes.route("/admin")
def hello_admin():
    return 'Admin'

@routes.route("/user/<name>")
def hello_user(name):
    return 'Hello %s' % name

### URL BUILDING
@routes.route('/user/<name>')
def hello_specific_name(name):
    if name == 'Alexandre':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user', name = name ))

# JSON test
def json_response():
    response = {"name": "Alexandre", "age": 29}
    return jsonify([response])

# API
# Get ALL books
@routes.route('/api/books', methodes=['GET'])
def get_books():
    #Pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    books = Book.query.paginate(page, per_page, False)
    return jsonify({
        'books': [book.to_dict() for book in books.items],
        'page': page,
        'per_page': per_page,
        'total': books.total
    })

# Create a book
@routes.route('/api/books', methods=['POST'])
def create_book():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    new_book = Book(
        title = request.json['title'],
        author = request.json['author'],
        genre = request.json['genre']
    )

    data = request.get_json()
    
    if 'title' not in data or 'author' not in data or 'genre' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

#Get one book with his id
@routes.route('/api/book<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())

#Update a book
@routes.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    
    if 'title' in request.json:
        book.title = request.json['title']
    if 'author' in request.json:
        book.author = request.json['author']
    if 'genre' in request.json:
        book.genre = request.json['genre']
        
    db.session.commit()
    return jsonify(book.to_dict())

@routes.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}), 200