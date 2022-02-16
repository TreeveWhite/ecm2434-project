from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(request : request) -> HttpResponse:
    context = {}
    return render(request, "exeterDomination/homePage.html", context)