""" module tests_interventions """
from tests.base import TestUser
from . import(intervention, empty_incident_type, empty_comment_int, empty_image_int, invalid_intervention, \
edit_int_location, edit_invalid_int_location, edit_int_comment, edit_invalid_int_comment, edit_int_status, \
edit_invalid_int_status)

class TestApp(TestUser):

    def test_create_intervention(self):
        response = self.create_intervention(intervention)
        self.assertIn("Created intervention record", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_empty_incident_type(self):
        response = self.empty_incident_type(empty_incident_type)
        self.assertIn('incident_type or status cannot have empty spaces', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_comment(self):
        response = self.int_comment_empty(empty_comment_int)
        self.assertIn('comment and location fields cannot be empty and comment takes alphabets', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_image(self):
        response = self.int_image_empty(empty_image_int)
        self.assertIn('The status and image fields cannot be empty', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_duplicate_intervention(self):
        self.create_intervention(intervention)
        response = self.duplicate_intervention(intervention)
        self.assertIn('Intervention record already exists', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_invalid_intervention(self):
        response = self.invalid_intervention(invalid_intervention)
        self.assertIn('Invalid input format', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_get_interventions(self):
        self.create_intervention(intervention)
        response = self.get_interventions()
        self.assertEqual(response.status_code, 200)

    def test_get_single_intervention(self):
        self.create_intervention(intervention)
        response = self.get_single_intervention()
        self.assertEqual(response.status_code, 200)

    def test_delete_interventions(self):
        self.create_intervention(intervention)
        self.get_single_intervention()
        response = self.delete_intervention()
        self.assertIn('Intervention record has been deleted', str(response.data))
        self.assertEqual(response.status_code, 200)
    
    def test_deleted_intervention(self):
        self.get_single_intervention()
        response = self.delete_intervention()
        self.assertIn('intervention doesnot exist', str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_redflag_location(self):
        self.create_intervention(intervention)
        self.get_single_intervention()
        response = self.edit_int_location(edit_int_location)
        self.assertIn("Updated interventions location", str(response.data))
        self.assertEqual(response.status_code, 200)
    
    def test_edit_int_location_not_found(self):
        response = self.edit_int_location(edit_int_location)
        self.assertIn("Intervention record not found", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_invalid_int_location(self):
        self.get_single_intervention()
        response = self.edit_invalid_int_location(edit_invalid_int_location)
        self.assertIn("Please enter a valid key for location field as location", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_edit_int_comment(self):
        self.create_intervention(intervention)
        self.get_single_intervention()
        response = self.edit_int_comment(edit_int_comment)
        self.assertIn("Updated interventions comment", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_edit_int_comment_not_found(self):
        response = self.edit_int_comment_not_found(edit_int_comment)
        self.assertIn("Intervention record not found", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_invalid_int_comment(self):
        self.get_single_intervention()
        response = self.edit_invalid_int_comment(edit_invalid_int_comment)
        self.assertIn("Please enter a valid key for comment field as comment", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_edit_int_status(self):
        self.create_intervention(intervention)
        self.get_single_intervention()
        response = self.edit_int_status(edit_int_status)
        self.assertIn("Updated interventions status", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_edit_int_status_not_found(self):
        response = self.edit_int_status_not_found(edit_int_status)
        self.assertIn("Intervention record not found", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_invalid_int_status(self):
        self.get_single_intervention()
        response = self.edit_invalid_int_status(edit_invalid_int_status)
        self.assertIn("Please enter a valid key for status field as status", str(response.data))
        self.assertEqual(response.status_code, 400)