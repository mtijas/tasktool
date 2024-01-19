from django.forms import ModelForm
from .models import AccountSettings

class AccountSettingsForm(ModelForm):
    class Meta:
        model = AccountSettings
        fields = [
            "selected_lang",
        ]

