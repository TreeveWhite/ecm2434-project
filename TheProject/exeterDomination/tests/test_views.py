from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestGame(TestCase):
    def setUp(self):
        User.objects.create(username="test", password="password")  # Must be changed when sessions are implemented

    def testGameWithNoLogin(self):
        resp = self.client.get(reverse('game'), follow=True)
        self.assertRedirects(resp, '/play/login')  # Change this if redirect location changes later down the line
        self.assertTemplateUsed(resp, 'exeterDomination/loginPage.html')  # Change this if redirect location changes
        # later down the line

    def testGameWithLogin(self):
        self.client.login(username="test", password="password")  # Must be changed when sessions are implemented
        resp = self.client.get(reverse('game'))
        self.assertRedirects(resp, '/play/game')
        self.assertTemplateUsed(resp, "exeterDomination/gamePage.html")


class TestLoginPage(TestCase):
    def setUp(self):
        User.objects.create(username="test", password="password")  # Must be changed when sessions are implemented

    def testLoginPageWhileLoggedOut(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/loginPage.html')

    def testLoginPageWhileLoggedIn(self):
        self.client.login(username="test", password="password")  # Must be changed when sessions are implemented
        resp = self.client.get(reverse('login'))
        self.assertRedirects(resp, '/play/game/')  # Not sure where to check the site sends the logged in user
        self.assertTemplateUsed(resp, 'exeterDomination/gamePage.html')


class TestSignUpPage(TestCase):
    def setUp(self):
        User.objects.create(username="test", password="password")  # Must be changed when sessions are implemented

    def testSignUpPageWhileSignedIn(self):
        self.client.login(username="test", password="password")  # Must be changed when sessions are implemented
        resp = self.client.get(reverse('signup'))
        self.assertRedirects(resp, '/play/game/')  # Not sure where to check the site sends the logged in user
        self.assertTemplateUsed(resp, 'exeterDomination/gamePage.html')

    def testSignUpPageWhileSignedOut(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exeterDomination/signUpPage.html')


#class TestLeaderboardPage(TestCase):
#    def testLeaderboardPage(self):
