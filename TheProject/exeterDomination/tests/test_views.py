from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client


class TestGame(TestCase):
    """
    This class tests the 'game' view, where the user can play a wordle
    like game to capture a point. Anything to do with the login
    code is merely a placeholder until the login implementation is
    complete.
    """
    def setUp(self):
        # Must be changed when sessions are implemented
        User.objects.create(username="test", password="password")

    def testGameWithNoLogin(self):
        """
        Tests if the user is taken to the login page if they try to
        visit the gameplay page without being logged in.
        """
        resp = self.client.get(reverse('game'), follow=True)
        # Change this if redirect location changes later down the line
        self.assertRedirects(resp, '/play/login')
        # Change this if redirect location changes
        self.assertTemplateUsed(resp, 'exeterDomination/loginPage.html')
        # later down the line

    def testGameWithLogin(self):
        """
        Tests if the user is taken to the gameplay page if they
        access it while being logged in already.
        """
        # Must be changed when sessions are implemented
        self.client.login(username="test", password="password")
        #c = Client(enforce_csrf_checks=True)
        #c.force_login("test")
        resp = self.client.get(reverse('game'))
        self.assertRedirects(resp, '/play/game')
        self.assertTemplateUsed(resp, "exeterDomination/gamePage.html")


class TestLoginPage(TestCase):
    """
    This class tests the redirects on the login page.
    """
    def setUp(self):
        # Must be changed when sessions are implemented
        User.objects.create(username="test", password="password")

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
        # Must be changed when sessions are implemented
        self.client.login(username="test", password="password")
        resp = self.client.get(reverse('login'))
        # Not sure where to check the site sends the logged in user
        self.assertRedirects(resp, '/play/game/')
        self.assertTemplateUsed(resp, 'exeterDomination/gamePage.html')


class TestSignUpPage(TestCase):
    """
    This class tests the redirects on the signUp page.
    """
    def setUp(self):
        # Must be changed when sessions are implemented
        User.objects.create(username="test", password="password")

    def testSignUpPageWhileSignedIn(self):
        """
        This function makes sure a user is redirected to
        the appropriate page if they navigate to the
        signup page while already logged in.
        """
        # Must be changed when sessions are implemented
        self.client.login(username="test", password="password")
        resp = self.client.get(reverse('signup'))
        # Not sure where to check the site sends the logged in user
        self.assertRedirects(resp, '/play/game/')
        self.assertTemplateUsed(resp, 'exeterDomination/gamePage.html')

    def testSignUpPageWhileSignedOut(self):
        """
        This function just tests if a user remains on the
        correct page (signup page) when they navigate to it
        while signed out.
        """
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/signUpPage.html')


# class TestLeaderboardPage(TestCase):
#    def testLeaderboardPage(self):
