from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from exeterDomination.models import Users, Locations

def index(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/homePage.html", context)

def about(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/aboutPage.html", context)

def login(request : request, username : str, password : str) -> HttpResponse:

    returnPage  = render(request, "exeterDomination/loginPage.html", {})

    # users = Users.objects.filter()

    # if :
    #     # Successful Login
    #     # Set cookie as the unique PK or session ID as unique PK.
    #     context = {}
    #     returnPage = render(request, "exeterDomination/gamePage.html", context)

    return returnPage

def signup(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/signUpPage.html", context)

def game(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/gamePage.html", context)

def leaderboard(request : request) -> HttpResponse:
    context = {'player_scores' : [['ExamplePlayerName', "100"], ], }
    return render(request, "exeterDomination/leaderboardPage.html", context)