"""module base tests """
import unittest
import json
from api.v1 import app
from api.v1.db_handler import Redflags, Interventions
from config import TestingConfig
from api.v1.models import Database
import re
from tests import(redflag, empty_incident_type, empty_comment, empty_image, invalid_redflag, edit_redflag_location, \
edit_redflag_location_not_found, edit_invalid_redflag_location, edit_redflag_comment, edit_redflag_comment_not_found, \
edit_invalid_redflag_comment, edit_redflag_status, edit_redflag_status_not_found, edit_invalid_redflag_status)

app.config.from_object(TestingConfig)

db = Database()

class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.db = Database()

    def tearDown(self):
        self.db.cur.execute("DROP TABLE redflags CASCADE")
        self.db.cur.execute("DROP TABLE interventions CASCADE")
        self.db.cur.execute("DROP TABLE users CASCADE")

    def create_flag(self, redflag):
        response = self.client.post("/api/v1/redflags", \
        data=json.dumps(redflag), content_type='application/json')
        return response

    def empty_type(self, empty_incident_type):
        response = self.client.post("/api/v1/redflags", \
        data=json.dumps(empty_incident_type), content_type='application/json')
        return response

    def comment_empty(self, empty_comment):
        response = self.client.post("/api/v1/redflags", \
        data=json.dumps(empty_comment), content_type='application/json')
        return response

    def image_empty(self, empty_image):
        response = self.client.post("/api/v1/redflags", \
        data=json.dumps(empty_image), content_type='application/json')
        return response

    def duplicate_redflag(self, redflag):
        response = self.client.post("/api/v1/redflags", \
        data=json.dumps(redflag), content_type='application/json')
        return response

    def invalid_redflag(self, invalid_redflag):
        response = self.client.post("/api/v1/redflags", \
        data=json.dumps(invalid_redflag), content_type='application/json')
        return response

    def get_redflags(self):
        response = self.client.get("/api/v1/redflags")
        return response

    def get_single_redflag(self):
        response = self.client.get("/api/v1/redflags/1")
        return response

    def redflag_not_found(self):
        response = self.client.get("/api/v1/redflags/10000")
        return response

    def delete_redflag(self):
        response = self.client.delete("/api/v1/redflags/1")
        return response

    def edit_flag_location(self, edit_redflag_location):
        response = self.client.patch("/api/v1/redflags/1/location", \
        data=json.dumps(edit_redflag_location), content_type='application/json')
        return response

    def edit_flag_location_not_found(self, edit_redflag_location_not_found):
        response = self.client.patch("/api/v1/redflags/10000/location", \
        data=json.dumps(edit_redflag_location_not_found), content_type='application/json')
        return response

    def edit_invalid_flag_location(self, edit_invalid_redflag_location):
        response = self.client.patch("/api/v1/redflags/1/location", \
        data=json.dumps(edit_invalid_redflag_location), content_type='application/json')
        return response

    def edit_flag_comment(self, edit_redflag_comment):
        response = self.client.patch("/api/v1/redflags/1/comment", \
        data=json.dumps(edit_redflag_comment), content_type='application/json')
        return response

    def edit_flag_comment_not_found(self, edit_redflag_comment_not_found):
        response = self.client.patch("/api/v1/redflags/10000/comment", \
        data=json.dumps(edit_redflag_comment_not_found), content_type='application/json')
        return response

    def edit_invalid_flag_comment(self, edit_invalid_redflag_comment):
        response = self.client.patch("/api/v1/redflags/1/comment", \
        data=json.dumps(edit_invalid_redflag_comment), content_type='application/json')
        return response

    def edit_flag_status(self, edit_redflag_status):
        response = self.client.patch("/api/v1/redflags/1/status", \
        data=json.dumps(edit_redflag_status), content_type='application/json')
        return response

    def edit_flag_status_not_found(self, edit_redflag_status_not_found):
        response = self.client.patch("/api/v1/redflags/10000/status", \
        data=json.dumps(edit_redflag_status_not_found), content_type='application/json')
        return response

    def edit_invalid_flag_status(self, edit_invalid_redflag_status):
        response = self.client.patch("/api/v1/redflags/1/status", \
        data=json.dumps(edit_invalid_redflag_status), content_type='application/json')
        return response

    def home_route(self):
        response = self.client.get('/')
        return response

        


        

    