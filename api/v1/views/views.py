from flask import jsonify, make_response, request
from api.v1 import app
from api.v1.models.redflags import Redflags

@app.route('/')
def home():
    """default route for homepage"""

    return jsonify({'message': 'Welcome to iReporter'})

@app.route('/api/v1/redflags', methods=['POST'])
def create_redflag():
    """ method implementing the create redflag api """
    
    data = request.get_json(force=True)
    redflag = {
        'id' : Redflags.len_of_redflag_dict(),
        'createdOn' : data['createdOn'],
        'createdBy' : data['createdBy'],
        'type' : data['type'],
        'location' : data['location'],
        'status' : data['status'],
        'Images' : data['Images'],
        'Videos' : data['Videos'],
        'comment' : data['comment']
    }
    id = Redflags.len_of_redflag_dict()
    create_redflag = Redflags.create_redflag(redflag)
    if create_redflag:
        return make_response(jsonify({"status" : 201, "data" : [{"id": int(id), "message": "Created red-flag record"}]}))
    else:
        return jsonify({"error": "Invalid input format"})