from flask import jsonify, make_response, request
from api.v1 import app
from api.v1.models.redflags import Redflags
from api.v1.models.validators import Validators

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
                'flagid' : Redflags.len_of_redflag_dict(),
                'createdOn' : data['createdOn'],
                'createdBy' : data['createdBy'],
                'incidenttype' : data['incidenttype'],
                'location' : data['location'],
                'status' : data['status'],
                'Images' : data['Images'],
                'Videos' : data['Videos'],
                'comment' : data['comment']
            }
            id = Redflags.len_of_redflag_dict()
            if not Validators.validate_input_string(redflag['incidenttype'], redflag['location'], redflag['status'], redflag['comment']):
                return make_response(jsonify({'error': 'incidenttype, location, status or comment cannot have empty spaces'}), 400)
            createdOn = request.json['createdOn']
            valid_createdOn = Validators.validate_date_created(createdOn)
            if valid_createdOn:
                return valid_createdOn
            create_redflag = Redflags.create_redflag(redflag)
            if create_redflag:
                return make_response(jsonify({"status" : 201, "data" : [{"flagid": int(id), "message": "Created red-flag record"}]}))
    except Exception:
                return make_response(jsonify({"error": "Invalid input format"}), 400)

@app.route('/api/v1/redflags', methods=['GET'])
def get_redflags():
    """ method implementing get all redflags endpoint """
    # if redflag_list == []:
    #     return make_response(jsonify({'status': 404, 'error': 'No redflags have been posted yet'}))
    all_redflags = Redflags.get_all_redflags()
    if all_redflags:
        return make_response(jsonify({'status': 200, 'redflag_list':all_redflags}))

@app.route('/api/v1/redflags/<int:flagid>')
def get_specific_redflag(flagid):
    """ gets a specific redflag by id """
    get_a_redflag = Redflags.get_specific_redflag(flagid)
    if get_a_redflag:
        return make_response(jsonify({'status': 200, 'redflag': get_a_redflag}))
    else:
        return make_response(jsonify({'status': 404, 'message': 'Redflag not found'}))