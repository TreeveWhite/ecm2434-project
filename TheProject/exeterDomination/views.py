"""
The views.py file is responsible for displaying
the correct content on the page a user navigates
 to.
"""
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as k
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm
from exeterDomination.models import Locations

from .location import posInRec


def index(request: request) -> HttpResponse:
    """
    This is the index view. It renders the home
    page for the user.

    Returns:
        HttpResponse: the rendered template for
            this page
    """
    context = {}
    return render(request, "exeterDomination/homePage.html", context)


def about(request: request) -> HttpResponse:
    """
    This is the about view. It renders the about
    page for the user.

    Returns:
        HttpResponse: the rendered template for
            this page
    """
    context = {}
    return render(request, "exeterDomination/aboutPage.html", context)


def login(request: request) -> HttpResponse:
    """
    This is the login view. If the user is authenticated, then
    they are redirecred to the game page; otherwise the type of
    request is checked.
        * GET request: It will render the loginPage
            with empty fields.
        * POST request: It will get the username and
            password entered. It then tries to
            authenticate the user; if the credentials
            match, then the user is logged in and taken
            to the game page. Otherwise the form is
            reset.
    """
    if not request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "exeterDomination/loginPage.html", {})
        if request.method == "POST":
            username = request.POST['uname']
            password = request.POST['psw']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                k(request, user)
            else:
                return render(request, "exeterDomination/loginPage.html", {})
        return redirect('game')
    else:
        return redirect('game')


def signup(request: request) -> HttpResponse:
    """
    This is the signup view. If the user is authenticated, then
    they are redirected to the game page; otherwise the type of
    request is checked:
        * GET request: It will render the signUpPage
            with empty form fields.
        * POST request: It will get the username and
            password entered. If the form is valid,
            then the form data is cleaned for security,
            and then the user is added to the database.
            Finally, the user is logged in and redirected
            to the home page.
    """
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
                user2 = authenticate(
                    request, username=username, password=password)
                if user2 is not None:
                    k(request, user2)
                return redirect(reverse('index'))
            else:
                print('Form is not valid')
                context = {'form': form}
                return render(
                    request,
                    'exeterDomination/signUpPage.html',
                    context)
        return render(request, "exeterDomination/signUpPage.html", {})
    else:
        return redirect('game')


@login_required(login_url='/login')
def game(request: request) -> HttpResponse:
    """
    This is the game view. It can only be accessed by
    logged-in users; if an un-logged in user tries to
    access it, they are redirected to the login page.
    Otherwise, the game page is rendered.

    Returns:
        HttpResponse: the rendered template for
            this page
    """
    context = {}
    return render(request, "exeterDomination/gamePage.html", context)


def leaderboard(request: request) -> HttpResponse:
    """
    This is the leaderboard view. It renders
    the leaderboard page.

    Returns:
        HttpResponse: the rendered template for
            this page
    """
    context = {'player_scores': [['ExamplePlayerName', "100"], ], }
    return render(request, "exeterDomination/leaderboardPage.html", context)


def locations(request: request) -> HttpResponse:
    """
    This is the locations view. It queries the
    locations database, and passes them as
    context to the main page. They are then
    displayed on a map of the campus.

    Returns:
        HttpResponse: the rendered template for
            this page
    """
    # Order in array is harrisonOwner, inspirOwner, innoOwner, laverOwner, amoryOwner,
    # forumOwner, intoOwner, streathamOwner, newmanOwner, sportsOwner.

    buildingOwners = []

    for i in range(1, 11, 1):
        buildingOwner = Locations.objects.get(pk=i).claimedBy
        if buildingOwner is not None:
            buildingOwners.append(buildingOwner.username)
        else:
            buildingOwners.append("no one. This building is yet to be claimed")

    context = {'buildingOwners': buildingOwners}
    return render(request, "exeterDomination/locationsPage.html", context)


def claim(request: request) -> HttpResponse:
    """
    This is the claim method. It enables
    a player to claim a location.

    Returns:
        HttpResponse: the rendered template for
            this page
    """

    if request.method == "POST":
        playerLong = request.POST.get("long")
        playerLat = request.POST.get("lat")

        print(playerLat)

        print(playerLong)

        locationName = posInRec(1, float(playerLat), float(playerLong))

        if locationName != "":
            msg = f"Congratulations, you have claimed the {locationName} building."
        
        else:
            msg = "Unfortunatly you are not close enough to claim any building. Please move to a building accepted by the game and try again. See locations page for all buildings."

        return HttpResponse(msg)
