from flask import jsonify, make_response, request
from api.v1 import app
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity)
from api.v1.models import Redflags, Interventions
from api.v1.utilities.helpers import update_redflags

red = Redflags()
incid = Interventions()

@app.route('/')
def home():
    """default route for homepage"""

    return jsonify({'message': 'Welcome to iReporter'})


@app.route('/api/v1/redflags', methods=['POST'])
def create_redflag():
    """ method implementing the create redflag api """
    try:
        data = request.get_json(force=True)
        redflag = {
            'created_by': data['created_by'],
            'incident_type': data['incident_type'],
            'location': data['location'],
            'status': data['status'],
            'image': data['image'],
            'comment': data['comment']
        }
        if not incid.check_status(redflag['status']):
            return make_response(jsonify(
                {'status': 400, 'error': 'status can only be posted as a draft'}), 400)
        elif not red.validate_if_redflag(redflag['incident_type']):
            return make_response(jsonify(
                {'status': 400, 'error': 'incident type can only be redflag'}), 400)
        elif not incid.valid_comment(redflag['comment']):
            return jsonify(
            {'error': 'comment field should be a string and should contain alphabets'}), 400
        elif not incid.validate_location(redflag['location']):
            return make_response(
                jsonify(
                    {
                        'status': 400,
                        'error': 'location field cannot be empty'}), 400)
        elif not incid.validate_image(redflag['image']):
            return make_response(jsonify(
                {'status': 400, 'error': 'The image field cannot be empty'}), 400)
        check_redflag = red.check_redflag(
            redflag['created_by'], redflag['comment'])
        if check_redflag:
            return jsonify({"message": "Redflag record already exists"}), 400
        red_flag = red.create_redflag(redflag)
        return make_response(jsonify({"status": 201, "data": [{"redflag_id": int(
            red_flag['redflag_id']), "message": "Created red-flag record"}]}), 201)
    except Exception:
        return make_response(jsonify({"error": "Invalid input format"}), 400)


@app.route('/api/v1/redflags', methods=['GET'])
def get_redflags():
    """ method implementing get all redflags endpoint """
    all_redflags = red.get_redflags()
    if all_redflags:
        return make_response(
            jsonify({'status': 200, 'redflag_list': all_redflags}))


@app.route('/api/v1/redflags/<int:redflag_id>', methods=['GET'])
def get_specific_redflag(redflag_id):
    """ gets a specific redflag by id """
    get_redflag = red.get_specific_redflag(redflag_id)
    if get_redflag:
        return make_response(
            jsonify({'status': 200, 'redflag': get_redflag}), 200)
    else:
        return make_response(
            jsonify({'status': 404, 'message': 'Redflag not found'}), 400)


@app.route('/api/v1/redflags/<int:redflag_id>/location', methods=['PATCH'])
def edit_redflags_location(redflag_id):
    """ edits the location of a redflag """
    try:
        data = request.get_json(force=True)

        message, status = update_redflags(
            redflag_id, 'location', data['location'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify(
            {"error": "Please enter a valid key for location field as location"}), 400


@app.route('/api/v1/redflags/<int:redflag_id>/comment', methods=['PATCH'])
def edit_redflags_comments(redflag_id):
    """ edits the comments of a redflag """
    try:
        data = request.get_json(force=True)

        message, status = update_redflags(
            redflag_id, 'comment', data['comment'])

        return make_response(jsonify({"message": message}), status)
    except:
        return jsonify(
            {"error": "Please enter a valid key for comment field as comment"}), 400


@app.route('/api/v1/redflags/<int:redflag_id>/status', methods=['PATCH'])
@jwt_required
def edit_redflags_status(redflag_id):
    """ edits the status of a redflag """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify(
            {'message': 'Unauthorised access, please login as admin'}), 401
    try:
        data = request.get_json(force=True)

        message, status = update_redflags(redflag_id, 'status', data['status'])

        return make_response(jsonify({"message": message}), status)
    except:
        return jsonify(
            {"error": "Please enter a valid key for status field as status"}), 400


@app.route('/api/v1/redflags/<int:redflag_id>', methods=['DELETE'])
def del_redflag(redflag_id):
    """ deletes a redflag from records """
    flag_list = red.get_specific_redflag(redflag_id)
    if flag_list:
        red.delete_redflag(redflag_id)
        response = {"status": 200,
                    "data": [{"flagid": int(flag_list['redflag_id']),
                              "message": "red-flag record has been deleted"}]}
        return jsonify(response)
    return jsonify({'status': 404, 'error': 'Redflag doesnot exist'}), 404
