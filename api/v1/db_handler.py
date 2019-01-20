""" module handling operations performed by the database """
from flask import make_response, current_app as app
from api.v1.models import Database

db = Database()
cursor = db.cur
dictcur = db.dict_cursor

class Redflags:
    """class to handle database operations on products"""

    def create_redflag(self, data):
        """ method to create redflags """
        query = "INSERT INTO redflags(created_by, incident_type, \
        location, status, image, comment) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(data['created_by'], \
        data['incident_type'], data['location'], data['status'], data['image'], data['comment'])
        cursor.execute(query)
        return self.check_redflag(data['created_by'], data['comment'])

    def get_redflags(self):
        """method that returns all redflag records"""
        query ="SELECT * FROM redflags"
        dictcur.execute(query)
        redflags = dictcur.fetchall()
        return redflags

    def get_specific_redflag(self, redflag_id):
        """method that returns a redflag by redflag_id"""
        query = "SELECT * FROM redflags WHERE redflag_id='{}'".format(redflag_id)
        dictcur.execute(query)
        specific_redflag = dictcur.fetchone()
        return specific_redflag

    def delete_redflag(self, redflag_id):
        """method to delete a redflag by redflag_id"""
        query = "DELETE FROM redflags WHERE redflag_id='{}'".format(redflag_id)
        del_redflag = cursor.execute(query)
        return del_redflag

    def edit_redflags(self, redflag_id, column, column_data):
        """method to edit redflag comment and location"""
        query = "UPDATE redflags SET {column}='{column_data}' WHERE redflag_id='{redflag_id}';"\
        .format(column=column, column_data=column_data, redflag_id=redflag_id)
        dictcur.execute(query)
        return dictcur

    @staticmethod
    def check_redflag(created_by, comment):
        """ method to check if a redflag already exists """
        query = "SELECT DISTINCT redflag_id, created_by, comment FROM redflags WHERE created_by='{}' AND comment='{}';" \
        .format(created_by, comment)
        dictcur.execute(query)
        data = dictcur.fetchone()
        return data


