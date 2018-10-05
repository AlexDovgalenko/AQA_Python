
from application.base.base_element import Element, BasePageElement
from application.locators.login_page_locators import LoginPageLocators


class LoginPageElements(BasePageElement):

    @property
    def user_name(self):
        return Element(LoginPageLocators.user_name_txt)

    @property
    def user_password(self):
        return Element(LoginPageLocators.user_pwd_txt)

    @property
    def login_btn(self):
        return Element(LoginPageLocators.log_in_btn)

    @property
    def login_container(self):
        return Element(LoginPageLocators.login_container)

    @property
    def login_error_message_container(self):
        return Element(LoginPageLocators.login_error_message)

    @property
    def user_frofile_icon(self):
        return Element(LoginPageLocators.user_profile_icon)