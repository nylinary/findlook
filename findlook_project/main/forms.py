from django import forms
from django.core import validators


def check_if_gmail(value):
    if value.split('@')[1] != 'gmail.com':
        raise forms.ValidationError("Only google mail.")

class SuggestionForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(validators=[check_if_gmail])
    text = forms.CharField(widget=forms.Textarea(
            attrs={'placeholder': 'Ваши предложения..'}))
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

