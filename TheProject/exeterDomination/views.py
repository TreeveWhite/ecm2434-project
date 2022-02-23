import pydoc
from urllib import request
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as k
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import SignUpForm
from exeterDomination.models import Locations

def index(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/homePage.html", context)

def about(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/aboutPage.html", context)

def login(request : request) -> HttpResponse:
    if not request.user.is_authenticated:
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
        return redirect('game')
    else:
        return redirect('game')



def signup(request : request) -> HttpResponse:
    if not request.user.is_authenticated:
        if request.method == 'GET':
            form = SignUpForm()
            context = {'form': form}
            return render(request, "exeterDomination/signUpPage.html", context)
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            username = request.POST['username']
            password = request.POST['password1']
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                user2 = authenticate(request, username=username, password=password)
                if user2 is not None:
                    k(request, user2)
                return redirect(reverse('index'))
            else:
                print('Form is not valid')
                context = {'form': form}
                return render(request, 'exeterDomination/signUpPage.html', context)
        return render(request, "exeterDomination/signUpPage.html", {})
    else:
        return redirect('game')


@login_required(login_url='/play/login')
def game(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/gamePage.html", context)


def leaderboard(request : request) -> HttpResponse:
    context = {'player_scores' : [['ExamplePlayerName', "100"], ], }
    return render(request, "exeterDomination/leaderboardPage.html", context)

def locations(request : request) -> HttpResponse:
    # Order in array is harrisonOwner, inspirOwner, innoOwner, laverOwner, amoryOwner,
    # forumOwner, intoOwner, streathamOwner, newmanOwner, sportsOwner.

    buildingOwners = []

    for i in range(1, 11, 1):
        buildingOwner = Locations.objects.get(pk=i).claimedBy
        if buildingOwner != None:
            buildingOwners.append(buildingOwner.username)
        else:
            buildingOwners.append("no one. This building is yet to be claimed")

    context = {'buildingOwners' : buildingOwners}
    return render(request, "exeterDomination/locationsPage.html", context)
