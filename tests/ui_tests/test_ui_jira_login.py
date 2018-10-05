import allure
import pytest
from hamcrest import assert_that, is_in
from application.pages import Pages
from application.base.base_ui_test import BaseTest
from utils.config import Config

step = allure.step


@allure.story("Login to JIRA via UI")
class TestLoginToJira(BaseTest):

    username = Config.username
    password = Config.password
    expected_login_error_message = "Sorry, your username and password are incorrect - please try again."

    @pytest.mark.parametrize("user_name, pass_word", [

        ("", password),
        (username, ""),
        ("wrong_user", password),
        (username, "wrong_pass")
        ])
    def test_negative_login_to_jira(self, user_name, pass_word):
        self.driver.get(Config.base_url)

        with step("Try to login to Jira wit {} username and {} password".format(user_name, pass_word)):
            self.pages.login_page.fill_username(user_name)
            self.pages.login_page.fill_password(pass_word)
            self.pages.login_page.submit()

        assert_that(self.pages.login_page.elements.login_error_message_container.extract_text(), self.expected_login_error_message)


    @pytest.mark.parametrize("user_name, pass_word", [(username, password)])
    def test_positive_login_to_jira(self, user_name, pass_word, logger):
        self.pages.login_page.fill_username(user_name)
        self.pages.login_page.fill_password(pass_word)
        self.pages.login_page.submit()

        assert self.pages.login_page.user_profile()

