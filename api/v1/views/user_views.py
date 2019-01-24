from flask import jsonify, make_response, request
from api.v1 import app
from api.v1.models import Users
from api.v1.utilities.helpers import instan_jwt

user = Users()


@app.route('/api/v1/auth/signup', methods=['POST'])
def create_user():
    """ method implementing the signup user endpoint """
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    role = request.json['role']

    if not user.validate_email(email):
        return jsonify(
            {'error': 'email should be in the form someone@example.com'}), 400
    if not user.valid_password(password):
        return jsonify(
            {'error': 'password should contain atleast 6 characters, some uppercase \
            letters of the alphabet, numbers and cannot have empty spaces'}), 400
    if not user.valid_username(username):
        return jsonify(
            {'error': 'username field should have length of atleast 3 characters, \
            should not have empty spaces, cannot be empty and should contain alphabets'}), 400
    if not user.valid_firstname(firstname):
        return jsonify(
            {'error': 'firstname field should have length of atleast 3 characters, \
            should not have empty spaces, cannot be empty and should contain alphabets'}), 400
    if not user.valid_lastname(lastname):
        return jsonify(
            {'error': 'lastname field should have length of atleast 3 characters, \
            should not have empty spaces, cannot be empty and should contain alphabets'}), 400
    if not user.valid_role(role):
        return jsonify({'error': 'role can be either admin or user only'}), 400
    check_user = user.check_username(username)
    if check_user:
        return jsonify({'message': 'username already exist'}), 400
    signup_data = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password": password,
        "email": email,
        "role": role
    }
    user.signup_user(signup_data)
    return make_response(
        jsonify({"message": "User registered successfully"}), 201)


@app.route('/api/v1/auth/admin', methods=['POST'])
def create_admin():
    """ method implementing the signup user endpoint """
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    role = request.json['role']

    if not user.validate_email(email):
        return jsonify(
            {'error': 'email should be in the form someone@example.com'}), 400
    if not user.valid_password(password):
        return jsonify(
            {'error': 'password should contain atleast 6 characters, some letters \
            of the alphabets, numbers and cannot have empty spaces'}), 400
    if not user.valid_username(username):
        return jsonify(
            {'error': 'username field should have length of atleast 3 characters, \
            should not have empty spaces, cannot be empty and should contain alphabets'}), 400
    if not user.valid_lastname(lastname):
        return jsonify(
            {'error': 'lastname field should have length of atleast 3 characters, \
            should not have empty spaces, cannot be empty and should contain alphabets'}), 400
    if not user.valid_firstname(firstname):
        return jsonify(
            {'error': 'firstname field should have length of atleast 3 characters, \
            should not have empty spaces, cannot be empty and should contain alphabets'}), 400
    if not user.valid_role(role):
        return jsonify({'error': 'role can be either admin or user only'}), 400
    check_user = user.check_username(username)
    if check_user:
        return jsonify({'message': 'Admin username already exist'}), 400
    signup_data = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "password": password,
        "email": email,
        "role": role
    }
    user.signup_user(signup_data)
    return make_response(
        jsonify({"message": "Admin registered successfully"}), 201)


@app.route('/api/v1/auth/login', methods=['POST'])
def sigin_user():
    """ method implementing api for siging in a user """
    data = request.get_json()
    login_data = {
        "username": data.get('username'),
        "password": data.get('password')
    }
    login = user.login_user(login_data)
    if not login:
        return jsonify({'message': 'username doesnot exist'})
    pass_check = user.verify_password(
        login["password"], login_data["password"])
    if login and pass_check:
        access_token = instan_jwt.encode_token(login_data['username'])
        return jsonify({"status": 200, "message": "You are now logged in",
                        "access_token": access_token.decode('UTF-8')}), 200
    else:
        return make_response(
            jsonify({"message": "username or password is wrong"}), 400)
