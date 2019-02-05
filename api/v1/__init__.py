from flask import Flask
from flask_cors import CORS
from api.v1.dbhandler import Database

app = Flask(__name__)
CORS(app)

db_connect = Database()
from api.v1.views import redflags_views
from api.v1.views import interventions_views
from api.v1.views import user_views