"""
This test file is for testing
forms used on the website.
"""
from django.test import TestCase
from ..forms import SignUpForm


class SignUpFormTest(TestCase):
    """
    This form test will check various inputs, and hopefully match
    them to their expected outputs.
    """

    def testShortPassword(self):
        """
        This function will test a valid username with a well-made,
        but ultimately too-short password.

        The expected result:
        password length < 8 characters -- will return false when its validity is checked.
        """
        form = SignUpForm(data={
            "username": "validTestUsername",
            "password1": "s062k@",
            "password2": "s062k@"
        })
        self.assertFalse(form.is_valid())

    def testLongPassword(self):
        """
        This function will test a valid username with a well-made,
        very long (64 character) password. It contains lower, and
        uppercase letters, as well as special characters, and
        numbers.

        The expected result:
        password length > 8 characters -- will return true when its validity is checked.
        """
        form = SignUpForm(
            data={
                "username": "validTestUsername",
                "password1": "@3qgqbq?e24dGnJ7UeBY-TWAp$c&Z8ywjNpULL@!CANL+#zvDM739s_Yth?kd^eN@",
                "password2": "@3qgqbq?e24dGnJ7UeBY-TWAp$c&Z8ywjNpULL@!CANL+#zvDM739s_Yth?kd^eN@"})
        self.assertTrue(form.is_valid())

    def testSimilarUsernameAndPassword(self):
        """
        This function will test a valid username with a not so well-made
        password. The password is simply the username with two @ signs
        appended to it.

        The expected result:
        password very similar to username -- will return false when its validity is checked.
        """
        form = SignUpForm(data={
            "username": "validTestUsername",
            "password1": "validTestUsername@@",
            "password2": "validTestUsername@@"
        })

        self.assertFalse(form.is_valid())

    def testInvalidUsername(self):
        """
        This function will test an invalid username with a well-formed
        password. The username is a string of special characters, with
        the word invalid appended to the end of it.

        The expected result:
        username contains forbidden characters -- will return false when its validity is checked.
        """
        form = SignUpForm(data={
            "username": "invalid)=`&3,\\_<,`4~$2",
            "password1": "5vqR*ES6q4vL",
            "password2": "5vqR*ES6q4vL"
        })

        self.assertFalse(form.is_valid())

    def testAllNumbersPassword(self):
        """
        This function will test a valid username with a password made
        up solely of numbers.

        The expected result:
        password contains only numbers -- will return false when its validity is checked.
        """
        form = SignUpForm(data={
            "username": "validTestUsername",
            "password1": "060737087507516",
            "password2": "060737087507516"
        })

        self.assertFalse(form.is_valid())

    def testBadPasswordComplexity(self):
        """
        This function will test a valid username with a very bad password.
        The password is simply, password.

        password is easily guessable -- will return false when its validity is checked.
        """
        form = SignUpForm(data={
            "username": "validTestUsername",
            "password1": "password",
            "password2": "password"
        })

        self.assertFalse(form.is_valid())
