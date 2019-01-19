from flask import Flask
from api.v1.models import Database

app = Flask(__name__)

db_connect = Database()
from api.v1.views import views, user_views