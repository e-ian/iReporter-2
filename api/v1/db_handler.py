""" module handling operations performed by the database """
from flask import make_response, current_app as app
from api.v1.models import Database
from werkzeug.security import generate_password_hash, check_password_hash

db = Database()
cursor = db.cur
dictcur = db.dict_cursor

class Redflags:
    """class to handle database operations on redflags"""

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

class Interventions:
    """ class to handle database operations on interventions """
    def create_intervention(self, form_data):
        """ method to create an intervention record """
        command = "INSERT INTO interventions(created_by, incident_type, \
        location, status, image, comment) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(form_data['created_by'], \
        form_data['incident_type'], form_data['location'], form_data['status'], form_data['image'], form_data['comment'])
        cursor.execute(command)
        return self.check_intervention(form_data['created_by'], form_data['comment'])

    def get_interventions(self):
        """ method to get all interventions """
        command ="SELECT * FROM interventions"
        dictcur.execute(command)
        interventions = dictcur.fetchall()
        return interventions

    def get_single_intervention(self, intervention_id):
        """ method to get a specific intervention """
        command = "SELECT * FROM interventions WHERE intervention_id='{}'".format(intervention_id)
        dictcur.execute(command)
        single_intervention = dictcur.fetchone()
        return single_intervention

    def edit_interventions(self, intervention_id, column, column_data):
        """method to edit intervention status, comment and location"""
        command = "UPDATE interventions SET {column}='{column_data}' WHERE intervention_id='{intervention_id}';"\
        .format(column=column, column_data=column_data, intervention_id=intervention_id)
        dictcur.execute(command)
        return dictcur

    def delete_intervention(self, intervention_id):
        """method to delete an intervention by intervention_id"""
        command = "DELETE FROM interventions WHERE intervention_id='{}'".format(intervention_id)
        del_intervention = cursor.execute(command)
        return del_intervention

    @staticmethod
    def check_intervention(created_by, comment):
        """ method to check if an intervention record already exists """
        command = "SELECT DISTINCT intervention_id, created_by, comment FROM interventions WHERE created_by='{}' AND comment='{}';" \
        .format(created_by, comment)
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

class Users:
    """class handling all database operations on users"""

    def signup_user(self, data):
        """ method to register a new user """
        query = "INSERT INTO users(firstname, lastname, username, password, email, role) \
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(data['firstname'], data['lastname'], \
        data['username'], generate_password_hash(data['password']), data['email'], data['role'])
        cursor.execute(query)
        return data

    def signup_admin(self, data):
        """ method to register an admin """
        query = "INSERT INTO users(firstname, lastname, username, password, email, role) \
        VALUES('{}', '{}', '{}', '{}', '{}', 'admin')".format(data['firstname'], data['lastname'], \
        data['username'], generate_password_hash(data['password']), data['email'])
        cursor.execute(query)
        return data

    def login_user(self, data):
        """ method to login in registered users"""
        query = "SELECT * FROM users WHERE username='{}'".format(data['username'])
        dictcur.execute(query)
        login = dictcur.fetchone()
        return login

    @staticmethod
    def check_username(username):
        """ method to check if a username is already taken"""
        query = "SELECT * FROM users WHERE username='{}'".format(username)
        dictcur.execute(query)
        data = dictcur.fetchone()
        return data

    def verify_password(self, data, db_data):
        return check_password_hash(data, db_data)




