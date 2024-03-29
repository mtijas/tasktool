from django import forms
from django.utils.translation import gettext_lazy as _

class TaskEditForm(forms.Form):
    title = forms.CharField(label=_('Title'), max_length=512)
    description = forms.CharField(label=_('Description'), widget=forms.Textarea(attrs={"rows":"5"}))
