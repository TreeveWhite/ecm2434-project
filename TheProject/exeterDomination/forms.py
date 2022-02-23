from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
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

    fields = ['username', 'password1', 'password2']