""" module tests_interventions """
from tests.base import TestUser
from . import(
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
    post_as_draft,
    empty_int_location)


class TestApp(TestUser):

    def test_create_intervention(self):
        response = self.create_intervention(intervention)
        self.assertIn("Created intervention record", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_incident_type(self):
        response = self.incident_type(incident_type)
        self.assertIn(
            'incident type can only be intervention', str(
                response.data))
        self.assertEqual(response.status_code, 400)

    def test_post_draft(self):
        response = self.post_as_draft(post_as_draft)
        self.assertIn(
            'status can only be posted as a draft', str(
                response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_comment(self):
        response = self.int_comment_empty(empty_comment_int)
        self.assertIn(
            'comment field should be a string and should contain alphabets', str(
                response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_int_location(self):
        response = self.empty_int_location(empty_int_location)
        self.assertIn('location field cannot be empty', str(response.data))
        self.assertEqual(response.status_code, 400)

    def test_empty_image(self):
        response = self.int_image_empty(empty_image_int)
        self.assertIn('The image field cannot be empty', str(response.data))
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
        self.assertIn(
            'Intervention record has been deleted', str(
                response.data))
        self.assertEqual(response.status_code, 200)

    def test_deleted_intervention(self):
        self.get_single_intervention()
        response = self.delete_intervention()
        self.assertIn('intervention doesnot exist', str(response.data))
        self.assertEqual(response.status_code, 404)

    def test_edit_int_location(self):
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
        self.assertIn(
            "Please enter a valid key for location field as location", str(
                response.data))
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
        self.assertIn(
            "Please enter a valid key for comment field as comment", str(
                response.data))
        self.assertEqual(response.status_code, 400)

    def test_edit_int_status_not_found(self):
        response = self.edit_int_status_not_found(edit_int_status)
        self.assertIn("Intervention record not found", str(response.data))
        self.assertEqual(response.status_code, 404)

