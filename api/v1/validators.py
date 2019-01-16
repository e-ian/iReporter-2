"""
module for validating inputs
"""

from flask import Flask, jsonify
import re
import datetime

class Validators:

    @staticmethod
    def validate_input_string(incidenttype, status):
        """ method to validate if the input is a string and not empty """
        if not incidenttype or not status:
            return False
        else:
            return True

    @staticmethod
    def validate_date_created(createdOn):
        """method to validate the date a record was created"""
        try:
            datetime.datetime.strptime(createdOn, '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Incorrect date format, should be YYYY-MM-DD'}), 400

    @staticmethod
    def validate_comment_and_location(comment, location):
        """ method to validate comment and location inputs """
        if not comment or not location or comment.isspace() or location.isspace() \
        or not isinstance(comment, str):
            return False
        else:
            return True

    @staticmethod
    def validate_status_and_image(status, images):
        """ method to validate status and image inputs """
        if not status or not images or status.isspace() or images.isspace():
            return False
        else:
            return True
        

        
