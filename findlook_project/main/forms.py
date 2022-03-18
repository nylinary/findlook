from dataclasses import fields
from email import message
import imp
from django import forms
from django.core import validators
from .models import UserSuggested, UserProfileInfo
from django.contrib.auth.models import User

def check_if_gmail(value):
    try:
        if value.split('@')[1] != 'gmail.com':
            raise forms.ValidationError("Only google mail.")
    except Exception:
        raise forms.ValidationError("Enter email")

class SuggestionForm(forms.ModelForm):
    name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'TextInput NameInput pl-1'}))
    email = forms.EmailField(label='Почта', validators=[check_if_gmail],
                             widget=forms.TextInput(attrs={'class':'TextInput EmailInput pl-1'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(
            attrs={'class': 'TextInput TextareaInput pl-1'}))
    
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)]),
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
    