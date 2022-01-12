from django import forms
from django.core import validators

class SuggestionForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea(
            attrs={'placeholder': 'Ваши предложения..'}))
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

