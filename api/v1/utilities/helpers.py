""" module holding helper functions """
from api.v1.db_handler import Redflags
red = Redflags()

def update_redflags(redflag_id, column, column_data):
    flag_list = red.get_specific_redflag(redflag_id)
    if flag_list:
        red.edit_redflags( redflag_id, column, column_data)
        return "Updated redflag's {}".format(column), 200
    return "not found", 404