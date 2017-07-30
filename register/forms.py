from django import forms

from .models import regdata

class RegDataForm(forms.ModelForm):

    class Meta:
        model = regdata
        fields = ('nama', 'email','tlp',)
