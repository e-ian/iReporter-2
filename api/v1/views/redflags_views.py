from flask import jsonify, make_response, request
from api.v1 import app
from api.v1.db_handler import Redflags
from api.v1.utilities.helpers import update_redflags
from api.v1.validators import Validators

red = Redflags()
validate = Validators()

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
        if not Validators.validate_input_string(
                redflag['incident_type'], redflag['status']):
            return make_response(jsonify(
                {'status': 400, 'error': 'incident_type or status cannot have empty spaces'}), 400)
        elif not Validators.validate_comment_and_location(redflag['comment'], redflag['location']):
            return make_response(
                jsonify(
                    {
                        'status': 400,
                        'error': 'comment and location fields cannot be empty and comment takes alphabets'}),
                400)
        elif not Validators.validate_status_and_image(redflag['status'], redflag['image']):
            return make_response(jsonify(
                {'status': 400, 'error': 'The status and image fields cannot be empty'}), 400)
        
        check_redflag = red.check_redflag(redflag['created_by'], redflag['comment'])
        
        if check_redflag:
            return jsonify({"message": "Redflag record already exists"})
        red_flag = red.create_redflag(redflag)
        return make_response(jsonify({"status": 201, "data": [
                                    {"redflag_id": int(red_flag['redflag_id']), "message": "Created red-flag record"}]}), 201)
    except Exception:
        return make_response(jsonify({"error": "Invalid input format"}), 400)


@app.route('/api/v1/redflags', methods=['GET'])
def get_redflags():
    """ method implementing get all redflags endpoint """
    all_redflags = red.get_redflags()
    if all_redflags:
        return make_response(jsonify({'status': 200, 'redflag_list': all_redflags}))

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

        message, status = update_redflags( redflag_id, 'location', data['location'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify({"error": "Please enter a valid key for location field as 'location' "}), 400

@app.route('/api/v1/redflags/<int:redflag_id>/comment', methods=['PATCH'])
def edit_redflags_comments(redflag_id):
    """ edits the comments of a redflag """
    try:
        data = request.get_json(force=True)

        message, status = update_redflags( redflag_id, 'comment', data['comment'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify({"error": "Please enter a valid key for comment field as 'comment' "}), 400

@app.route('/api/v1/redflags/<int:redflag_id>/status', methods=['PATCH'])
def edit_redflags_status(redflag_id):
    """ edits the status of a redflag """
    try:
        data = request.get_json(force=True)

        message, status = update_redflags( redflag_id, 'status', data['status'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify({"error": "Please enter a valid key for status field as 'status' "}), 400

@app.route('/api/v1/redflags/<int:redflag_id>', methods=['DELETE'])
def delete_redflag(redflag_id):
    """ deletes a redflag from records """
    flag_list = red.get_specific_redflag(redflag_id)
    if flag_list:
        red.delete_redflag(redflag_id)
        response = {"status": 200, "data": [
            {"flagid": int(flag_list['redflag_id']), "message": "red-flag record has been deleted"}]}
        return jsonify(response)
    return jsonify({'status': 404, 'error': 'Redflag doesnot exist'})
