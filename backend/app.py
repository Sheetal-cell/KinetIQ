from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

# Set static_folder to access frontend from backend
app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Serve data from data.json
@app.route('/data')
def send_data():
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(data_path) as f:
        data = json.load(f)
    return jsonify(data)

# Serve index.html on root
@app.route('/')
def serve_dashboard():
    return send_from_directory(app.static_folder, 'index.html')

# Serve any static file (CSS, JS, images, etc.)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
