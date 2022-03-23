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
from exeterDomination.models import Locations
from .forms import SignUpForm, JoinTeamForm, CreateTeamForm


from .location import posInRec


def index(indexRequest: request) -> HttpResponse:
    """
    This is the index view. It renders the home
    page for the user.
    :param request: the Http Request the server has received
    :type request: HttpRequest
    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    context = {}
    return render(indexRequest, "exeterDomination/homePage.html", context)


def about(aboutRequest: request) -> HttpResponse:
    """
    This is the about view. It renders the about
    page for the user.
    :param request: the Http Request the server has received
    :type request: HttpRequest
    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    context = {}
    return render(aboutRequest, "exeterDomination/aboutPage.html", context)


def login(loginRequest: request) -> HttpResponse:
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
    :param request: the Http Request the server has received
    :type request: HttpRequest
    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    if not loginRequest.user.is_authenticated:
        if loginRequest.method == "GET":
            return render(loginRequest, "exeterDomination/loginPage.html", {})
        if loginRequest.method == "POST":
            username = loginRequest.POST['uname']
            password = loginRequest.POST['psw']
            user = authenticate(loginRequest, username=username, password=password)
            if user is not None:
                k(loginRequest, user)
            else:
                return render(loginRequest, "exeterDomination/loginPage.html", {})
        return redirect('game')
    else:
        return redirect('game')


def signup(signUpRequest: request) -> HttpResponse:
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
    :param request: the Http Request the server has received
    :type request: HttpRequest
    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    if not signUpRequest.user.is_authenticated:
        if signUpRequest.method == 'GET':
            form = SignUpForm()
            context = {'form': form}
            return render(signUpRequest, "exeterDomination/signUpPage.html", context)
        if signUpRequest.method == 'POST':
            form = SignUpForm(signUpRequest.POST)
            username = signUpRequest.POST['username']
            password = signUpRequest.POST['password1']
            group = signUpRequest.POST["teamName"]
            if form.is_valid():
                form.save()
                #user = form.cleaned_data.get('username')
                user2 = authenticate(
                    signUpRequest, username=username, password=password)
                if user2 is not None:
                    print(group)
                    k(signUpRequest, user2)
                    grp = Group.objects.get(id=group)
                    grp.user_set.add(User.objects.get(id=signUpRequest.user.id))
                    grp.save()
                return redirect(reverse('index'))
            else:
                print('Form is not valid')
                context = {'form': form}
                return render(
                    signUpRequest,
                    'exeterDomination/signUpPage.html',
                    context)
        return render(signUpRequest, "exeterDomination/signUpPage.html", {})
    else:
        return redirect('game')


@login_required(login_url='/login')
def game(gameRequest: request) -> HttpResponse:
    """
    This is the game view. It can only be accessed by
    logged-in users; if an un-logged in user tries to
    access it, they are redirected to the login page.
    Otherwise, the game page is rendered.
    :param request: the Http Request the server has received
    :type request: HttpRequest
    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    context = {}

    if gameRequest.user.groups.filter(name="Game Masters").exists():
        if not gameRequest.user.is_staff:
            gameRequest.user.is_staff = True
            gameRequest.user.save()
    else:
        if gameRequest.user.is_staff and not gameRequest.user.is_superuser and gameRequest.user.groups.filter(name="Game Masters").exists():
            gameRequest.user.is_staff = False
            gameRequest.user.save()

    return render(gameRequest, "exeterDomination/gamePage.html", context)


def leaderboard(request: request) -> HttpResponse:
    """
    This is the leaderboard view. It renders
    the leaderboard page.
    :param request: the Http Request the server has received
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

    try:
        teams = Group.objects.all().exclude(name="GameMasters")

        teamScores = {}
        for team in teams:
            teamScores[team.name] = 0

            for player in playerScores.keys():
                if player in team.user_set.all():
                    teamScores[team.name] += playerScores[player]
        
        teamScores["Unclaimed"] = playerScores["Unclaimed"]
    
    except Exception:
        teamScores = {"Unclaimed": 100}

    context = {'player_scores': playerScores, 'team_scores' : teamScores}
    return render(request, "exeterDomination/leaderboardPage.html", context)


