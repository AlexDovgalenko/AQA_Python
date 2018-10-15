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


@allure.story("Search for Jira Issues in UI")
class TestSearchJiraIssues(BaseTest):

    @allure.title("Search for a single Issue via UI")
    def test_search_one_issue(self, login_to_jira):
        common_utils.delete_all_my_issues(Config.username)
        common_utils.create_issue_api()
        summary_substring = "API test issue by AlexDovgalenko"

        with step("Navigate to the \"Reported by Me\" issues page"):
            self.pages.dashboard_page.go_to_search_page()

        with step("Try to search for the issue with scecific summary which contains following substring [{}]".format(summary_substring)):
            self.pages.dashboard_page.search_for_issue_with_summary(summary_substring)
            # self.pages.dashboard_page.reload()
            time.sleep(2)
            self.pages.dashboard_page.elements.first_issue_in_list_sumary.click()
            self.pages.dashboard_page.elements.first_issue_in_list_sumary.is_visible()
            assert_that(summary_substring, is_in(self.pages.dashboard_page.get_first_issue_summary())), "Issue summary [{}] is not equal to expected summary value [{}]".format(self.pages.dashboard_page.get_first_issue_summary(),  summary_substring)

    @allure.title("Search for 5 Issues via UI")
    def test_search_5_issues(self, login_to_jira):
        common_utils.delete_all_my_issues(Config.username)
        common_utils.create_issue_api(5)
        summary_substring = "API test issue by AlexDovgalenko"
        issues_summary_list = []
        expected_result_number = 5
        with step("Navigate to the \"Reported by Me\" issues page"):
            self.pages.dashboard_page.go_to_search_page()

        with step("Check number of search result equals 5"):
            # self.pages.dashboard_page.search_for_issue_with_summary(summary_substring)
            self.pages.dashboard_page.is_dashboard_page()
            self.pages.dashboard_page.elements.search_issue_field.wait_to_be_visible().click()
            self.pages.dashboard_page.elements.search_issue_field.wait_to_be_visible().fill_with(summary_substring, clear=True)
            self.pages.dashboard_page.elements.search_issue_btn.wait_to_be_visible().click()
            self.issues_summary_list = self.pages.dashboard_page.elements.search_issue_elements_summary.find_all()
            assert_that(len(self.issues_summary_list), expected_result_number), "Number of search result [{}] is not equall to expected [{}]". format(len(self.issues_summary_list), expected_result_number)

        with step ("Check that summary of each item in search result matches the pattersn [{}]".format(summary_substring)):
            for item in issues_summary_list:
                print(item.extract_text())
                assert_that(item.extract_text(), summary_substring), "Issue summary [{}] is not equal to expected summary value [{}]".format(item.extract_text(), summary_substring)

