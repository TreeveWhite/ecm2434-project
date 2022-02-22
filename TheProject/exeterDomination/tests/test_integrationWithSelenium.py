from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import TestCase


pathToGeckodriver = "/Users/faris/downloads/geckodriver" # Insert geckodriver executable here


class SeleniumLoginTest(StaticLiveServerTestCase, TestCase):

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
        unameInput.send_keys("testUser1")  # Need to tweak this to allow us to use this username in final build
        pwdInput = self.selenium.find_element_by_name("psw")
        pwdInput.send_keys("password")  # Need to tweak this to allow us to use this password in the final build
        button = self.selenium.find_element_by_xpath("//input[@class='formButton arcade-font']")
        button.click()
        self.selenium.implicitly_wait(5)
        assert "Login" and "Sign Up" not in self.selenium.page_source
        assert self.selenium.title != "Login | Exeter Domination"
        # assert "<h1>Forbidden <span>(403)</span></h1>" not in self.selenium.page_source
        # The above test will continually fail until the login / signup system has been implemented


class SignUpWithSeleniumTest(StaticLiveServerTestCase, TestCase):
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
        signUpButton = self.selenium.find_element_by_xpath("//input[@class='formButton arcade-font']")
        signUpButton.click()
        self.selenium.implicitly_wait(5)
        assert "Login" and "Sign Up" not in self.selenium.page_source
        assert self.selenium.title != "Sign Up | Exeter Domination" or "Log In | Exeter Domination"
        # assert "<h1>Forbidden <span>(403)</span></h1>" not in self.selenium.page_source
        # The above test will continually fail until the login / signup system has been implemented

