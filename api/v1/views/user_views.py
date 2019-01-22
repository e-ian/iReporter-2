from flask import jsonify, make_response, request
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from api.v1 import app
from api.v1.db_handler import Users
from api.v1.validators import Validators

b = Users()
validate = Validators()

@app.route('/api/v1/auth/signup', methods=['POST'])
def create_user():
    """ method implementing the signup user endpoint """
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    role = request.json['role']

    valid_firstname = validate.validate_inputs(firstname)
    valid_lastname = validate.validate_inputs(lastname)
    valid_username = validate.validate_inputs(username)
    valid_role = validate.validate_inputs(role)
    valid_pass = validate.valid_password(password)
    valid_email = validate.validate_email(email)
    if valid_firstname:
        return valid_firstname
    if valid_lastname:
        return valid_lastname
    if valid_username:
        return valid_username
    if valid_role:
        return valid_role
    if valid_pass:
        return valid_pass
    if valid_email:
        return valid_email
    check_user = b.check_username(username)
    if check_user:
        return jsonify({'message': 'username already exist'}), 400
    signup_data ={
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password": password,
        "email": email,
        "role": role
    }
    b.signup_user(signup_data)
    return make_response(jsonify({"message": "User registered successfully"}), 201)

@app.route('/api/v1/auth/admin', methods=['POST'])
def create_admin():
    """ method implementing the signup user endpoint """
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    role = request.json['role']

    valid_firstname = validate.validate_inputs(firstname)
    valid_lastname = validate.validate_inputs(lastname)
    valid_username = validate.validate_inputs(username)
    valid_role = validate.validate_inputs(role)
    valid_pass = validate.valid_password(password)
    valid_email = validate.validate_email(email)
    if valid_firstname:
        return valid_firstname
    if valid_lastname:
        return valid_lastname
    if valid_username:
        return valid_username
    if valid_role:
        return valid_role
    if valid_pass:
        return valid_pass
    if valid_email:
        return valid_email
    check_user = b.check_username(username)
    if check_user:
        return jsonify({'message': 'Admin username already exist'}), 400
    signup_data ={
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password": password,
        "email": email,
        "role": role
    }
    b.signup_user(signup_data)
    return make_response(jsonify({"message": "Admin registered successfully"}), 201)

@app.route('/api/v1/auth/login', methods=['POST'])
def sigin_user():
    """ method implementing api for siging in a user """
    login_data ={
        "username": request.json['username'],
        "password": request.json['password']
    }
    login = b.login_user(login_data)
    if not login:
        return jsonify({'message': 'username doesnot exist'})
    pass_check = b.verify_password(login["password"], login_data["password"])

    if login and pass_check:
        access_token = create_access_token(identity=login)
        return jsonify({"status": 200, "message": "You are now logged in", "access_token":access_token}), 200
    else:
        return make_response(jsonify({"message": "username or password is wrong"}), 400)