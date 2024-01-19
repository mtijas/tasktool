from django.contrib.auth.models import Account
from django.test import TestCase
from django.utils.translation import gettext

from account.forms import AccountSettingsForm


class AccountSettingsFormTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = Account.objects.create_user(
            username='user1@foo.bar', password='topsecret'
        )

    def test_accountsettings_no_unexpected_errors(self):
        """Accountsettings should not have unexpected errors on minimum data"""
        data = {
            'selected_lang': 'en',
            'user': self.user1.id
        }

        form = AccountSettingsForm(data=data)

        self.assertEquals(form.errors, {})
