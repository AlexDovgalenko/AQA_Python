from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_name_txt = (By.XPATH, '//*[@id="login-form-username"]')
    user_pwd_txt = (By.XPATH, '//*[@id="login-form-password"]')
    log_in_btn = (By.XPATH, '//*[@id="login"]')
    login_container = (By.CLASS_NAME, '//*[@class="dashboard-item-content "]')
    login_error_message = (By.XPATH, '//*[@id="usernameerror"]')
    user_profile_icon = (By.XPATH, '// *[ @ id = "header-details-user-fullname"]')




