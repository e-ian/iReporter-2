""" module tests_api """

import unittest
import json
from api.v1 import app
from api.v1.views import views

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

if __name__ == "__main__":
    unittest.main()