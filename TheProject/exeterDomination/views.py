from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/homePage.html", context)

def about(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/aboutPage.html", context)

def login(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/loginPage.html", context)

def signup(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/signUpPage.html", context)

def game(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/gamePage.html", context)