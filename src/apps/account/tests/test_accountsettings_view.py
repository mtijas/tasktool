from django.contrib.auth.models import Account
from django.test import Client, TestCase
from django.urls import reverse


class AccountSettingsLoginsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = Account.objects.create_user(
            username='user1@foo.bar', password='topsecret'
        )

    def setUp(self):
        self.client = Client()

    def test_redirects_non_logged_in_to_login_on_view_page(self):
        """Non logged in accounts should get redirected to login page"""
        response = self.client.get(reverse("profile"))

        self.assertRedirects(
            response, f'/auth/login/?next={reverse("profile")}')

    def test_allows_logged_in_to_view_page(self):
        """Logged in user should be able to view the profile page"""
        self.client.login(username='user1@foo.bar', password='topsecret')
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 200)
