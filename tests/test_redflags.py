""" module tests_redflags """
from tests.base import TestUser
from . import(redflag, incident_type, empty_comment, empty_image, invalid_redflag, \
edit_redflag_location, edit_redflag_location_not_found, edit_invalid_redflag_location, \
edit_redflag_comment, edit_redflag_comment_not_found, edit_invalid_redflag_comment, edit_redflag_status, \
edit_redflag_status_not_found, edit_invalid_redflag_status, redflag_draft, empty_flag_location)

class TestApp(TestUser):

    def test_create_redflag(self):
        response = self.create_flag(redflag)
        self.assertIn("Created red-flag record", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_incident_type(self):
        response = self.empty_type(incident_type)
        self.assertIn('incident type can only be redflag', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_comment(self):
        response = self.comment_empty(empty_comment)
        self.assertIn('comment field should be a string and should contain alphabets', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_redflag_draft(self):
        response = self.redflag_draft(redflag_draft)
        self.assertIn('status can only be posted as a draft', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_flag_location(self):
        response = self.empty_flag_location(empty_flag_location)
        self.assertIn('location field cannot be empty', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_image(self):
        response = self.image_empty(empty_image)
        self.assertIn('The image field cannot be empty', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_duplicate_redflag(self):
        self.create_flag(redflag)
        response = self.duplicate_redflag(redflag)
        self.assertIn('Redflag record already exists', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_invalid_redflag(self):
        response = self.invalid_redflag(invalid_redflag)
        self.assertIn('Invalid input format', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_get_redflags(self):
        self.create_flag(redflag)
        response = self.get_redflags()
        self.assertEqual(response.status_code, 200)

    def test_get_single_redflag(self):
        self.create_flag(redflag)
        response = self.get_single_redflag()
        self.assertEqual(response.status_code, 200)

    def test_delete_redflag(self):
        self.create_flag(redflag)
        self.get_single_redflag()
        response = self.delete_redflag()
        self.assertIn('red-flag record has been deleted', str(response.data))
        self.assertEqual(response.status_code, 200)
    
    def test_deleted_redflag(self):
        self.get_single_redflag()
        response = self.delete_redflag()
        self.assertIn('Redflag doesnot exist', str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_redflag_location(self):
        self.create_flag(redflag)
        self.get_single_redflag()
        response = self.edit_flag_location(edit_redflag_location)
        self.assertIn("Updated redflags location", str(response.data))
        self.assertEqual(response.status_code, 200)
    
    def test_edit_redflag_location_not_found(self):
        response = self.edit_flag_location(edit_redflag_location_not_found)
        self.assertIn("Redflag not found in records", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_invalid_redflag_location(self):
        self.get_single_redflag()
        response = self.edit_invalid_flag_location(edit_invalid_redflag_location)
        self.assertIn("Please enter a valid key for location field as location", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_edit_redflag_comment(self):
        self.create_flag(redflag)
        self.get_single_redflag()
        response = self.edit_flag_comment(edit_redflag_comment)
        self.assertIn("Updated redflags comment", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_edit_redflag_comment_not_found(self):
        response = self.edit_flag_comment_not_found(edit_redflag_comment_not_found)
        self.assertIn("Redflag not found in records", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_invalid_redflag_comment(self):
        self.get_single_redflag()
        response = self.edit_invalid_flag_comment(edit_invalid_redflag_comment)
        self.assertIn("Please enter a valid key for comment field as comment", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_edit_redflag_status(self):
        self.create_flag(redflag)
        self.get_single_redflag()
        response = self.edit_flag_status(edit_redflag_status)
        self.assertIn("Updated redflags status", str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_edit_redflag_status_not_found(self):
        response = self.edit_flag_status_not_found(edit_redflag_status_not_found)
        self.assertIn("Redflag not found in records", str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_invalid_redflag_status(self):
        self.get_single_redflag()
        response = self.edit_invalid_flag_status(edit_invalid_redflag_status)
        self.assertIn("Please enter a valid key for status field as status", str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_home_route(self):
        response = self.home_route()
        self.assertIn('Welcome to iReporter', str(response.data))



