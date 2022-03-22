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

    def __init__(self, *args, **kwargs) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class JoinTeamForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(JoinTeamForm, self).__init__(*args, **kwargs)
        choices = Group.objects.exclude(name="Game Masters")
        self.fields['teamName'].choices = tuple([(c.id, c.name) for c in choices])
        if len(self.fields['teamName'].choices) == 0:
            self.fields['teamName'].choices = ((0, "None"))
    try:
        teamName = forms.ChoiceField(widget=forms.Select, choices=getMyChoices())
    except Exception:
        teamName = forms.ChoiceField(widget=forms.Select, choices=((0, "None")))

    def __init__(self, *args, **kwargs) -> None:
        super(JoinTeamForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-select'


class CreateTeamForm(forms.Form):
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
