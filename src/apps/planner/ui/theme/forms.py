from django import forms
from django.utils.translation import gettext_lazy as _

class ThemeEditForm(forms.Form):
    title = forms.CharField(label=_('Title'), max_length=2048)
    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs={"rows":"5"}),
        required=False
    )
