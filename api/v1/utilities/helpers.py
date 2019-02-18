""" module holding helper functions """
from functools import wraps
import re
import jwt
from flask import jsonify, request
from api.v1.models import Redflags, Interventions, Users
from flask import current_app as app
import datetime

red = Redflags()
incid = Interventions()
user = Users()


def update_redflags(redflag_id, column, column_data):
    flag_list = red.get_specific_redflag(redflag_id)
    if flag_list:
        red.edit_redflags(redflag_id, column, column_data)
        return "Updated redflags {}".format(column), 200
    return "Redflag not found in records", 404


def patch_interventions(intervention_id, column, column_data):
    incid_list = incid.get_single_intervention(intervention_id)
    if incid_list:
        incid.edit_interventions(intervention_id, column, column_data)
        return "Updated interventions {}".format(column), 200
    return "Intervention record not found", 404


def verify_admin(logged_user):
    """verifies if user is admin"""
    return logged_user['role'] == 'admin'

def verify_user(logged_user):
    """verifies if user is not admin"""
    return logged_user['role'] == 'user'

# def validate_user(logged_user):
#     """ checks for the user who is logged on to the system """
#     return logged_user['user_id'] == user_id


class Secure_jwt:
    SECRET = 'akokoro'

    def encode_token(self, username):
        """method to generate token """

        payload = {
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        }
        return jwt.encode(payload, 'akokoro', algorithm='HS256')


instan_jwt = Secure_jwt()


def secured(f):
    """Decorator for protecting routes"""
    @wraps(f)
    def decorator(*args, **kwargs):
        access_token = None
        if 'Authorization' in request.headers:
            access_token = request.headers['Authorization']
           
        if not access_token:
            return jsonify(
                {'status': 401, 'error': 'Missing authorization token'}), 401
        access_token = access_token.split(" ")[1]
        try:
            payload = jwt.decode(access_token, 'akokoro', algorithms=['HS256'])
            logged_user = user.check_username(payload['user'])
        except jwt.ExpiredSignatureError:
            return jsonify(
                {'status': 401, 'error': 'Access token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify(
                {'status': 401, 'error': 'Access token is invalid'}), 401
        return f(logged_user, *args, **kwargs)
    return decorator
