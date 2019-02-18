from flask import jsonify, make_response, request
from api.v1.utilities.helpers import verify_admin, secured, verify_user
from api.v1 import app
from api.v1.models import Interventions
from api.v1.utilities.helpers import patch_interventions

incid = Interventions()


@app.route('/api/v1/interventions', methods=['POST'])
@secured
def create_intervention(logged_user):
    """ method implementing create intervention api """
    if verify_admin(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    try:
        form_data = request.get_json(force=True)
        incident_type = form_data['incident_type']
        location = form_data['location']
        status = form_data['status']
        image = form_data['image']
        comment = form_data['comment']
        if not incid.check_status(status):
            return make_response(jsonify(
                {'status': 400, 'error': 'status can only be posted as a draft'}), 400)
        elif not incid.validate_incident_type(incident_type):
            return make_response(jsonify(
                {'status': 400, 'error': 'incident type can only be intervention'}), 400)
        elif not incid.valid_comment(comment):
            return jsonify(
                {'error': 'comment field should be a string and should contain alphabets'}), 400
        elif not incid.validate_location(location):
            return make_response(
                jsonify(
                    {
                        'status': 400,
                        'error': 'location field cannot be empty'}), 400)
        elif not incid.validate_image(image):
            return make_response(jsonify(
                {'status': 400, 'error': 'The image field cannot be empty'}), 400)
        check_intervention = incid.check_intervention(
            logged_user['username'], comment)
        if check_intervention:
            return jsonify(
                {"message": "Intervention record already exists"}), 400
        valid_intervention = incid.create_intervention(
            logged_user['username'], incident_type, location, status, image, comment)
        return make_response(jsonify({"status": 201, "data": [{"intervention_id": int(
            valid_intervention['intervention_id']), "message": "Created intervention record"}]}), 201)
    except Exception:
        return make_response(jsonify({"error": "Invalid input format"}), 400)


@app.route('/api/v1/interventions', methods=['GET'])
@secured
def get_interventions(logged_user):
    """ method implementing get all redflags endpoint """
    if logged_user['role'] == 'admin':        
        all_interventions = incid.get_interventions()
        if all_interventions:
            return make_response(
            jsonify({'status': 200, 'interventions_list': all_interventions}), 200)
        return jsonify({'status': 200, 'message': 'No interventions to display'})
    created_by = logged_user['username']
    records = incid.get_user_interventions(created_by)
    if records:
        return make_response(jsonify({'status': 200, 'interventions_list': records}))


@app.route('/api/v1/interventions/<int:intervention_id>', methods=['GET'])
@secured
def get_specific_intervention(logged_user, intervention_id):
    """ gets a specific intervention by id """
    get_intervention = incid.get_single_intervention(intervention_id)
    if get_intervention:
        return make_response(
            jsonify({'status': 200, 'intervention': get_intervention}), 200)
    return make_response(
        jsonify({'status': 404, 'message': 'Intervention record not found'}), 400)


@app.route(
    '/api/v1/interventions/<int:intervention_id>/location',
    methods=['PATCH'])
@secured
def edit_intervention_location(logged_user, intervention_id):
    """ edits the location of an intervention """
    if verify_admin(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    try:
        data = request.get_json(force=True)

        message, status = patch_interventions(
            intervention_id, 'location', data['location'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify(
            {"error": "Please enter a valid key for location field as location"}), 400


@app.route(
    '/api/v1/interventions/<int:intervention_id>/comment',
    methods=['PATCH'])
@secured
def edit_intervention_comment(logged_user, intervention_id):
    """ edits the comment of an intervention """
    if verify_admin(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    try:
        data = request.get_json(force=True)

        message, status = patch_interventions(
            intervention_id, 'comment', data['comment'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify(
            {"error": "Please enter a valid key for comment field as comment"}), 400


@app.route(
    '/api/v1/interventions/<int:intervention_id>/status',
    methods=['PATCH'])
@secured
def edit_intervention_status(logged_user, intervention_id):
    """ edits the status of an intervention """
    if verify_user(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    try:
        data = request.get_json(force=True)

        message, status = patch_interventions(
            intervention_id, 'status', data['status'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify(
            {"error": "Please enter a valid key for status field as status"}), 400


@app.route('/api/v1/interventions/<int:intervention_id>', methods=['DELETE'])
@secured
def del_intervention(logged_user, intervention_id):
    """ deletes a redflag from records """
    intervention_list = incid.get_single_intervention(intervention_id)
    if intervention_list:
        incid.delete_intervention(intervention_id)
        response = {"status": 200, "data": [{"intervention_id": int(
            intervention_list['intervention_id']), "message": "Intervention record has been deleted"}]}
        return jsonify(response)
    return jsonify({'status': 404, 'error': 'intervention doesnot exist'}), 404
