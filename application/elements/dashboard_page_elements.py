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

    @property
    def summary_edit_btn(self):
        return Element(DashboardPageLocators.summary_edit_btn)

    @property
    def summary_edit_fld(self):
        return Element(DashboardPageLocators.summary_edit_fld)

    @property
    def summary_submit_btn(self):
        return Element(DashboardPageLocators.summary_submit_btn)

    @property
    def severity_edit_val(self):
        return Element(DashboardPageLocators.severity_edit_val)

    @property
    def severity_edit_fld(self):
        return Element(DashboardPageLocators.severity_edit_fld)

    @property
    def severity_submit_btn(self):
        return Element(DashboardPageLocators.severity_submit_btn)

    @property
    def severity_list_item(self):
        return Element(DashboardPageLocators.severity_list_item)

    @property
    def search_for_issues_menu_item(self):
        return Element(DashboardPageLocators.search_for_issues_menu_item)

    @property
    def search_issue_elements_summary(self):
        return Element(DashboardPageLocators.search_issue_elements_summary)
    
    @property
    def spinner(self):
        return Element(DashboardPageLocators.spinner)

