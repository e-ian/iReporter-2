"""
module for validating inputs
"""

from flask import Flask, jsonify
import re
import datetime


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
