from flask import jsonify, make_response, request
from api.v1 import app
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity)
from api.v1.models import Interventions
from api.v1.utilities.helpers import patch_interventions
from api.v1.validators import Validators

incid = Interventions()
validate = Validators()


@app.route('/api/v1/interventions', methods=['POST'])
def create_intervention():
    """ method implementing create intervention api """
    try:
        form_data = request.get_json(force=True)
        intervention = {
            'created_by': form_data['created_by'],
            'incident_type': form_data['incident_type'],
            'location': form_data['location'],
            'status': form_data['status'],
            'image': form_data['image'],
            'comment': form_data['comment']
        }

        if not incid.check_status(intervention['status']):
            return make_response(jsonify(
                {'status': 400, 'error': 'status can only be posted as a draft'}), 400)
        elif not incid.validate_incident_type(intervention['incident_type']):
            return make_response(jsonify(
                {'status': 400, 'error': 'incident type can only be intervention'}), 400)
        elif not incid.valid_comment(intervention['comment']):
            return jsonify(
            {'error': 'comment field should be a string and should contain alphabets'}), 400
        elif not incid.validate_location(intervention['location']):
            return make_response(
                jsonify(
                    {
                        'status': 400,
                        'error': 'location field cannot be empty'}), 400)
        elif not incid.validate_image(intervention['image']):
            return make_response(jsonify(
                {'status': 400, 'error': 'The image field cannot be empty'}), 400)
        check_intervention = incid.check_intervention(
            intervention['created_by'], intervention['comment'])
        if check_intervention:
            return jsonify(
                {"message": "Intervention record already exists"}), 400
        valid_intervention = incid.create_intervention(intervention)
        return make_response(jsonify({"status": 201, "data": [{"intervention_id": int(
            valid_intervention['intervention_id']), "message": "Created intervention record"}]}), 201)
    except:
        return make_response(jsonify({"error": "Invalid input format"}), 400)


@app.route('/api/v1/interventions', methods=['GET'])
def get_interventions():
    """ method implementing get all redflags endpoint """
    all_interventions = incid.get_interventions()
    if all_interventions:
        return make_response(
            jsonify({'status': 200, 'interventions_list': all_interventions}), 200)


@app.route('/api/v1/interventions/<int:intervention_id>', methods=['GET'])
def get_specific_intervention(intervention_id):
    """ gets a specific intervention by id """
    get_intervention = incid.get_single_intervention(intervention_id)
    if get_intervention:
        return make_response(
            jsonify({'status': 200, 'intervention': get_intervention}), 200)
    else:
        return make_response(
            jsonify({'status': 404, 'message': 'Intervention record not found'}), 400)


@app.route(
    '/api/v1/interventions/<int:intervention_id>/location',
    methods=['PATCH'])
def edit_intervention_location(intervention_id):
    """ edits the location of an intervention """
    try:
        data = request.get_json(force=True)

        message, status = patch_interventions(
            intervention_id, 'location', data['location'])

        return make_response(jsonify({"message": message}), status)
    except:
        return jsonify(
            {"error": "Please enter a valid key for location field as location"}), 400


@app.route(
    '/api/v1/interventions/<int:intervention_id>/comment',
    methods=['PATCH'])
def edit_intervention_comment(intervention_id):
    """ edits the comment of an intervention """
    try:
        data = request.get_json(force=True)

        message, status = patch_interventions(
            intervention_id, 'comment', data['comment'])

        return make_response(jsonify({"message": message}), status)
    except:
        return jsonify(
            {"error": "Please enter a valid key for comment field as comment"}), 400


@app.route(
    '/api/v1/interventions/<int:intervention_id>/status',
    methods=['PATCH'])
@jwt_required
def edit_intervention_status(intervention_id):
    """ edits the status of an intervention """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify(
            {'message': 'Unauthorised access, please login as admin'}), 401
    try:
        data = request.get_json(force=True)

        message, status = patch_interventions(
            intervention_id, 'status', data['status'])

        return make_response(jsonify({"message": message}), status)
    except:
        return jsonify(
            {"error": "Please enter a valid key for status field as status"}), 400


@app.route('/api/v1/interventions/<int:intervention_id>', methods=['DELETE'])
def del_intervention(intervention_id):
    """ deletes a redflag from records """
    intervention_list = incid.get_single_intervention(intervention_id)
    if intervention_list:
        incid.delete_intervention(intervention_id)
        response = {"status": 200, "data": [{"intervention_id": int(
            intervention_list['intervention_id']), "message": "Intervention record has been deleted"}]}
        return jsonify(response)
    return jsonify({'status': 404, 'error': 'intervention doesnot exist'}), 404
