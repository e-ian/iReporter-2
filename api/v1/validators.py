"""
module for validating inputs
"""

from flask import Flask, jsonify
import re
import datetime

class Validators:

    @staticmethod
    def validate_input_string(incidenttype, location, status, comment):
        """ method to validate if the input is a string and not empty """
        if not incidenttype or not location or not status or not comment:
            return False
        else:
            return True

    @staticmethod
    def validate_date_created(createdOn):
        """method to validate the date a record was created"""
        try:
            datetime.datetime.strptime(createdOn, '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Incorrect data format, should be YYYY-MM-DD'}), 400


        
