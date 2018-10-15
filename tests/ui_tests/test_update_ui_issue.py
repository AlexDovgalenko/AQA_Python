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


@allure.story("Update Jira Issue in UI")
class TestUpdateJiraIssue(BaseTest):

    # @pytest.mark.skip
    @allure.title("Update Issue summary via UI")
    @pytest.mark.flaky(reruns=3)
    def test_update_issue_summary(self, login_to_jira):
        common_utils.delete_all_my_issues(Config.username)
        common_utils.create_issue_api()
        updated_summary = common_utils.get_field_to_update('summary')

        with step("Navigate to the \"Reported by Me\" issues page"):
            self.pages.dashboard_page.go_to_reported_by_me()
            self.pages.dashboard_page.is_reported_by_me_page()

        with step("Try to update issue summary from original value to [{}]".format(updated_summary)):
            self.pages.dashboard_page.update_first_issue_summary(updated_summary)
            self.pages.dashboard_page.reload()
            time.sleep(2)
            self.pages.dashboard_page.is_dashboard_page()
            self.pages.dashboard_page.elements.first_issue_in_list_sumary.click()
            self.pages.dashboard_page.elements.first_issue_in_list_sumary.is_visible()

            assert_that(self.pages.dashboard_page.get_first_issue_summary(),  updated_summary), "Issue summary [{}] after update is not equal to expected summary value [{}]".format(self.pages.dashboard_page.get_first_issue_summary(),  updated_summary)

    @allure.title("Update Issue severity via UI")
    def test_update_issue_severity(self, login_to_jira):
        common_utils.delete_all_my_issues(Config.username)
        common_utils.create_issue_api()
        updated_severity = common_utils.get_field_to_update('severity')

        with step("Navigate to the \"Reported by Me\" issues page"):
            self.pages.dashboard_page.go_to_reported_by_me()
            self.pages.dashboard_page.is_reported_by_me_page()

        with step("Try to update issue severity from original value to [{}]".format(updated_severity)):
            self.pages.dashboard_page.update_first_issue_severity()
            self.pages.dashboard_page.reload()
            time.sleep(1)
            self.pages.dashboard_page.elements.severity_edit_val.wait_to_be_visible()
            self.pages.dashboard_page.elements.first_issue_in_list_sumary.wait_to_be_visible().click()
            time.sleep(1)
            actual_severity = self.pages.dashboard_page.elements.severity_edit_val.wait_to_be_visible().extract_text()
            assert_that(actual_severity,  updated_severity), "Issue severity [{}] after update is not equal to expected value [{}]".format(actual_severity,  updated_severity)
