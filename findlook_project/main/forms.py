from dataclasses import fields
from email import message
import imp
from django import forms
from django.core import validators
from .models import UserSuggested, UserProfileInfo
from django.contrib.auth.models import User

def check_if_gmail(value):
    if value.split('@')[1] != 'gmail.com':
        raise forms.ValidationError("Only google mail.")

class SuggestionForm(forms.ModelForm):
    name = forms.CharField(required=False)
    email = forms.EmailField(validators=[check_if_gmail])
    message = forms.CharField(widget=forms.Textarea(
            attrs={'placeholder': 'Ваши предложения..'}))
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    class Meta:
        model = UserSuggested
        fields = '__all__'


class UserForm(forms.ModelForm):
    """Registration form for user"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None,
        }

class UserProfileInfoForm(forms.ModelForm):
    """Registration form for user"""
    class Meta:
        model = UserProfileInfo
        fields = ('instagramm_link', 'profile_pic')

class UserLoginForm(forms.Form):
    """Form for login page."""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    