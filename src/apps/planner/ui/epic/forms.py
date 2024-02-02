from django import forms
from django.utils.translation import gettext_lazy as _

class EpicEditForm(forms.Form):
    title = forms.CharField(label=_('Title'), max_length=2048)
    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs={"rows":"5"}),
        required=False
    )
    themes = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        themes = kwargs.pop('themes', [])
        super(EpicEditForm, self).__init__(*args, **kwargs)
        self.fields['themes'].choices = themes