@login_required
def teams(teamRequest : request) -> HttpRequest:
    """
    This is the teams view. It renders
    the page which allows users to create
    or join different teams.
    :param request: the Http Request the server has received
    :type request: HttpRequest
    :return: the rendered template for this page
    :rtype: HttpResponse
    """
    queryForName = Group.objects.filter(user=teamRequest.user).exclude(name="Game Masters").first()
    finalTeamName = queryForName.name if queryForName is not None else "No Team"
    joinTeamForm = JoinTeamForm()
    createTeamForm = CreateTeamForm()
    context = {"teamName": finalTeamName, 'form': joinTeamForm, 'form2': createTeamForm}
    if teamRequest.method == 'GET':
        return render(teamRequest, "exeterDomination/teamsPage.html", context)
    elif teamRequest.method == 'POST':
        joinTeamForm = JoinTeamForm(teamRequest.POST or None)
        createTeamForm = CreateTeamForm(teamRequest.POST or None)
        if "join_team" in teamRequest.POST:
            group = teamRequest.POST["teamName"]
            if joinTeamForm.is_valid():
                print("jointTeamForm is valid")
                meow = Group.objects.filter(user=User.objects.get(id=teamRequest.user.id))
                if len(meow) > 0:
                    print("More than 0 group objects - after joinTeamForm")
                    for i in meow:
                        groupToRemoveUserFrom = Group.objects.get(id=i.id)
                        if groupToRemoveUserFrom.name != "Game Masters":
                            groupToRemoveUserFrom.user_set.remove(teamRequest.user.id)
                            groupToRemoveUserFrom.save()

                groupToJoin = Group.objects.get(id=group)
                print(groupToJoin)
                groupToJoin.user_set.add(User.objects.get(id=teamRequest.user.id))
                print(groupToJoin.user_set, groupToJoin.name)
                groupToJoin.save()
                return redirect(reverse("index"))
            #return render(request, "exeterDomination/teamsPage.html", context)
        elif "create_team" in teamRequest.POST:
            group2 = teamRequest.POST["teamName2"]
            print(createTeamForm.errors)
            if createTeamForm.is_valid():
                newGroup, yesno = Group.objects.get_or_create(name=group2)
                newGroup.save()
                if yesno:
                    meow2 = teamRequest.user.groups.filter(user=User.objects.get(id=teamRequest.user.id))
                    if len(meow2) > 0:
                        for i in meow2:
                            groupToRemoveUserFrom = teamRequest.user.groups.get(id=i.id)
                            if groupToRemoveUserFrom.name != "Game Masters":
                                groupToRemoveUserFrom.user_set.remove(teamRequest.user.id)
                                groupToRemoveUserFrom.save()
                        nan = Group.objects.get(name=group2)
                        nan.user_set.add(User.objects.get(id=teamRequest.user.id))
                        nan.save()
                        nan.refresh_from_db()
                        teamRequest.user.groups.add(nan)
                        teamRequest.user.groups.update()
                        return redirect(reverse("index"))
    return render(teamRequest, "exeterDomination/teamsPage.html", context)


def locations(locationRequest: request) -> HttpResponse:
    """
    This is the locations view. It queries the
    locations database, and passes them as
    context to the main page. They are then
    displayed on a map of the campus.
    :param request: the Http Request the server has received
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
    return render(locationRequest, "exeterDomination/locationsPage.html", context)


def claim(claimRequest: request) -> HttpResponse:
    """
    This is the claim method. It enables
    a player to claim a location.
    :param request: the Http Request the server has received
    :type request: HttpRequest
    :return: the rendered template for this page
    :rtype: HttpResponse
    """

    if claimRequest.method == "POST":
        playerLong = claimRequest.POST.get("long")
        playerLat = claimRequest.POST.get("lat")

        # print(playerLat)
        # print(playerLong)

        locationName = posInRec(
            claimRequest.user.id,
            float(playerLong),
            float(playerLat))

        if locationName != "":
            msg = f"Congratulations, you have claimed the {locationName} building."

        else:
            msg = "Unfortunately you are not close enough to claim any building. Please move to a building accepted by the game and try again. See locations page for all buildings."

        return HttpResponse(msg)