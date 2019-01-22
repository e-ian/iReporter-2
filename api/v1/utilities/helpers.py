""" module holding helper functions """
from api.v1.db_handler import Redflags, Interventions
from werkzeug.security import generate_password_hash, check_password_hash

red = Redflags()
incid = Interventions()

def update_redflags(redflag_id, column, column_data):
    flag_list = red.get_specific_redflag(redflag_id)
    if flag_list:
        red.edit_redflags(redflag_id, column, column_data)
        return "Updated redflag's {}".format(column), 200
    return "Redflag not found in records", 404

def patch_interventions(intervention_id, column, column_data):
    incid_list = incid.get_single_intervention(intervention_id)
    if incid_list:
        incid.edit_interventions(intervention_id, column, column_data)
        return "Updated intervention's {}".format(column), 200
    return "Intervention record not found", 404
