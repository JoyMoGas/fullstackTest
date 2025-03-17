from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permite solicitudes desde el frontend

@app.route('/api/get', methods=['GET'])
def get_books():
    books = [
        {"title": "1984", "author": "George Orwell", "image": "https://via.placeholder.com/150"},
        {"title": "El principito", "author": "Antoine de Saint-Exupéry", "image": "https://via.placeholder.com/150"}
    ]
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
