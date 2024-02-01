from django import forms
from django.utils.translation import gettext_lazy as _

class StoryEditForm(forms.Form):
    title = forms.CharField(label=_('Title'), max_length=2048)
    epics = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        epics = kwargs.pop('epics', [])
        super(StoryEditForm, self).__init__(*args, **kwargs)
        self.fields['epics'].choices = epics
