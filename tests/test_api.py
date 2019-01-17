""" module tests_api """

import unittest
import json
from api.v1 import app
from api.v1.views import views
from api.v1.models.Redflags import Redflags
from api.v1.models.users import Users
from . import (
    redflag,
    redflagempty,
    invalid_date,
    empty_list,
    redflag_comment,
    empty_incident_type,
    empty_image,
    redflag_draft,
    edit_comment)


class TestUser(unittest.TestCase):
    """class for testing the API endpoints"""

    def setUp(self):
        """
        method that:
        sets up instance of app for the tests
        creates client to run the tests
        """
        kwargs = {
            'created_On': '2018-12-19',
            'created_By': 'emma',
            'incident_Type': 'redflag',
            'location': 'mulago',
            'status': 'resolved',
            'images': 'images',
            'comment': 'bribery in OPM'
        }
        self.redflags = Redflags(**kwargs)
        kwargs = {
            'first_name': 'emma',
            'last_name': 'ogwal',
            'email': 'ogwal@hotmail.com',
            'phone_number': '772903077',
            'user_name': 'eogwal',
            'role': 'admin',
            'password': 'akokorodrift'
        }
        self.users = Users(**kwargs)
        self.client = app.test_client()

    def test_home(self):
        """ tests default home route """
        with self.client as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Welcome to iReporter', str(response.data))

    def test_create_redflag(self):
        """ tests if a redflag has been created """
        with self.client as client:
            response = client.post(
                '/api/v1/redflags',
                data=json.dumps(redflag),
                content_type='application/json')
            self.assertEqual(response.status_code, 201)
            self.assertIn("Created red-flag record", str(response.data))

    def test_empty_input_redflag(self):
        """ tests if one of the inputs of a redflag is empty """
        with self.client as client:
            response = client.post(
                '/api/v1/redflags',
                data=json.dumps(redflagempty),
                content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                "comment and location fields cannot be empty and comment takes alphabets", str(
                    response.data))

    def test_invalid_date_format(self):
        """ tests the inputs of the date """
        with self.client as client:
            response = client.post(
                '/api/v1/redflags',
                data=json.dumps(invalid_date),
                content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                "Incorrect date format, should be YYYY-MM-DD", str(response.data))

    def test_get_all_redflags(self):
        """tests if all redflags can be fetched """
        with self.client as client:
            response = client.get('/api/v1/redflags')
            self.assertEqual(response.status_code, 200)

    def test_get_specific_redflag(self):
        """ tests if a specific redflag can be fetched """
        with self.client as client:
            response = client.get('/api/v1/redflags/1')
            self.assertEqual(response.status_code, 200)

    def test_specific_redflag_not_found(self):
        """tests is a red flag cannot be got by flagid"""
        with self.client as client:
            client.post(
                '/api/v1/redflags',
                json=dict(
                    created_By='emma',
                    incident_Type='redflag',
                    location='mulago',
                    status='resolved',
                    images='image',
                    comment='bribe'))
            response = client.get('/api/v1/redflags/10000')
            self.assertIn("Redflag not found", str(response.data))

    def test_edit_redflag_location(self):
        """ tests for editing location """
        with self.client as client:
            client.post(
                'api/v1/redflags',
                data=json.dumps(redflag),
                content_type='application/json')
            response = client.patch(
                '/api/v1/redflags/1/location',
                json=dict(
                    location='kampala'))
            self.assertEqual(response.status_code, 200)

    def test_edit_location_not_found(self):
        """ tests if the flagid doesnot exit when editing location """
        with self.client as client:
            response = client.patch(
                '/api/v1/redflags/0/location',
                json=dict(
                    location='kampala'))
            self.assertIn('Redflag not found', str(response.data))

    def test_edit_redflag_comment(self):
        """ tests for editing comment"""
        with self.client as client:
            client.post(
                '/api/v1/redflags',
                data=json.dumps(edit_comment),
                content_type='application/json')
            response = client.patch(
                '/api/v1/redflags/1/comment',
                json=dict(
                    comment='bribery in OPM'))
            self.assertEqual(response.status_code, 200)

    def test_edit_comment_not_found(self):
        """ tests if the flagid doesnot exit when editing comment """
        with self.client as client:
            client.post(
                '/api/v1/redflags',
                data=json.dumps(redflag),
                content_type='application/json')
            response = client.patch(
                'api/v1/redflags/0/comment',
                json=dict(
                    comment='bribery'))
            self.assertIn('Redflag not found', str(response.data))

    def test_deleted_red_flag(self):
        """ tests if a red flag has been deleted """
        with self.client as client:
            response = client.delete('api/v1/redflags/1')
            self.assertEqual(response.status_code, 200)

    def test_deleted_red_flag_does_not_exist(self):
        """ tests whether a user cannot delete the same redflag twice """
        with self.client as client:
            response = client.delete('api/v1/redflags/0')
            self.assertIn('Redflag doesnot exist', str(response.data))

    def test_incident_type(self):
        """ tests if incident type is not empty """
        with self.client as client:
            response = client.post(
                "api/v1/redflags",
                data=json.dumps(empty_incident_type),
                content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'incident_Type or status cannot have empty spaces', str(
                    response.data))

    def test_empty_image(self):
        """ tets if image field is not empty """
        with self.client as client:
            response = client.post(
                "api/v1/redflags",
                data=json.dumps(empty_image),
                content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                'The status and image fields cannot be empty', str(
                    response.data))

    def test_edit_comment_payload(self):
        """ tests for payload data of edit comment """
        with self.client as client:
            client.post(
                '/api/v1/redflags',
                data=json.dumps(redflag),
                content_type='application/json')
            response = client.patch(
                '/api/v1/redflags/1/comment',
                json=dict(
                    comment='bribery in OPM'))
            response_data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response_data, dict)


if __name__ == "__main__":
    unittest.main()
