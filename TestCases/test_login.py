import time

import faker
import pytest
from Pages import login_page
from faker import Faker

from TestCases.conftest import setup


@pytest.mark.usefixtures("setup")
class Test_login_page():

    def test_loginWithValidCredentials(self):
        Login_page = login_page.Login_page(self.driver)
        Login_page.emailAddressField("rohit@yopmail.com")
        Login_page.passwordField("Kiwi@2018")
        Login_page.loginButton()
        time.sleep(2)
        current_url = setup.driver.current_url
        # Assert the current URL matches the expected URL after successful login
        assert current_url == "https://odin-web-qa.kiwi-internal.com/dealer/sites", "URL did not match after login"

    def test_loginWithInValidCredentials(self):
        fake = Faker()
        Login_page = login_page.Login_page(self.driver)
        Login_page.emailAddressField(fake.email())
        Login_page.passwordField(fake.password())
        Login_page.loginButton()
        time.sleep(2)
        current_url = setup.driver.current_url
        # Assert the current URL matches the expected URL after successful login
        assert current_url != "https://odin-web-qa.kiwi-internal.com/dealer/sites", "URL did not match after login"