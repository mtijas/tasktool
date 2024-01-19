from django.contrib.auth.models import Account
from django.test import Client, TestCase
from django.urls import reverse

from account.models import AccountSettings


class AccountSettingsLoginsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = Account.objects.create_user(
            username='user1@foo.bar', password='topsecret'
        )
        cls.settings1 = AccountSettings.objects.create(
            user = cls.user1
        )

    def setUp(self):
        self.client = Client()

    def test_redirects_non_logged_in_to_login_on_view_page(self):
        """Non logged in accounts should get redirected to login page"""
        response = self.client.get(reverse('accountsettingsedit'))

        self.assertRedirects(
            response, f'/auth/login/?next={reverse('accountsettingsedit')}')

    def test_allows_logged_in_to_view_page(self):
        """Logged in user should be able to view the accountsettingsedit page"""
        self.client.login(username='user1@foo.bar', password='topsecret')
        response = self.client.get(reverse('accountsettingsedit'))

        self.assertEqual(response.status_code, 200)

    def test_non_logged_in_user_is_forbidden_from_post_update(self):
        """Not logged in user should be forbidden to POST update form"""
        data = {
            'selected_lang': 'en',
            'user': self.user1.id
        }

        response = self.client.post(
            reverse('accountsettingsedit'),
            data=data
        )

        self.assertRedirects(
            response, f'/auth/login/?next={reverse('accountsettingsedit')}')
        accountsettings = AccountSettings.objects.get(id=self.settings1.id)
        self.assertEquals(accountsettings.calendar_default_timespan_weeks, self.settings1.calendar_default_timespan_weeks)

    def test_logged_in_user_is_allowed_to_update_settings(self):
        """Logged in user should be able to update settings"""
        data = {
            'selected_lang': 'en',
            'user': self.user1.id
        }

        self.client.login(username='user1@foo.bar', password='topsecret')

        response = self.client.post(
            reverse('accountsettingsedit'),
            data=data
        )

        self.assertRedirects(response, reverse('profile'))
        accountsettings = AccountSettings.objects.get(id=self.settings1.id)
        self.assertEquals(accountsettings.selected_lang, data['selected_lang'])

