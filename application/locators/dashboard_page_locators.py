from selenium.webdriver.common.by import By


class DashboardPageLocators:
    reported_by_me_label = (By.XPATH, '//*[@class="search-title"][contains(text(), "Reported by me")]')
    assign_to_me_link = (By.XPATH, '//*[@id="assign-to-me"]')
    search_issue_field = (By.XPATH, '//*[@id="searcher-query"]')
    search_issue_btn = (By.XPATH, '//*/button/*[contains(text(), "Search")]')
    search_issues_list_item = (By.CLASS_NAME, '//*[@class="list-content"]/ol/li')
    user_profile_icon = (By.XPATH, '// *[ @ id = "header-details-user-fullname"]')
    create_btn = (By.XPATH, '//*[@id="create_link"]')
    issues_droprown = (By.XPATH, '//*[@id="find_link"]')
    issues_dropdown_reported_by_me = (By.XPATH, '//*[@id="filter_lnk_reported_lnk"]')
    first_issue_in_list = (By.XPATH, '//*[@id="content"]//ol[@class="issue-list"]/li[1]')
    first_issue_in_list_summary = (By.XPATH, '//*[@id="content"]//ol[@class="issue-list"]/li[1]/a/span[2]')
