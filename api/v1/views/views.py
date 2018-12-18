from flask import jsonify, make_response, request
from api.v1 import app

@app.route('/')
def home():
    """default route for homepage"""

    return jsonify({'message': 'Welcome to iReporter'})