from application.base.base_page import BasePage
from ..elements.dashboard_page_elements import DashboardPageElements
from .. elements.login_page_elements import LoginPageElements


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
        self.is_dashboard_page()
        self.elements.issues_dropdown.wait_to_be_clickable()
        self.elements.issues_dropdown.wait_to_be_visible().context.wait_to_be_visible().click()
        self.elements.issues_dropdown_reported_by_me.move_to().context.wait_to_be_visible().click()
        return self


