from django import forms
from django.utils.translation import gettext_lazy as _

class StoryEditForm(forms.Form):
    title = forms.CharField(label=_('Title'), max_length=2048)
