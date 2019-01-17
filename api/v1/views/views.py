from flask import jsonify, make_response, request
from api.v1 import app
from api.v1.models.Redflags import Redflags
from api.v1.validators import Validators

validate = Validators()
db = []


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
            'flagid': Redflags.len_of_redflag_dict(),
            'created_On': data['created_On'],
            'created_By': data['created_By'],
            'incident_Type': data['incident_Type'],
            'location': data['location'],
            'status': data['status'],
            'images': data['images'],
            'comment': data['comment']
        }
        id = Redflags.len_of_redflag_dict()
        if not Validators.validate_input_string(
                redflag['incident_Type'], redflag['status']):
            return make_response(jsonify(
                {'status': 400, 'error': 'incident_Type or status cannot have empty spaces'}), 400)
        elif not Validators.validate_comment_and_location(redflag['comment'], redflag['location']):
            return make_response(
                jsonify(
                    {
                        'status': 400,
                        'error': 'comment and location fields cannot be empty and comment takes alphabets'}),
                400)
        elif not Validators.validate_status_and_image(redflag['status'], redflag['images']):
            return make_response(jsonify(
                {'status': 400, 'error': 'The status and image fields cannot be empty'}), 400)
        created_On = request.json['created_On']
        valid_created_On = Validators.validate_date_created(created_On)
        if valid_created_On:
            return valid_created_On
        for redflag_data in db:
            if redflag_data['created_By'] == redflag['created_By'] and redflag_data['comment'] == redflag['comment']:
                return jsonify({"error": "Redflag record already exists"}), 400
        create_redflag = Redflags.create_redflag(redflag)
        db.append(redflag)
        if create_redflag:
            return make_response(jsonify({"status": 201, "data": [
                                 {"flagid": int(id), "message": "Created red-flag record"}]}), 201)
    except Exception:
        return make_response(jsonify({"error": "Invalid input format"}), 400)


@app.route('/api/v1/redflags', methods=['GET'])
def get_redflags():
    """ method implementing get all redflags endpoint """
    all_redflags = Redflags.get_all_redflags()
    if all_redflags:
        return make_response(jsonify({'status': 200, 'redflag_list': db}))


@app.route('/api/v1/redflags/<int:flagid>', methods=['GET'])
def get_specific_redflag(flagid):
    """ gets a specific redflag by id """
    get_a_redflag = Redflags.get_single_redflag(flagid)
    if get_a_redflag:
        return make_response(
            jsonify({'status': 200, 'redflag': get_a_redflag}), 200)
    else:
        return make_response(
            jsonify({'status': 404, 'message': 'Redflag not found'}), 400)


@app.route('/api/v1/redflags/<int:flagid>/location', methods=['PATCH'])
def edit_redflags_location(flagid):
    """ edits the location of a redflag """
    red_flag = [flag for flag in db if flag['flagid'] == flagid]
    if len(red_flag) == 0:
        return jsonify({'error': 'Redflag not found'})
    red_flag[0]['location'] = request.json.get(
        'location', red_flag[0]['location'])
    if red_flag[0]['location']:
        return make_response(
            jsonify({"message": "Updated redflag's location"}), 200)


@app.route('/api/v1/redflags/<int:flagid>/comment', methods=['PATCH'])
def edit_redflags_comments(flagid):
    """ edits the comments of a redflag """
    for redflag in db:
        if redflag['flagid'] == flagid:
            edited_comment = request.get_json()
            redflag['comment'] = edited_comment['comment']
            return jsonify({"status": 200, "data": [{"flagid": int(
                flagid), "message": "Updated redflag's comment"}]})
    return jsonify({'status': 404, 'error': 'Redflag not found'})


@app.route('/api/v1/redflags/<int:flagid>', methods=['DELETE'])
def delete_redflag(flagid):
    """ deletes a redflag from records """
    redflag = [flag for flag in db if flag['flagid'] == flagid]
    if redflag:
        db.remove(redflag[0])
        response = {"status": 200, "data": [
            {"flagid": int(flagid), "message": "red-flag record has been deleted"}]}
        return jsonify(response)
    return jsonify({'status': 404, 'error': 'Redflag doesnot exist'})
