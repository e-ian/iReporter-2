""" module handling operations performed by the database """
from flask import make_response, request, current_app as app
import re
from flask import Flask, jsonify
from api.v1.dbhandler import Database
from werkzeug.security import generate_password_hash, check_password_hash

db = Database()
cursor = db.cur
dictcur = db.dict_cursor


class Redflags():
    """class to handle Redflag model"""

    def create_redflag(self, data):
        """ method to create redflags """
        query = "INSERT INTO redflags(created_by, incident_type, \
        location, status, image, comment) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(
            data['created_by'],
            data['incident_type'],
            data['location'],
            data['status'],
            data['image'],
            data['comment'])
        cursor.execute(query)
        return self.check_redflag(data['created_by'], data['comment'])

    def get_redflags(self):
        """method that returns all redflag records"""
        query = "SELECT * FROM redflags"
        dictcur.execute(query)
        redflags = dictcur.fetchall()
        return redflags

    def get_specific_redflag(self, redflag_id):
        """method that returns a redflag by redflag_id"""
        query = "SELECT * FROM redflags WHERE redflag_id='{}'".format(
            redflag_id)
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

    def check_redflag(self, created_by, comment):
        """ method to check if a redflag already exists """
        query = "SELECT DISTINCT redflag_id, created_by, comment FROM redflags WHERE created_by='{}' AND comment='{}';" \
            .format(created_by, comment)
        dictcur.execute(query)
        data = dictcur.fetchone()
        return data
    
    def validate_if_redflag(self, incident_type):
        """ method to validate if the input incident type """
        incident_type = str(incident_type).lower()
        if incident_type not in ("redflag"):
            return False
        else:
            return True


class Interventions:
    """ class to handle Intervention model"""

    def create_intervention(self, form_data):
        """ method to create an intervention record """
        command = "INSERT INTO interventions(created_by, incident_type, \
        location, status, image, comment) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(
            form_data['created_by'],
            form_data['incident_type'],
            form_data['location'],
            form_data['status'],
            form_data['image'],
            form_data['comment'])
        cursor.execute(command)
        return self.check_intervention(
            form_data['created_by'], form_data['comment'])

    def get_interventions(self):
        """ method to get all interventions """
        command = "SELECT * FROM interventions"
        dictcur.execute(command)
        interventions = dictcur.fetchall()
        return interventions

    def get_single_intervention(self, intervention_id):
        """ method to get a specific intervention """
        command = "SELECT * FROM interventions WHERE intervention_id='{}'".format(
            intervention_id)
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
        command = "DELETE FROM interventions WHERE intervention_id='{}'".format(
            intervention_id)
        del_intervention = cursor.execute(command)
        return del_intervention

    def check_intervention(self, created_by, comment):
        """ method to check if an intervention record already exists """
        command = "SELECT DISTINCT intervention_id, created_by, comment \
        FROM interventions WHERE created_by='{}' AND comment='{}';".format(created_by, comment)
        dictcur.execute(command)
        data = dictcur.fetchone()
        return data

    def check_status(self, status):
        """method validating the status input"""
        status = str(status).lower()
        if status not in ("draft"):
            return False
        else:
            return True   

    def validate_incident_type(self, incident_type):
        """ method to validate if the input incident type """
        incident_type = str(incident_type).lower()
        if incident_type not in ("intervention"):
            return False
        else:
            return True

    def valid_comment(self, comment):
        """method validating the username input """
        return isinstance(comment, str) and re.search(r'[a-z]', str(comment))

    def validate_location(self, location):
        """ method to validate location inputs """
        if not location or location.isspace():
            return False
        else:
            return True

    def validate_image(self, image):
        """ method to validate image inputs """
        if not image or image.isspace():
            return False
        else:
            return True

class Users:
    """class handling the user model"""

    def signup_user(self, data):
        """ method to register a new user """
        query = "INSERT INTO users(firstname, lastname, username, password, email, role) \
        VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(
            data['firstname'], data['lastname'], data['username'], generate_password_hash(
                data['password']), data['email'], data['role'])
        cursor.execute(query)
        return data

    def signup_admin(self, data):
        """ method to register an admin """
        query = "INSERT INTO users(firstname, lastname, username, password, email, role) \
        VALUES('{}', '{}', '{}', '{}', '{}', 'admin')".format(
            data['firstname'], data['lastname'], data['username'], generate_password_hash(
                data['password']), data['email'])
        cursor.execute(query)
        return data

    def login_user(self, data):
        """ method to login in registered users"""
        query = "SELECT * FROM users WHERE username='{}'".format(
            data['username'])
        dictcur.execute(query)
        login = dictcur.fetchone()
        return login

    def check_username(self, username):
        """ method to check if a username is already taken"""
        query = "SELECT * FROM users WHERE username='{}'".format(username)
        dictcur.execute(query)
        data = dictcur.fetchone()
        return data

    def verify_password(self, data, db_data):
        return check_password_hash(data, db_data)

    def validate_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        else:
            return True

    def valid_password(self, password):
        """ method validating the password input """
        return isinstance(
            password,
            str) and len(password) >= 6 and re.search(
            r'[A-Z]',
            password) and re.search(
            r'[0-9]',
            password) and not re.search(
                r'\s',
            str(password))

    def valid_username(self, username):
        """method validating the username input """
        return isinstance(
            username,
            str) and len(username) >= 3 and not re.search(
            r'\s',
            str(username)) and not re.search(
            r'\W',
            str(username))

    def valid_firstname(self, firstname):
        """method validating the username input """
        return isinstance(
            firstname,
            str) and len(firstname) >= 3 and not re.search(
            r'\s',
            str(firstname)) and not re.search(
            r'\W',
            str(firstname))

    def valid_lastname(self, lastname):
        """method validating the username input """
        return isinstance(
            lastname,
            str) and len(lastname) >= 3 and not re.search(
            r'\s',
            str(lastname)) and not re.search(
            r'\W',
            str(lastname))

    def valid_role(self, role):
        """method validating the role"""
        role = str(role).lower()
        if role not in ("admin", "user"):
            return False
        else:
            return True
