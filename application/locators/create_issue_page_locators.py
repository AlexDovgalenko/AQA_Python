from selenium.webdriver.common.by import By


class CreateUpdateIssuePageLocators:
    create_issue_title = (By.XPATH, '//*[@id="create-issue-dialog"]//h2[contains(text(), "Create Issue")]')
    project_dropdown = (By.XPATH, '//*[@id="project-field"]')
    project_dropdown_arrow = (By.XPATH, '//*[@id="project-single-select"]/span')
    issue_type_dropdown = (By.XPATH, '//*[@id="issuetype-field"]')
    issue_type_dropdown_arrow = (By.XPATH, '//*[@id="issuetype-single-select"]/span')
    summary_field = (By.XPATH, '//*[@id="summary"]')
    description_text_tab = (By.XPATH, '//*[@id="description-wiki-edit"]//a[contains(text(), "Text")]')
    description_field = (By.XPATH, '//*[@id="description"]')
    create_button = (By.XPATH, '//*[@id="create-issue-submit"]')
    update_button = (By.XPATH, '//*[@id="update-issue-submit"]')
    summary_error_message = (By.XPATH, '//*[@id="create-issue-dialog"]//div[@class="error"]')


