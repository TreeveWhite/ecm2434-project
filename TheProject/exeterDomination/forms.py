"""
forms.py
=======================================
This module contains the forms classes that enables us to display http forms on the
frontend and pass data to the database when the forms ae sent to the server.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


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
            'name'       : 'username',
            'placeholder': 'Username'}))

    password1 = forms.CharField(
        help_text='Password: ',
        required=True,
        widget=forms.PasswordInput(attrs={
            'name'       : 'password',
            'placeholder': 'Password'
        }))

    password2 = forms.CharField(
        help_text='Re-Enter Password: ',
        required=True,
        widget=forms.PasswordInput(attrs={
            'name'       : 'psw-repeat',
            'placeholder': 'Repeat Password'
        }))

    try:
        choices = Group.objects.exclude(name="Game Masters")
        for choice in choices:
            listOfList.append([choice.id, choice.name])

        my_tuple = tuple((tuple(i) for i in listOfList))

        teamName = forms.ChoiceField(widget=forms.Select, choices=my_tuple)
    except Exception:
        pass


class JoinTeamForm(forms.Form):
    choices = Group.objects.exclude(name="Game Masters")
    listOfList = []
    for choice in choices:
        listOfList.append([choice.id, choice.name])

    my_tuple = tuple((tuple(i) for i in listOfList))

    teamName = forms.ChoiceField(widget=forms.Select, choices=my_tuple)


class CreateTeamForm(forms.Form):
    teamName2 = forms.CharField(
            max_length=128,
            required=True,
            help_text='Team Name: ',
            widget=forms.TextInput(attrs={
                'name'       : 'teamName2',
                'placeholder': 'Team Name: '}))


class Meta:
    """
    This class describes the Meta data of the forms.
    """

    fields = ['username', 'password1', 'password2', 'teamName', 'teamName2']
