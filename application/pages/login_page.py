from application.base.base_page import BasePage
from application.pages.dashboard_page import DashboardPage
from ..elements.login_page_elements import LoginPageElements
import time


class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.elements = LoginPageElements(driver)
        
    def is_login_page(self):
        return self.elements.login_container.is_visible()
    
    def fill_username(self, text):
        return self.elements.user_name.fill_with(text)
    
    def fill_password(self, text):
        return self.elements.user_password.fill_with(text)
    
    def submit(self):
        return self.elements.login_btn.click()

    def user_profile(self):
        return self.elements.user_frofile_icon.is_visible()

    def login_as(self, username, password):
        self.elements.user_name.fill_with(username)
        self.elements.user_password.fill_with(password)
        self.elements.login_btn.click()
        time.sleep(2)
        return self
