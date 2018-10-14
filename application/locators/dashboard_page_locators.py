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
    summary_edit_btn = (By.XPATH, '//*[@id="summary-val"]/span')
    summary_edit_fld = (By.XPATH, '//*[@id="summary"]')
    summary_submit_btn = (By.XPATH, '//*[@id="summary-form"]/div[2]/button[1]')
    severity_edit_val = (By.XPATH, '//*[@id="priority-val"]')
    severity_edit_fld = (By.XPATH, '//*[@id="priority-field"]')
    severity_list_item = (By.XPATH, '//li[starts-with(@id,"blocker-")]')
    severity_submit_btn = (By.XPATH, '//*[@id="priority-form"]/div[2]/button[1]/span')
    search_for_issues_menu_item = (By.XPATH, '//*[@id="issues_new_search_link_lnk"]')
    search_issue_elements_summary = (By.XPATH, '//*[@id="content"]//ol[@class="issue-list"]/li/a/span[2]')
