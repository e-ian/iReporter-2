""" module tests_api """

import unittest
import json
from api.v1 import app
from api.v1.views import views
from api.v1.models.redflags import Redflags

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

    def test_create_redflag(self):
        """ tests if a redflag has been created """

        redflag = {
            'createdOn' : '2018-12-19',
            'createdBy' : 'emma',
            'incidenttype' : 'redflag',
            'location' : 'mulago',
            'status' : 'resolved',
            'Images' : 'Images',
            'comment' :'bribery in OPM'}

        with self.client as client:
            response = client.post('/api/v1/redflags', data=json.dumps(redflag), \
            content_type='application/json')
            self.assertEqual(response.status_code, 200)

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





if __name__ == "__main__":
    unittest.main()