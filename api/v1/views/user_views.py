# from flask import jsonify, request, make_response
# from api.v1 import app
# from api.v1.models.users import Users
# from werkzeug.security import generate_password_hash, check_password_hash
# users = []

# @app.route('/api/v1/auth/signup', methods=['POST'])
# def signup_user():
#     """ method implementing the signup endpoint """
#     data = request.get_json(force=True)
#     username = data.get("user_name")
#     email = data.get("email")
#     role = data.get("role")

#     for user in users:
#         if user.username == data['user_name']:
#             return jsonify({"status": 400, "message": "username already exists"}), 400

#             user_id = len(users) + 1
#             secret_key = generate_password_hash(data['password'], method='sha256')
#             kwargs = {
#                 "user_id": user_id,
#                 "first_name": data['first_name'],
#                 "last_name": data['last_name'],
#                 "email": data['email'],
#                 "phone_number": data['phone_number'],
#                 "user_name": data['user_name'],
#                 "role": data['role'],
#                 "password": data['password'],
#             }
#             user = Users(**kwargs)
#             users.append(user)
#             return jsonify({'status': 201, "data": [{"user_id":user_id, 'message': 'User registered successfully'}]}), 201
#         return jsonify({'message': 'invalid'})

# # @app.route('/api/v1/auth/login', methods=['POST'])
# # def user_login():
# #     """ methods implementing login endpoint """
# #     data = request.get_json()
# #     user_name = data.get("user_name")
# #     password = data.get("password")