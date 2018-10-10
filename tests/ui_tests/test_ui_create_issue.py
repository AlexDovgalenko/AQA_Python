import allure
import pytest
from hamcrest import assert_that, is_in
from utils import common_utils
from application.pages import Pages
from application.base.base_ui_test import BaseTest
from utils.config import Config
import os.path

from selenium.webdriver.common.keys import Keys
import time

step = allure.step

# my_path = os.path.abspath(os.path.dirname('__file__'))
# path = os.path.join(my_path, "test_data/csv/create_issue_positive.csv")


@allure.story("Create Jira Issue")
# @pytest.mark.usefixtures("login_to_jira")
class TestCreateJiraIssue(BaseTest):

    @pytest.fixture()
    def get_issue_params(type_of_test):
        my_path = os.path.abspath(os.path.dirname('__file__'))
        issue = []
        if type_of_test == 'positive':
            path = os.path.join(my_path, "test_data/csv/create_issue_positive.csv")
            issue = common_utils.read_issue_data_from_csv(path)
        elif type_of_test == 'negative':
            path  = os.path.join(my_path, "test_data/csv/create_issue_negative.csv")
            issue = common_utils.read_issue_data_from_csv(path)
        return issue


    @pytest.mark.parametrize("project, summary, description, issuetype, error_message", get_issue_params('negative'))
    def test_create_new_issue_ui_negative(self, project, summary, description, issuetype, error_message, login_to_jira):
        # self.driver.get(Config.base_url)
        # self.login_to_jira()
        with step("Navigate to the \"Reported by Me\" issues page"):
            self.pages.dashboard_page.go_to_reported_by_me()
            self.pages.dashboard_page.is_reported_by_me_page()

        with step("Try to create issue {} in project {}, with fillowing summary {}".format(issuetype, project, summary)):
            self.pages.dashboard_page.elements.create_btn.wait_to_be_visible().click()
            self.pages.create_issue_page.is_create_issue_page()
            self.pages.create_issue_page.create_new_issue(project, issuetype, summary, description)
            assert_that(self.pages.create_issue_page.elements.summary_error_message.extract_text(),  error_message)


    @pytest.mark.parametrize("project, summary, description, issuetype",  get_issue_params('positive'))
    def test_create_new_issue_ui_positive(self, project, summary, description, issuetype, login_to_jira):
        # self.driver.get(Config.base_url)
        # self.login_to_jira()
        with step("Navigate to the \"Reported by Me\" issues page"):
            self.pages.dashboard_page.go_to_reported_by_me()
            self.pages.dashboard_page.is_reported_by_me_page()

        with step("Try to create issue {} in project {}, with fillowing summary {}".format(issuetype, project, summary)):
            self.pages.dashboard_page.elements.create_btn.wait_to_be_visible().click()
            self.pages.create_issue_page.is_create_issue_page()
            self.pages.create_issue_page.create_new_issue(project, issuetype, summary, description)
            self.pages.dashboard_page.go_to_reported_by_me()
            self.pages.dashboard_page.is_reported_by_me_page()
            assert_that(self.pages.create_issue_page.get_global_date_time() in self.pages.dashboard_page.get_first_issue_summary())


