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
                'id' : Redflags.len_of_redflag_dict(),
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
                return make_response(jsonify({"status" : 201, "data" : [{"id": int(id), "message": "Created red-flag record"}]}))
    except Exception:
                return make_response(jsonify({"error": "Invalid input format"}), 400)