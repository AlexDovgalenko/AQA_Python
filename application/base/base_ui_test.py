import pytest
from utils.config import Config
from application.pages import Pages


@pytest.mark.usefixtures("driver")
class BaseTest(object):

    def get_url(self):
        return self.driver.get(Config.base_url)

    @property
    def pages(self):
        return Pages(self.driver)

    @pytest.fixture()
    def login_to_jira(self, driver):
        driver.get(Config.base_url)
        self.pages.login_page.elements.user_name.wait_to_be_visible().fill_with("Alexander_Dovgalenko")
        self.pages.login_page.elements.user_password.wait_to_be_visible().fill_with("test_pass")
        self.pages.login_page.elements.login_btn.wait_to_be_visible().click()
        return self




