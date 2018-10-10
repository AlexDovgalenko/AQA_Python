from application.pages.login_page import LoginPage
from application.pages.create_issue_page import CreateUpdateIssuePage
from application.pages.dashboard_page import DashboardPage


class Pages(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def login_page(self):
        return LoginPage(self.driver)

    @property
    def create_issue_page(self):
        return CreateUpdateIssuePage(self.driver)

    @property
    def dashboard_page(self):
        return DashboardPage(self.driver)



