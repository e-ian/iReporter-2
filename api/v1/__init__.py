from flask import Flask
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from api.v1.dbhandler import Database

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'apaclango'
jwt = JWTManager(app)
db_connect = Database()
from api.v1.views import redflags_views
from api.v1.views import interventions_views
from api.v1.views import user_views