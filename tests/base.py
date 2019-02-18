"""module base tests """
import unittest
import json
from api.v1 import app
from api.v1.models import Redflags, Interventions
from config import TestingConfig
from api.v1.models import Database
from tests import(
    redflag,
    empty_comment,
    empty_image,
    invalid_redflag,
    edit_redflag_location,
    edit_redflag_location_not_found,
    edit_invalid_redflag_location,
    edit_redflag_comment,
    edit_redflag_comment_not_found,
    edit_invalid_redflag_comment,
    edit_redflag_status,
    edit_redflag_status_not_found,
    edit_invalid_redflag_status,
    intervention,
    incident_type,
    empty_comment_int,
    empty_image_int,
    invalid_intervention,
    edit_int_location,
    edit_invalid_int_location,
    edit_int_comment,
    edit_invalid_int_comment,
    edit_int_status,
    edit_invalid_int_status,
    login_admin,
    create_admin,
    create_user,
    login_user,
    invalid_username,
    invalid_firstname,
    invalid_lastname,
    invalid_password,
    invalid_email,
    invalid_role,
    post_as_draft,
    empty_int_location,
    redflag_draft, empty_flag_location)

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

    """ base tests for redflags """

    def create_flag(self, redflag):
        response = self.client.post(
            "/api/v1/redflags",
            data=json.dumps(redflag),
            content_type='application/json', headers=self.user_header())
        return response

    def empty_type(self, empty_incident_type):
        response = self.client.post(
            "/api/v1/redflags",
            data=json.dumps(empty_incident_type),
            content_type='application/json', headers=self.user_header())
        return response

    def redflag_draft(self, redflag_draft):
        response = self.client.post(
            "/api/v1/redflags",
            data=json.dumps(redflag_draft),
            content_type='application/json', headers=self.user_header())
        return response

    def comment_empty(self, empty_comment):
        response = self.client.post(
            "/api/v1/redflags",
            data=json.dumps(empty_comment),
            content_type='application/json', headers=self.user_header())
        return response

    def empty_flag_location(self, empty_flag_location):
        response = self.client.post(
            "/api/v1/redflags",
            data=json.dumps(empty_flag_location),
            content_type='application/json', headers=self.user_header())
        return response

    def image_empty(self, empty_image):
        response = self.client.post(
            "/api/v1/redflags",
            data=json.dumps(empty_image),
            content_type='application/json', headers=self.user_header())
        return response

    def duplicate_redflag(self, redflag):
        response = self.client.post(
            "/api/v1/redflags",
            data=json.dumps(redflag),
            content_type='application/json', headers=self.user_header())
        return response

    def invalid_redflag(self, invalid_redflag):
        response = self.client.post(
            "/api/v1/redflags",
            data=json.dumps(invalid_redflag),
            content_type='application/json', headers=self.user_header())
        return response

    def get_redflags(self):
        response = self.client.get(
            "/api/v1/redflags",
            headers=self.user_header())
        return response

    def get_single_redflag(self):
        response = self.client.get(
            "/api/v1/redflags/1",
            headers=self.user_header())
        return response

    def redflag_not_found(self):
        response = self.client.get(
            "/api/v1/redflags/10000",
            headers=self.user_header())
        return response

    def delete_redflag(self):
        response = self.client.delete(
            "/api/v1/redflags/1",
            headers=self.user_header())
        return response

    def edit_flag_location(self, edit_redflag_location):
        response = self.client.patch(
            "/api/v1/redflags/1/location",
            data=json.dumps(edit_redflag_location),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_flag_location_not_found(self, edit_redflag_location_not_found):
        response = self.client.patch(
            "/api/v1/redflags/10000/location",
            data=json.dumps(edit_redflag_location_not_found),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_invalid_flag_location(self, edit_invalid_redflag_location):
        response = self.client.patch(
            "/api/v1/redflags/1/location",
            data=json.dumps(edit_invalid_redflag_location),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_flag_comment(self, edit_redflag_comment):
        response = self.client.patch(
            "/api/v1/redflags/1/comment",
            data=json.dumps(edit_redflag_comment),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_flag_comment_not_found(self, edit_redflag_comment_not_found):
        response = self.client.patch(
            "/api/v1/redflags/10000/comment",
            data=json.dumps(edit_redflag_comment_not_found),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_invalid_flag_comment(self, edit_invalid_redflag_comment):
        response = self.client.patch(
            "/api/v1/redflags/1/comment",
            data=json.dumps(edit_invalid_redflag_comment),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_flag_status(self, edit_redflag_status):
        response = self.client.patch(
            "/api/v1/redflags/1/status",
            data=json.dumps(edit_redflag_status),
            content_type='application/json',
            headers=self.admin_header())
        return response

    def edit_flag_status_not_found(self, edit_redflag_status_not_found):
        response = self.client.patch(
            "/api/v1/redflags/10000/status",
            data=json.dumps(edit_redflag_status_not_found),
            content_type='application/json',
            headers=self.admin_header())
        return response

    def edit_invalid_flag_status(self, edit_invalid_redflag_status):
        response = self.client.patch(
            "/api/v1/redflags/1/status",
            data=json.dumps(edit_invalid_redflag_status),
            content_type='application/json',
            headers=self.admin_header())
        return response

    def home_route(self):
        response = self.client.get('/')
        return response

    """ base tests for interventions """

    def create_intervention(self, intervention):
        response = self.client.post(
            "/api/v1/interventions", content_type='application/json',
            data=json.dumps(intervention), headers=self.user_header())
        return response

    def incident_type(self, empty_incident_type):
        response = self.client.post(
            "/api/v1/interventions",
            data=json.dumps(empty_incident_type),
            content_type='application/json', headers=self.user_header())
        return response

    def post_as_draft(self, post_as_draft):
        response = self.client.post(
            "/api/v1/interventions",
            data=json.dumps(post_as_draft),
            content_type='application/json', headers=self.user_header())
        return response

    def empty_int_location(self, empty_int_location):
        response = self.client.post(
            "/api/v1/interventions",
            data=json.dumps(empty_int_location),
            content_type='application/json', headers=self.user_header())
        return response

    def int_comment_empty(self, empty_comment_int):
        response = self.client.post(
            "/api/v1/interventions",
            data=json.dumps(empty_comment_int),
            content_type='application/json', headers=self.user_header())
        return response

    def int_image_empty(self, empty_image_int):
        response = self.client.post(
            "/api/v1/interventions",
            data=json.dumps(empty_image_int),
            content_type='application/json', headers=self.user_header())
        return response

    def duplicate_intervention(self, intervention):
        response = self.client.post(
            "/api/v1/interventions",
            data=json.dumps(intervention),
            content_type='application/json', headers=self.user_header())
        return response

    def invalid_intervention(self, invalid_intervention):
        response = self.client.post(
            "/api/v1/interventions",
            data=json.dumps(invalid_intervention),
            content_type='application/json', headers=self.user_header())
        return response

    def get_interventions(self):
        response = self.client.get(
            "/api/v1/interventions",
            headers=self.user_header())
        return response

    def get_single_intervention(self):
        response = self.client.get(
            "/api/v1/interventions/1",
            headers=self.user_header())
        return response

    def intervention_not_found(self):
        response = self.client.get(
            "/api/v1/interventions/10000",
            headers=self.user_header())
        return response

    def delete_intervention(self):
        response = self.client.delete(
            "/api/v1/interventions/1",
            headers=self.user_header())
        return response

    def edit_int_location(self, edit_int_location):
        response = self.client.patch(
            "/api/v1/interventions/1/location",
            data=json.dumps(edit_int_location),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_int_location_not_found(self, edit_int_location):
        response = self.client.patch(
            "/api/v1/interventions/10000/location",
            data=json.dumps(edit_int_location),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_invalid_int_location(self, edit_invalid_int_location):
        response = self.client.patch(
            "/api/v1/interventions/1/location",
            data=json.dumps(edit_invalid_int_location),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_int_comment(self, edit_int_comment):
        response = self.client.patch(
            "/api/v1/interventions/1/comment",
            data=json.dumps(edit_int_comment),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_int_comment_not_found(self, edit_int_comment):
        response = self.client.patch(
            "/api/v1/interventions/10000/comment",
            data=json.dumps(edit_int_comment),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_invalid_int_comment(self, edit_invalid_int_comment):
        response = self.client.patch(
            "/api/v1/interventions/1/comment",
            data=json.dumps(edit_invalid_int_comment),
            content_type='application/json', headers=self.user_header())
        return response

    def edit_int_status(self, edit_int_status):
        response = self.client.patch(
            "/api/v1/interventions/1/status",
            data=json.dumps(edit_int_status),
            content_type='application/json', headers=self.admin_header())
        return response

    def edit_int_status_not_found(self, edit_int_status):
        response = self.client.patch(
            "/api/v1/interventions/10000/status",
            data=json.dumps(edit_int_status),
            content_type='application/json',
            headers=self.admin_header())
        return response

    def edit_invalid_int_status(self, edit_invalid_int_status):
        response = self.client.patch(
            "/api/v1/interventions/1/status",
            data=json.dumps(edit_invalid_int_status),
            content_type='application/json', headers=self.admin_header())
        return response

    """ base tests for users """

    def register_admin(self, create_admin):
        response = self.client.post(
            "/api/v1/auth/admin",
            data=json.dumps(create_admin),
            content_type='application/json')
        return response

    def signin_admin(self):
        self.register_admin(create_admin)
        response = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(login_admin),
            content_type='application/json')
        message = json.loads(response.data.decode())
        return message

    def admin_header(self):
        return{'content_type': 'application/json', 'Authorization': self.signin_admin()['access_token']}

    def signup_user(self, create_user):
        response = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(create_user),
            content_type='application/json')
        return response

    def login_user(self):
        self.signup_user(create_user)
        response = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(login_user),
            content_type='application/json')
        data = json.loads(response.data.decode())
        return data

    def user_header(self):
        return{'content_type': 'application/json', 'Authorization': "Bearer " +self.login_user()['access_token']}

    def invalid_firstname(self, invalid_firstname):
        response = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(invalid_firstname),
            content_type='application/json')
        return response

    def invalid_lastname(self, invalid_lastname):
        response = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(invalid_lastname),
            content_type='application/json')
        return response

    def invalid_username(self, invalid_username):
        response = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(invalid_username),
            content_type='application/json')
        return response

    def invalid_role(self, invalid_role):
        response = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(invalid_role),
            content_type='application/json')
        return response
