from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permite solicitudes desde el frontend

@app.route('/api/get', methods=['GET'])
def get_books():
    books = [
        {"title": "1984", "author": "George Orwell", "image": "https://www.designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-tf-2-a-million-to-one.jpg"},
        {"title": "El principito", "author": "Antoine de Saint-Exupéry", "image": "https://www.designforwriters.com/wp-content/uploads/2017/10/design-for-writers-book-cover-jsr-an3-aurora-north-and-the-wicked-witches.jpg"}
    ]
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
