from django.urls import reverse
from django.test import SimpleTestCase


class PlayPageTests(SimpleTestCase):
    def testResponseCode(self):
        pageURL = "/play"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 301)

    def testTemplateName(self):
        viewName = "index"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/homePage.html")

    def testView(self):
        viewName = "index"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class AboutPageTests(SimpleTestCase):
    def testResponseCode(self):
        pageURL = "/play/about"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        pageURL = "/play/about"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/aboutPage.html")

    def testView(self):
        viewName = "about"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class LoginPageTests(SimpleTestCase):
    def testResponseCode(self):
        pageURL = "/play/login"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        pageURL = "/play/login"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/loginPage.html")

    def testView(self):
        viewName = "login"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class SignUpPageTests(SimpleTestCase):
    def testResponseCode(self):
        pageURL = "/play/signup"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        pageURL = "/play/signup"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/signUpPage.html")

    def testView(self):
        viewName = "signup"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class GamePageTests(SimpleTestCase):
    def testResponseCode(self):
        pageURL = "/play/game"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        pageURL = "/play/game"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/gamePage.html")

    def testView(self):
        viewName = "game"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class LeaderboardPageTests(SimpleTestCase):
    def testResponseCode(self):
        pageURL = "/play/leaderboard"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        pageURL = "/play/leaderboard"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/leaderboardPage.html")

    def testView(self):
        viewName = "leaderboard"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)
