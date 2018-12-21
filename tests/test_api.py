""" module tests_api """

import unittest
import json
from api.v1 import app
from api.v1.views import views
from api.v1.models.Redflags import Redflags
from . import (redflag, redflagempty, invalid_date, empty_list)

class TestUser(unittest.TestCase):
    """class for testing the API endpoints"""
    def setUp(self):
        """ 
        method that:
        sets up instance of app for the tests
        creates client to run the tests
        """
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
            response = client.post('/api/v1/redflags', data=json.dumps(redflag), \
            content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertIn("Created red-flag record", str(response.data))

    def test_empty_input_redflag(self):
        """ tests if one of the inputs of a redflag is empty """
        with self.client as client:
            response = client.post('/api/v1/redflags', data=json.dumps(redflagempty), \
            content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn("incidenttype, location, status or comment cannot have empty spaces", str(response.data))

    def test_invalid_date_format(self):
        """ tests the inputs of the date """
        with self.client as client:
            response = client.post('/api/v1/redflags', data=json.dumps(invalid_date), \
            content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn("Incorrect data format, should be YYYY-MM-DD", str(response.data))

    def test_get_all_redflags(self):
        """tests if all redflags can be fetched """
        with self.client as client:
            response = client.get('/api/v1/redflags')
            self.assertEqual(response.status_code, 200)

    # def test_no_redflags_posted(self):
    #     """ tests if no redflags have been posted yet """
    #     with self.client as client:
    #         client.post('/api/v1/redflags', data=json.dumps(empty_list), content_type='application/json')
    #         response = client.get('/api/v1/redflags')
    #         # self.assertEqual(response.status_code, 404)
    #         self.assertIn("No redflags have been posted yet", str(response.data))

    def test_get_specific_redflag(self):
        """ tests if a specific redflag can be fetched """
        with self.client as client:
            response = client.get('/api/v1/redflags/1')
            self.assertEqual(response.status_code, 200)

    def test_specific_redflag_not_found(self):
        """tests is a red flag cannot be got by flagid"""
        with self.client as client:
            client.post('/api/v1/redflags', json=dict(createdBy='emma', incidenttype='redflag', location='mulago', \
            status='resolved', Images='image', comment='bribe'))
            response = client.get('/api/v1/redflags/10000')
            self.assertIn("Redflag not found", str(response.data))

    

if __name__ == "__main__":
    unittest.main()