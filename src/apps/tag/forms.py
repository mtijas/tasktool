from django import forms
from django.utils.translation import gettext_lazy as _
from ..widgets import ColorInput

class TagEditForm(forms.Form):
    title = forms.CharField(label=_('Title'), max_length=512)
    background_color = forms.CharField(widget=ColorInput())
    text_color = forms.CharField(widget=ColorInput())
