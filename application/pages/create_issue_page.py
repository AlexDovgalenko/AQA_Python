from application.base.base_page import BasePage
from application.pages.dashboard_page import DashboardPage
from ..elements.create_issue_page_elements import CreateUpdateIssuePageElements
from utils.common_utils import get_current_datetime_str
from selenium.webdriver.common.keys import Keys


global_date_time = ''


class CreateUpdateIssuePage(BasePage):
    def __init__(self, driver):
        super(CreateUpdateIssuePage, self).__init__(driver)
        self.elements = CreateUpdateIssuePageElements(driver)

    def is_create_issue_page(self):
        return self.elements.create_issue_page_title.is_visible()

    def enter_project(self, project):
        self.elements.project_dropdown.wait_to_be_visible().click()
        # self.elements.project_dropdown.fill_with(project)
        # self.elements.project_dropdown.elem.send_keys(Keys.ENTER)
        self.elements.project_dropdown.fill_with(project, clear=True, keys='RETURN')
        return self

    def enter_issue_type(self, issuetype):
        self.elements.issue_type_dropdown.wait_to_be_visible().context.wait_to_be_visible().click()
        self.elements.issue_type_dropdown.fill_with(issuetype, clear=True, keys=Keys.ENTER)
        return self

    def enter_summary(self, summary):
        date_time = get_current_datetime_str()
        global global_date_time
        global_date_time = date_time
        summary_res = summary % date_time
        self.elements.summary_field.wait_to_be_visible().context.wait_to_be_visible().click()
        self.elements.summary_field.fill_with(summary_res)
        return self

    def enter_description(self, description):
        self.elements.description_field.wait_to_be_visible().click()
        self.elements.description_field.fill_with(description)
        return self

    def submit_issue(self):
        return self.elements.create_btn.wait_to_be_visible().click()

    def create_new_issue(self, project, issue_type, summary, description):
        self.enter_project(project)
        self.enter_issue_type(issue_type)
        self.enter_summary(summary)
        self.elements.description_text_tab.click()
        self.enter_description(description)
        self.submit_issue()
        return self

    def get_global_date_time(self):
        return global_date_time