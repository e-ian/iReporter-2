""" module tests_users """
from tests.base import TestUser
from . import(create_admin, login_admin, create_user, login_user, invalid_username, invalid_firstname, invalid_lastname, \
invalid_password, invalid_email, invalid_role)

class TestApp(TestUser):

    def test_register_admin(self):
        response = self.register_admin(create_admin)
        self.assertIn("Admin registered successfully", str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_signup_user(self):
        response = self.signup_user(create_user)
        self.assertIn("User registered successfully", str(response.data))

    def test_user_login(self):
        self.signup_user(create_user)
        response = self.login_user()
        self.assertEqual(response['status'], 200)

    def test_invalid_firstname(self):
        response = self.invalid_firstname(invalid_firstname)
        self.assertEqual(response.status_code, 400)

    def test_invalid_lastname(self):
        response = self.invalid_lastname(invalid_lastname)
        self.assertEqual(response.status_code, 400)

    def test_invalid_username(self):
        response = self.invalid_username(invalid_username)
        self.assertEqual(response.status_code, 400)

    def test_invalid_role(self):
        response = self.invalid_role(invalid_role)
        self.assertEqual(response.status_code, 400)

