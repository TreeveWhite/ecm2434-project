"""
forms.py
=======================================
This module contains the forms classes that enables us to display http forms on the
frontend and pass data to the database when the forms ae sent to the server.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


def getMyChoices():
    """
    This function displays the list of team choices available at account
    creation
    """
    try:
        listOfList = []
        choices = Group.objects.exclude(name="Game Masters")
        for choice in choices:
            listOfList.append([choice.id, choice.name])

        my_tuple = tuple((tuple(i) for i in listOfList))
        return my_tuple
    except Exception:
        return ((0, "None"), (1, "Domination"))


class SignUpForm(UserCreationForm):
    """
    This class allows us to display a form that
    lets a user create an account.
    """

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        choices = Group.objects.exclude(name="Game Masters")
        self.fields['teamName'].choices = tuple([(c.id, c.name) for c in choices])
        if len(self.fields['teamName'].choices) == 0:
            self.fields['teamName'].choices = ((0, "None"),)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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

    teamName = forms.ChoiceField(widget=forms.Select, choices=getMyChoices())

class JoinTeamForm(forms.Form):
    """
    This class displays a form which allows the
    user to join a specified team
    """
    def __init__(self, *args, **kwargs):
        super(JoinTeamForm, self).__init__(*args, **kwargs)
        choices = Group.objects.exclude(name="Game Masters")
        self.fields['teamName'].choices = tuple([(c.id, c.name) for c in choices])
        if len(self.fields['teamName'].choices) == 0:
            self.fields['teamName'].choices = ((0, "None"))

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-select'

    try:
        teamName = forms.ChoiceField(widget=forms.Select, choices=getMyChoices())
    except Exception:
        teamName = forms.ChoiceField(widget=forms.Select, choices=((0, "None")))

class CreateTeamForm(forms.Form):
    """
    This class displays a form which allows the
    user to create their own team
    """
    teamName2 = forms.CharField(

            max_length=128,
            required=True,
            help_text='Team Name: ',
            widget=forms.TextInput(attrs={
                'name'       : 'teamName2',
                'placeholder': 'Team Name: '}))


    def __init__(self, *args, **kwargs) -> None:
        super(CreateTeamForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class Meta:
    """
    This class describes the Meta data of the forms.
    """

    fields = ['username', 'password1', 'password2', 'teamName', 'teamName2']
