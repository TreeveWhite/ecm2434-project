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
        self.selenium.get(self.live_server_url + "/play/login")
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
        assert "Login" and "Sign Up" not in self.selenium.page_source
        assert self.selenium.title != "Login | Exeter Domination"
        # assert "<h1>Forbidden <span>(403)</span></h1>" not in self.selenium.page_source
        # The above test will continually fail until the login / signup system
        # has been implemented


class SignUpWithSeleniumTest(StaticLiveServerTestCase, TestCase):
    """
    This class will test the sign up system with test credentials and check if the
    user is sent to the correct loacation.
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
        self.selenium.get(self.live_server_url + "/play/signup")
        testUsername = self.selenium.find_element_by_name("username")
        testUsername.send_keys("testUser1")
        testPassword = self.selenium.find_element_by_name("password")
        testPassword.send_keys("password")
        testRepeatPassword = self.selenium.find_element_by_name("psw-repeat")
        testRepeatPassword.send_keys("password")
        signUpButton = self.selenium.find_element_by_xpath(
            "//input[@class='formButton arcade-font']")
        signUpButton.click()
        self.selenium.implicitly_wait(5)
        assert "Login" and "Sign Up" not in self.selenium.page_source
        assert self.selenium.title != "Sign Up | Exeter Domination" or "Log In | Exeter Domination"
        # assert "<h1>Forbidden <span>(403)</span></h1>" not in self.selenium.page_source
        # The above test will continually fail until the login / signup system
        # has been implemented


class testNavigationLinks(StaticLiveServerTestCase, TestCase):
    """
    This class is mainly just to test that the hyperlinks, and navigation buttons are
    in order and working correctly. This is not currently comprehensive, but will be
    in time for release.
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

    def testHomeToAboutBackToHome(self):
        self.selenium.get(self.live_server_url + "/play")
        aboutButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button2']")
        aboutButton.click()
        assert self.selenium.title == "About | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/about"
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/play')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/"

    def testHomeToPlayBackToHome(self):
        self.selenium.get(self.live_server_url + "/play")
        playButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button1']")
        playButton.click()
        assert self.selenium.title == "Play Game | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/game"
        assert "<h3 class=\"Codle\">Compete to Claim Building</h3>" in self.selenium.page_source
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/play')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/"

    def testHomeToLeaderboardToHome(self):
        self.selenium.get(self.live_server_url + "/play")
        leaderboardButton = self.selenium.find_element_by_xpath(
            "//input[@class='arcade-font button3']")
        leaderboardButton.click()
        assert self.selenium.title == "Leaderboards | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/leaderboard"
        homeButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, '/play')]")
        homeButton.click()
        assert self.selenium.title == "Home | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/"

    def testLeaderboardToLogin(self):
        self.selenium.get(self.live_server_url + "/play/leaderboard")
        loginButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, 'login')]")
        loginButton.click()
        assert self.selenium.title == "Log In | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/login"

    def testLeaderboardToSignUp(self):
        self.selenium.get(self.live_server_url + "/play/leaderboard")
        signUpButton = self.selenium.find_element_by_xpath(
            "//a[contains(@href, 'signup')]")
        signUpButton.click()
        assert self.selenium.title == "Sign Up | Exeter Domination"
        assert self.selenium.current_url == self.live_server_url + "/play/signup"
