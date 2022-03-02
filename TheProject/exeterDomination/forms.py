"""
forms.py
=======================================
This module contains the forms classes that enables us to display http forms on the 
frontend and pass data to the database when the forms ae sent to the server.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    """
    This class allows us to display a form that
    lets a user create an account.
    """

    username = forms.CharField(
        max_length=128,
        required=True,
        help_text='Username: ',
        widget=forms.TextInput(attrs={
            'name': 'username',
            'placeholder': 'Username'}))

    password1 = forms.CharField(
        help_text='Password: ',
        required=True,
        widget=forms.PasswordInput(attrs={
            'name': 'password',
            'placeholder': 'Password'
        }))

    password2 = forms.CharField(
        help_text='Re-Enter Password: ',
        required=True,
        widget=forms.PasswordInput(attrs={
            'name': 'psw-repeat',
            'placeholder': 'Repeat Password'
        }))


class Meta:
    """
    This class describes the Meta data of the forms.
    """
    
    fields = ['username', 'password1', 'password2']
