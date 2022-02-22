import pydoc
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as k
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from exeterDomination.models import Users, Locations

def index(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/homePage.html", context)

def about(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/aboutPage.html", context)

def login(request : request) -> HttpResponse:
    if request.method == "GET":
        return render(request, "exeterDomination/loginPage.html", {})
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            k(request, user)
            print("LOGGED IN")
        else:
            return render(request, "exeterDomination/loginPage.html", {})
    return redirect(request, 'game')


def signup(request : request) -> HttpResponse:
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, "exeterDomination/signUpPage.html", context)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect(reverse('index'))
        else:
            print('Form is not valid')
            context = {'form': form}
            return render(request, 'exeterDomination/signUpPage.html', context)
    return render(request, "exeterDomination/signUpPage.html", {})


@login_required(login_url='/play/login')
def game(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/gamePage.html", context)


def leaderboard(request : request) -> HttpResponse:
    context = {'player_scores' : [['ExamplePlayerName', "100"], ], }
    return render(request, "exeterDomination/leaderboardPage.html", context)