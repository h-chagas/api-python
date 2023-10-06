from flask import Flask, jsonify, request

app = Flask(__name__)

# Data source
books = [
    {
        'id': 1,
        'title': '365 Days of Dad Jokes',
        'author': 'Jim Chumley'
    },
    {
        'id': 2,
        'title': 'Building High Performance Agile Teams',
        'author': 'Made Tech'
    },
    {
        'id': 3,
        'title': 'Moby-Dick',
        'author': 'Herman Melville'
    },
]


# GET ALL BOOKS
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# CREATE A BOOK
@app.route('/books', methods=['POST'])
def create_a_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

# GET A BOOK BY ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# MODIFY A BOOK
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    edited_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(edited_book)
            return jsonify(books[index])

# DELETE A BOOK
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)


app.run(port=5000, host='localhost', debug=True)

