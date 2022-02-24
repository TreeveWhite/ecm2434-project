from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from ..models import Locations


class TestGame(TestCase):
    """
    This class tests the 'game' view, where the user can play a wordle
    like game to capture a point. Anything to do with the login
    code is merely a placeholder until the login implementation is
    complete.
    """

    def setUp(self):
        user = User.objects.create(username='testuser')
        # Creates a test user
        user.set_password("abdlklnkf3-3432r@dd")
        # Sets a password
        user.save()
        # Saves the test user info

    def testGameWithNoLogin(self):
        """
        Tests if the user is taken to the login page if they try to
        visit the gameplay page without being logged in.
        """
        resp = self.client.get(reverse('game'), follow=True)
        self.assertRedirects(resp, '/play/login?next=%2Fplay%2Fgame')
        self.assertTemplateUsed(resp, 'exeterDomination/loginPage.html')

    def testGameWithLogin(self):
        """
        Tests if the user is taken to the gameplay page if they
        access it while being logged in already.
        """
        c = Client()
        logged_in = c.login(
            username="testuser",
            password="abdlklnkf3-3432r@dd")
        # Logs in with the test user information
        resp = c.get(reverse('game'))
        self.assertEquals(resp.status_code, 200)


class TestLoginPage(TestCase):
    """
    This class tests the redirects on the login page.
    """

    def setUp(self):
        user = User.objects.create(username='testuser')
        # Creates a test user
        user.set_password("abdlklnkf3-3432r@dd")
        # Sets a password
        user.save()
        # Saves the test user info

    def testLoginPageWhileLoggedOut(self):
        """
        This function makes sure the user is on the correct
        page (login page) if they navigate to it and are not
        logged in.
        """
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/loginPage.html')

    def testLoginPageWhileLoggedIn(self):
        """
        This function tests to see if the user is redirected
        to the correct page if they navigate to the login
        page and are already logged in.
        """
        c = Client()
        logged_in = c.login(
            username="testuser",
            password="abdlklnkf3-3432r@dd")
        resp = c.get(reverse('login'))
        # Not sure where to check the site sends the logged in user
        self.assertEqual(resp.url, "/play/game")
        self.assertEqual(resp.status_code, 302)


class TestSignUpPage(TestCase):
    """
    This class tests the redirects on the signUp page.
    """

    def setUp(self):
        user = User.objects.create(username='testuser')
        # Creates a test user
        user.set_password("abdlklnkf3-3432r@dd")
        # Sets a password
        user.save()
        # Saves the test user info

    def testSignUpPageWhileSignedIn(self):
        """
        This function makes sure a user is redirected to
        the appropriate page if they navigate to the
        signup page while already logged in.
        """
        c = Client()
        logged_in = c.login(
            username="testuser",
            password="abdlklnkf3-3432r@dd")
        resp = c.get(reverse('signup'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, '/play/game')

    def testSignUpPageWhileSignedOut(self):
        """
        This function just tests if a user remains on the
        correct page (signup page) when they navigate to it
        while signed out.
        """
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/signUpPage.html')


class TestLeaderboardPage(TestCase):
    """
    This class will be testing the Leaderboard page view.
    """

    def setUp(self):
        user = User.objects.create(username='FarisKapes')
        # Creates a test user
        user.set_password("abdlklnkf3-3432r@dd")
        # Sets a password
        user.save()
        # Saves the test user info

    def testLeaderboardWhileLoggedOut(self):
        """
        This function will test the leaderboard page while
        logged out. Ensuring that the additional table above
        the leaderboard table with the logged-in users' info
        is not visible to a visitor / logged-out user.
        """
        resp = self.client.get(reverse('leaderboard'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/leaderboardPage.html')
        assert not "FarisKapes".encode("UTF-8") in resp.content

    def testLeaderboardWhileLoggedIn(self):
        """
        This function will be testing the leaderboard page
        while the user is logged in. It will check if the
        user can see their username and domination percentage
        above the main leaderboard
        """
        c = Client()
        c.login(
            username="FarisKapes",
            password="abdlklnkf3-3432r@dd")
        resp = c.get(reverse('leaderboard'))
        assert "FarisKapes".encode('UTF-8') in resp.content


class TestLocationsPage(TestCase):
    """
    This class will be testing the locations page.
    """
    fixtures = ['../fixtures/coordinates.json', '../fixtures/locations.json']
    # This allows the fixtures containing the coordinate and location
    # information to be loaded

    def setUp(self):
        user = User.objects.create(username='testUser')
        # Creates a test user
        user.set_password("abdlklnkf3-3432r@dd")
        # Sets a password
        user.save()
        # Saves the test user info

    def testLocationsPageWhileLoggedOut(self):
        """
        This function tests the locations page view while the user is
        logged out.
        """
        resp = self.client.get(reverse('locations'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/locationsPage.html')

    def testLocationsPageWhileLoggedIn(self):
        """
        This function tests the locations page view while the user is
        logged in.
        """
        c = Client()
        c.login(
            username="testuser",
            password="abdlklnkf3-3432r@dd")
        resp = c.get(reverse('locations'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/locationsPage.html')
