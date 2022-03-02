"""
This test file is an integration
test. Many aspects of the site
are tested as one.
"""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import TestCase


# Insert geckodriver executable here
pathToGeckodriver = "/Users/faris/downloads/geckodriver"


class SeleniumLoginTest(StaticLiveServerTestCase, TestCase):
    """
    This class will test the functionality of the login system with test credentials.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path=pathToGeckodriver)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def testLoginFunctionality(self):
        """
        This function navigates directly to the login page, enters a username and
        password, and then presses the login button. It then checks that the user
        is logged in.
        """
        self.selenium.get(self.live_server_url + "/login")
        unameInput = self.selenium.find_element_by_name("uname")
        # Need to tweak this to allow us to use this username in final build
        unameInput.send_keys("testUser1")
        pwdInput = self.selenium.find_element_by_name("psw")
        # Need to tweak this to allow us to use this password in the final
        # build
        pwdInput.send_keys("password")
        button = self.selenium.find_element_by_xpath(
            "//input[@class='formButton arcade-font']")
        button.click()
        self.selenium.implicitly_wait(5)
        assert self.selenium.title != "Login | Exeter Domination"


class SignUpWithSeleniumTest(StaticLiveServerTestCase, TestCase):
    """
    This class will test the sign up system with test credentials and check if the
    user is sent to the correct location.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path=pathToGeckodriver)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def testSignUpFunctionality(self):
        """
        This function loads the signup page, creates a user account, and presses
        the signup button. It then checks that the user is redirected directly
        to a page where they are logged in.
        """
        self.selenium.get(self.live_server_url + "/signup")
        testUsername = self.selenium.find_element_by_name("username")
        testUsername.send_keys("testUser1")
        testPassword = self.selenium.find_element_by_name("password1")
        testPassword.send_keys("ab43aa1-pejhf@33b")
        testRepeatPassword = self.selenium.find_element_by_name("password2")
        testRepeatPassword.send_keys("ab43aa1-pejhf@33b")
        signUpButton = self.selenium.find_element_by_xpath(
            "//input[@class='formButton arcade-font']")
        signUpButton.click()
        self.selenium.implicitly_wait(5)
        assert self.selenium.title != "Sign Up | Exeter Domination" or "Log In | Exeter Domination"


class testNavigationLinks(StaticLiveServerTestCase, TestCase):
    """
    This class is mainly just to test that the hyperlinks, and navigation buttons are
    in order and working correctly. This is not currently comprehensive, but will be
    in time for release.
    """
    fixtures = ['../fixtures/coordinates.json', '../fixtures/locations.json']

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path=pathToGeckodriver)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def testHomeToAboutBackToHome(self):
        """
        This function tests that the navigation buttons from the home
        page to the about page and back are in working order.
        """
        self.selenium.get(self.live_server_url + "/")
        aboutButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button2']")
        aboutButton.click()
        assert self.selenium.title == "About | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/about"
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/"

    def testHomeToLeaderboardToHome(self):
        """
        This function tests that the navigation buttons from the home
        page to the leaderboard page and back are in working order.
        """
        self.selenium.get(self.live_server_url + "/")
        leaderboardButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button3']")
        leaderboardButton.click()
        assert self.selenium.title == "Leaderboards | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/leaderboard"
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/"

    def testLeaderboardToLogin(self):
        """
        This function tests a likely path for a returning user, who may
        check the leaderboard and then move to the login page.
        """
        self.selenium.get(self.live_server_url + "/leaderboard")
        loginButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, 'login')]")
        loginButton.click()
        assert self.selenium.title == "Log In | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/login"

    def testLeaderboardToSignUp(self):
        """
        This function tests the most likely path for a new user, who may
        have originally been curious about who was topping the leaderboard,
        and has subsequently navigated to the sign up page.
        """
        self.selenium.get(self.live_server_url + "/leaderboard")
        signUpButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, 'signup')]")
        signUpButton.click()
        assert self.selenium.title == "Sign Up | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/signup"

    '''def testHomeToLocationsAndBack(self):
        """
        This function tests the path a user would take when checking the
        current locations, and then returning to the home page.
        """
        self.selenium.get(self.live_server_url + "/play")
        locationsButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button4']")
        locationsButton.click()
        assert self.selenium.title == "Locations | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/leaderboard"
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/play')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/"'''
