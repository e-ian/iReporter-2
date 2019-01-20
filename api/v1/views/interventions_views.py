from flask import jsonify, make_response, request
from api.v1 import app
from api.v1.db_handler import Interventions
# from api.v1.utilities.helpers import update_redflags
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
        if not Validators.validate_input_string(
                intervention['incident_type'], intervention['status']):
            return make_response(jsonify(
                {'status': 400, 'error': 'incident_type or status cannot have empty spaces'}), 400)
        elif not Validators.validate_comment_and_location(intervention['comment'], intervention['location']):
            return make_response(
                jsonify(
                    {
                        'status': 400,
                        'error': 'comment and location fields cannot be empty and comment takes alphabets'}),
                400)
        elif not Validators.validate_status_and_image(intervention['status'], intervention['image']):
            return make_response(jsonify(
                {'status': 400, 'error': 'The status and image fields cannot be empty'}), 400)        
        check_intervention = incid.check_intervention(intervention['created_by'], intervention['comment'])        
        if check_intervention:
            return jsonify({"message": "Intervention record already exists"})
        valid_intervention = incid.create_intervention(intervention)
        return make_response(jsonify({"status": 201, "data": [
                                    {"intervention_id": int(valid_intervention['intervention_id']), "message": "Created intervention record"}]}), 201)
    except Exception:
        return make_response(jsonify({"error": "Invalid input format"}), 400)

