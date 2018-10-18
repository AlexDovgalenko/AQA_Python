from application.base.base_page import BasePage
from ..elements.dashboard_page_elements import DashboardPageElements
from .. elements.login_page_elements import LoginPageElements
from selenium.webdriver.common.keys import Keys
import time


class DashboardPage(BasePage):
    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)
        self.elements = DashboardPageElements(driver)

    def is_dashboard_page(self):
        return self.elements.user_profile_icon.is_visible()

    def is_reported_by_me_page(self):
        return self.elements.reported_by_me_label.wait_to_be_visible().is_visible()

    def get_first_issue_summary(self):
        return self.elements.first_issue_in_list_sumary.wait_to_be_visible().extract_text()

    def go_to_reported_by_me(self):
        self.wait_for_ajax()
        self.is_dashboard_page()
        self.elements.issues_dropdown.wait_to_be_clickable().context.wait_to_be_visible().click()
        self.wait_for_ajax()
        self.elements.issues_dropdown_reported_by_me.move_to().context.wait_to_be_visible().click()
        return self

    def go_to_search_page(self):
        self.is_dashboard_page()
        self.elements.issues_dropdown.wait_to_be_clickable()
        self.elements.issues_dropdown.wait_to_be_visible().context.wait_to_be_visible().click()
        self.elements.search_for_issues_menu_item.move_to().context.wait_to_be_visible().click()
        return self

    def update_first_issue_summary(self, summary):
        self.is_dashboard_page()
        self.elements.summary_edit_btn.wait_to_be_visible().context.hover().click()
        self.elements.summary_edit_fld.wait_to_be_clickable().context.wait_to_be_visible().click()
        self.elements.summary_edit_fld.wait_to_be_visible().fill_with(summary, clear=True)
        self.elements.summary_submit_btn.wait_to_be_clickable().context.wait_to_be_visible().click()
        self.elements.summary_edit_btn.wait_to_be_visible()
        return self

    def update_first_issue_severity(self):
        self.is_dashboard_page()
        self.elements.severity_edit_val.wait_to_be_visible().context.hover().click()
        self.elements.severity_list_item.wait_to_be_visible().move_to()
        self.elements.severity_list_item.wait_to_be_clickable().context.click()
        self.wait_for_ajax()
        self.elements.severity_submit_btn.wait_to_be_clickable().context.click()
        
        return self

    def search_for_issue_with_summary(self, summary):
        self.is_dashboard_page()
        self.elements.search_issue_field.wait_to_be_visible().click()
        self.elements.search_issue_field.wait_to_be_visible().fill_with(summary, clear=True)
        self.elements.search_issue_btn.wait_to_be_visible().click()

