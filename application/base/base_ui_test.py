import pytest
from utils.config import Config
# from webdriver_manager.chrome import ChromeDriverManager
from application.pages import Pages


@pytest.mark.usefixtures("driver")
class BaseTest(object):

    def get_url(self):
        return self.driver.get(Config.app_url)

    @property
    def pages(self):
        return Pages(self.driver)

    # @pytest.fixture
    # def login_to_jira(self):
    #     blabla.login()

