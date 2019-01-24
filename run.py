"""
module to run the flask app
"""
from api.v1.models import Database
from flask import Flask

from api.v1 import app

if __name__ == '__main__':
    app.run(debug=True)