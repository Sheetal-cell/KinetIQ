from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__, static_folder='../frontend')
CORS(app)

@app.route('/data')
def send_data():
    with open('../data/data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def serve_dashboard():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
