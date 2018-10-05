from application.base.base_page import BasePage
# from ..elements.login_page_elem import Element


class DashboardPage(BasePage):
    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)
        self.elements = DashboardPageElements(driver)

    def is_dashboard_page(self):
        return self.elements.login_container.is_visible()