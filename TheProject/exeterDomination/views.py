"""
views.py
=======================================
The views.py file is responsible for displaying
the correct content on the page a user navigates
to.
"""
from urllib import request

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpRequest
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

    :param request: the Http Request the server has recived
    :type request: HttpRequest

    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    context = {}
    return render(request, "exeterDomination/homePage.html", context)


def about(request: request) -> HttpResponse:
    """
    This is the about view. It renders the about
    page for the user.

    :param request: the Http Request the server has recived
    :type request: HttpRequest

    :return: the rendered template for this page
    :rtype: HttpResponse
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

    :param request: the Http Request the server has recived
    :type request: HttpRequest

    :return: the rendered template for this page
    :rtype: HttpResponse
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

    :param request: the Http Request the server has recived
    :type request: HttpRequest

    :return: the rendered template for this page
    :rtype: HttpResponse
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
            group = request.POST["teamName"]
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                user2 = authenticate(
                    request, username=username, password=password)
                if user2 is not None:
                    print(group)
                    k(request, user2)
                    grp = Group.objects.get(id=group)
                    grp.user_set.add(User.objects.get(id=request.user.id))
                    grp.save()
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

    :param request: the Http Request the server has recived
    :type request: HttpRequest

    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    context = {}

    if request.user.groups.filter(name="Game Masters").exists():
        if not request.user.is_staff:
            request.user.is_staff = True
            request.user.save()
    else:
        if request.user.is_staff and not request.user.is_superuser and request.user.groups.filter(name="Game Masters").exists():
            request.user.is_staff = False
            request.user.save()

    return render(request, "exeterDomination/gamePage.html", context)


def leaderboard(request: request) -> HttpResponse:
    """
    This is the leaderboard view. It renders
    the leaderboard page.

    :param request: the Http Request the server has recived
    :type request: HttpRequest

    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    try:
        claimedLocations = Locations.objects.select_related(
            'claimedBy').exclude(claimedBy__isnull=True)
        numClaimed = claimedLocations.count()
        numLocations = Locations.objects.all().count()

        playerScores = {}
        for location in claimedLocations:
            if location.claimedBy.username in playerScores.keys():
                playerScores[location.claimedBy.username] += 1 / numLocations * 100
            else:
                playerScores[location.claimedBy.username] = 1 / numLocations * 100

        playerScores["Unclaimed"] = (
            numLocations - numClaimed) / numLocations * 100
    except Exception:
        playerScores = {"Unclaimed": 100}

    context = {'player_scores': playerScores}
    return render(request, "exeterDomination/leaderboardPage.html", context)


def locations(request: request) -> HttpResponse:
    """
    This is the locations view. It queries the
    locations database, and passes them as
    context to the main page. They are then
    displayed on a map of the campus.

    :param request: the Http Request the server has recived
    :type request: HttpRequest

    :return: the rendered template for this page
    :rtype: HttpResponse
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

    :param request: the Http Request the server has recived
    :type request: HttpRequest

    :return: the rendered template for this page
    :rtype: HttpResponse
    """

    if request.method == "POST":
        playerLong = request.POST.get("long")
        playerLat = request.POST.get("lat")

        # print(playerLat)
        # print(playerLong)

        locationName = posInRec(
            request.user.id,
            float(playerLong),
            float(playerLat))

        if locationName != "":
            msg = f"Congratulations, you have claimed the {locationName} building."

        else:
            msg = "Unfortunatly you are not close enough to claim any building. Please move to a building accepted by the game and try again. See locations page for all buildings."

        return HttpResponse(msg)
