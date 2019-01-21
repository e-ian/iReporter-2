"""
module for validating inputs
"""

from flask import Flask, jsonify
import re

class Validators:

    @staticmethod
    def validate_input_string(incident_type, status):
        """ method to validate if the input is a string and not empty """
        if not incident_type or not status:
            return False
        else:
            return True

    @staticmethod
    def validate_comment_and_location(comment, location):
        """ method to validate comment and location inputs """
        if not comment or not location or comment.isspace(
        ) or location.isspace() or not isinstance(comment, str):
            return False
        else:
            return True

    @staticmethod
    def validate_status_and_image(status, image):
        """ method to validate status and image inputs """
        if not status or not image or status.isspace() or image.isspace():
            return False
        else:
            return True

    @staticmethod
    def validate_inputs(input_str):
        """method validating if the input is a string """
        if re.search(r'\s', str(input_str)):
            return jsonify({'error': 'Input field cannot have empty spaces'}), 400
        if re.search(r'\W', str(input_str)):
            return jsonify({'error': 'Input field should have alphabets only'}), 400
        if re.search(r'\d', str(input_str)):
            return jsonify({'error': 'Input field doesnot take digits but letters'}), 400

    @staticmethod
    def valid_password(password):
        """ method validating the password input """
        if not len(password) >= 6:
            return jsonify({'error': 'Password should be greater or equal to six characters'}), 400
        if not re.search(r"^[a-zA-Z0-9]+$", password):
            return jsonify({'error': 'password should contain alphanumeric characters'}), 400
    @staticmethod
    def validate_email(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return jsonify({'error': 'email should be in the form someone@example.com'})
