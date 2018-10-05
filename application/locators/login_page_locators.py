from selenium.webdriver.common.by import By


class LoginPageLocators:
    user_name_txt = (By.XPATH, '//*[@id="login-form-username"]')
    user_pwd_txt = (By.XPATH, '//*[@id="login-form-password"]')
    log_in_btn = (By.XPATH, '//*[@id="login"]')
    login_container = (By.CLASS_NAME, '//*[@class="dashboard-item-content "]')
    login_error_message = (By.XPATH, '//*[@id="usernameerror"]')
    user_profile_icon = (By.XPATH, '// *[ @ id = "header-details-user-fullname"]')


class CreateUpdateIssuePageLocators:
    pass


class DashboardPageLocators:
    reported_by_me_label = (By.CLASS_NAME, '//*[@class="search-title"][contains(text(), "Reported by me")]')
    assign_to_me_link = (By.XPATH, '//*[@id="assign-to-me"]')
    search_issue_field = (By.XPATH, '//*[@id="searcher-query"]')
    search_issue_btn = (By.XPATH, '//*/button/*[contains(text(), "Search")]')
    search_issues_list_item = (By.CLASS_NAME, '//*[@class="list-content"]/ol/li')
    user_profile_icon = (By.XPATH, '// *[ @ id = "header-details-user-fullname"]')

