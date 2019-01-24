from flask import jsonify, make_response, request
from api.v1.utilities.helpers import verify_admin, secured, verify_user
from api.v1 import app
from api.v1.models import Redflags, Interventions
from api.v1.utilities.helpers import update_redflags

red = Redflags()
incid = Interventions()


@app.route('/')
def home():
    """default route for homepage"""

    return jsonify({'message': 'Welcome to iReporter'})


@app.route('/api/v1/redflags', methods=['POST'])
@secured
def create_redflag(logged_user):
    """ method implementing the create redflag api """
    if verify_admin(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    try:
        data = request.get_json(force=True)
        incident_type = data['incident_type']
        location = data['location']
        status = data['status']
        image = data['image']
        comment = data['comment']
        if not incid.check_status(status):
            return make_response(jsonify(
                {'status': 400, 'error': 'status can only be posted as a draft'}), 400)
        elif not red.validate_if_redflag(incident_type):
            return make_response(jsonify(
                {'status': 400, 'error': 'incident type can only be redflag'}), 400)
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
        check_redflag = red.check_redflag(
            logged_user['user_id'], comment)
        if check_redflag:
            return jsonify({"message": "Redflag record already exists"}), 400
        red_flag = red.create_redflag(logged_user['user_id'], incident_type, location, status, image, comment)
        return make_response(jsonify({"status": 201, "data": [{"redflag_id": int(
            red_flag['redflag_id']), "message": "Created red-flag record"}]}), 201)
    except Exception:
        return make_response(jsonify({"error": "Invalid input format"}), 400)


@app.route('/api/v1/redflags', methods=['GET'])
@secured
def get_redflags(logged_user):
    """ method implementing get all redflags endpoint """
    all_redflags = red.get_redflags()
    if all_redflags:
        return make_response(
            jsonify({'status': 200, 'redflag_list': all_redflags}))


@app.route('/api/v1/redflags/<int:redflag_id>', methods=['GET'])
@secured
def get_specific_redflag(logged_user, redflag_id):
    """ gets a specific redflag by id """
    get_redflag = red.get_specific_redflag(redflag_id)
    if get_redflag:
        return make_response(
            jsonify({'status': 200, 'redflag': get_redflag}), 200)
    else:
        return make_response(
            jsonify({'status': 404, 'message': 'Redflag not found'}), 400)


@app.route('/api/v1/redflags/<int:redflag_id>/location', methods=['PATCH'])
@secured
def edit_redflags_location(logged_user, redflag_id):
    """ edits the location of a redflag """
    if verify_admin(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    try:
        data = request.get_json(force=True)

        message, status = update_redflags(
            redflag_id, 'location', data['location'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify(
            {"error": "Please enter a valid key for location field as location"}), 400


@app.route('/api/v1/redflags/<int:redflag_id>/comment', methods=['PATCH'])
@secured
def edit_redflags_comments(logged_user, redflag_id):
    """ edits the comments of a redflag """
    if verify_admin(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    try:
        data = request.get_json(force=True)

        message, status = update_redflags(
            redflag_id, 'comment', data['comment'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify(
            {"error": "Please enter a valid key for comment field as comment"}), 400


@app.route('/api/v1/redflags/<int:redflag_id>/status', methods=['PATCH'])
@secured
def edit_redflags_status(logged_user, redflag_id):
    """ edits the status of a redflag """
    if verify_user(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    try:
        data = request.get_json(force=True)

        message, status = update_redflags(redflag_id, 'status', data['status'])

        return make_response(jsonify({"message": message}), status)
    except KeyError:
        return jsonify(
            {"error": "Please enter a valid key for status field as status"}), 400


@app.route('/api/v1/redflags/<int:redflag_id>', methods=['DELETE'])
@secured
def del_redflag(logged_user, redflag_id):
    """ deletes a redflag from records """
    if verify_admin(logged_user):
        return jsonify(
            {'status': 403, 'error': "You do not have privileges to perform this request"}), 403
    flag_list = red.get_specific_redflag(redflag_id)
    if flag_list:
        red.delete_redflag(redflag_id)
        response = {"status": 200,
                    "data": [{"flagid": int(flag_list['redflag_id']),
                              "message": "red-flag record has been deleted"}]}
        return jsonify(response)
    return jsonify({'status': 404, 'error': 'Redflag doesnot exist'}), 404
