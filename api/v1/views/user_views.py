from flask import jsonify, make_response, request
from api.v1 import app
from api.v1.db_handler import Users
# from api.v1.utilities.helpers import patch_interventions
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
    print(signup_data)
    b.signup_user(signup_data)
    return make_response(jsonify({"message": "User registered successfully"}), 201)