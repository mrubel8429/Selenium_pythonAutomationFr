from selenium import webdriver
import pytest

from pages.homepage import HomePage
from pages.loginPage import LoginPage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        driver = self.driver
        logout = HomePage(driver)
        logout.click_welcomLink()
        logout.click_logout()
