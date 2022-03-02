"""
This test file does the base cases
for the exeterDomination project.
"""
from django.urls import reverse
from django.test import SimpleTestCase


class HomePageTests(SimpleTestCase):
    """
    This class contains the basic base case tests for the home
    page.
    """

    def testResponseCode(self):
        """
        This test checks if the correct response code is given
        when a user navigates to the home page.
        """
        pageURL = "/"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        """
        This test checks that the correct template is loaded
        when the user navigates to the home page.
        """
        viewName = "index"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/homePage.html")

    def testView(self):
        """
        This test checks that navigating to the index view
        directly returns the correct response code.
        """
        viewName = "index"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class AboutPageTests(SimpleTestCase):
    """
    This class contains the basic base case tests for the about
    page.
    """

    def testResponseCode(self):
        """
        This test checks if the correct response code is given
        when a user navigates to the about page.
        """
        pageURL = "/about"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        """
        This test checks that the correct template is loaded
        when the user navigates to the about page.
        """
        pageURL = "/about"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/aboutPage.html")

    def testView(self):
        """
        This test checks that navigating to the about view
        directly returns the correct response code.
        """
        viewName = "about"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class LoginPageTests(SimpleTestCase):
    """
    This class contains the basic base case tests for the login
    page.
    """

    def testResponseCode(self):
        """
        This test checks if the correct response code is given
        when a user navigates to the login page.
        """
        pageURL = "/login"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        """
        This test checks that the correct template is loaded
        when the user navigates to the login page.
        """
        pageURL = "/login"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/loginPage.html")

    def testView(self):
        """
        This test checks that navigating to the login view
        directly returns the correct response code.
        """
        viewName = "login"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class SignUpPageTests(SimpleTestCase):
    """
    This class contains the basic base case tests for the signup
    page.
    """

    def testResponseCode(self):
        """
        This test checks if the correct response code is given
        when a user navigates to the signup page.
        """
        pageURL = "/signup"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        """
        This test checks that the correct template is loaded
        when the user navigates to the signup page.
        """
        pageURL = "/signup"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/signUpPage.html")

    def testView(self):
        """
        This test checks that navigating to the signup view
        directly returns the correct response code.
        """
        viewName = "signup"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)


class GamePageTests(SimpleTestCase):
    """
    This class contains the basic base case tests for the gameplay
    page.
    """

    def testResponseCode(self):
        """
        This test checks if the correct response code is given
        when a user navigates to the gameplay page.
        """
        pageURL = "/game"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 302)

    def testView(self):
        """
        This test checks that navigating to the game view
        directly returns the correct response code.
        """
        viewName = "game"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 302)


class LeaderboardPageTests(SimpleTestCase):
    """
    This class contains the basic base case tests for the leaderboard
    page.
    """

    def testResponseCode(self):
        """
        This test checks if the correct response code is given
        when a user navigates to the leaderboard page.
        """
        pageURL = "/leaderboard"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)

    def testTemplateName(self):
        """
        This test checks that the correct template is loaded
        when the user navigates to the leaderboard page.
        """
        pageURL = "/leaderboard"
        resp = self.client.get(pageURL)
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, "exeterDomination/leaderboardPage.html")

    def testView(self):
        """
        This test checks that navigating to the leaderboard view
        directly returns the correct response code.
        """
        viewName = "leaderboard"
        resp = self.client.get(reverse(viewName))
        self.assertEquals(resp.status_code, 200)
