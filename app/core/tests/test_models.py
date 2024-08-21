"""
Tests for models.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailzed(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@eXampLE.com', 'test1@example.com'],
            ['Test2@EXAMpLE.com', 'Test2@example.com'],
            ['TEST3@EXAMpLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """New user with no password raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test that super user gets created"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
