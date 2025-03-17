import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde otro dominio (frontend)

# Datos de ejemplo
books = [
    {"title": "Clean Code", "author": "Robert C. Martin", "image": "https://example.com/cleancode.jpg"},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "image": "https://example.com/pragmatic.jpg"}
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render asigna un puerto dinámico
    app.run(host='0.0.0.0', port=port)
