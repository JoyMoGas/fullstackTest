from flask import Flask, jsonify

app = Flask(__name__)

# Simulando datos de libros (esto podría venir de una API externa)
books = [
    {"title": "Clean Code", "author": "Robert C. Martin", "image": "https://example.com/cleancode.jpg"},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "image": "https://example.com/pragmatic.jpg"}
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
