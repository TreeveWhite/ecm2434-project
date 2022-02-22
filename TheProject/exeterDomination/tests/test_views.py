from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestGame(TestCase):
    def setUp(self):
        # Must be changed when sessions are implemented
        User.objects.create(username="test", password="password")

    def testGameWithNoLogin(self):
        resp = self.client.get(reverse('game'), follow=True)
        # Change this if redirect location changes later down the line
        self.assertRedirects(resp, '/play/login')
        # Change this if redirect location changes
        self.assertTemplateUsed(resp, 'exeterDomination/loginPage.html')
        # later down the line

    def testGameWithLogin(self):
        # Must be changed when sessions are implemented
        self.client.login(username="test", password="password")
        resp = self.client.get(reverse('game'))
        self.assertRedirects(resp, '/play/game')
        self.assertTemplateUsed(resp, "exeterDomination/gamePage.html")


class TestLoginPage(TestCase):
    def setUp(self):
        # Must be changed when sessions are implemented
        User.objects.create(username="test", password="password")

    def testLoginPageWhileLoggedOut(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/loginPage.html')

    def testLoginPageWhileLoggedIn(self):
        # Must be changed when sessions are implemented
        self.client.login(username="test", password="password")
        resp = self.client.get(reverse('login'))
        # Not sure where to check the site sends the logged in user
        self.assertRedirects(resp, '/play/game/')
        self.assertTemplateUsed(resp, 'exeterDomination/gamePage.html')


class TestSignUpPage(TestCase):
    def setUp(self):
        # Must be changed when sessions are implemented
        User.objects.create(username="test", password="password")

    def testSignUpPageWhileSignedIn(self):
        # Must be changed when sessions are implemented
        self.client.login(username="test", password="password")
        resp = self.client.get(reverse('signup'))
        # Not sure where to check the site sends the logged in user
        self.assertRedirects(resp, '/play/game/')
        self.assertTemplateUsed(resp, 'exeterDomination/gamePage.html')

    def testSignUpPageWhileSignedOut(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/signUpPage.html')


# class TestLeaderboardPage(TestCase):
#    def testLeaderboardPage(self):
