from application.base.base_element import Element, BasePageElement
from application.locators.dashboard_page_locators import DashboardPageLocators


class DashboardPageElements(BasePageElement):

    @property
    def user_profile_icon(self):
        return Element(DashboardPageLocators.user_profile_icon)

    @property
    def create_btn(self):
        return Element(DashboardPageLocators.create_btn)

    @property
    def assign_to_me_lnk(self):
        return Element(DashboardPageLocators.assign_to_me_link)

    @property
    def first_issue_in_list(self):
        return Element(DashboardPageLocators.first_issue_in_list)

    @property
    def first_issue_in_list_sumary(self):
        return Element(DashboardPageLocators.first_issue_in_list_summary)

    @property
    def issues_dropdown(self):
        return Element(DashboardPageLocators.issues_droprown)

    @property
    def issues_dropdown_reported_by_me(self):
        return Element(DashboardPageLocators.issues_dropdown_reported_by_me)

    @property
    def reported_by_me_label(self):
        return Element(DashboardPageLocators.reported_by_me_label)

    @property
    def search_issue_btn(self):
        return Element(DashboardPageLocators.search_issue_btn)

    @property
    def search_issue_field(self):
        return Element(DashboardPageLocators.search_issue_field)

    @property
    def search_issues_list_item(self):
        return Element(DashboardPageLocators.search_issues_list_item)
