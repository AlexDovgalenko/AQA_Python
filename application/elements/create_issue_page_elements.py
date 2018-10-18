from application.base.base_element import Element, BasePageElement
from application.locators.create_issue_page_locators import CreateUpdateIssuePageLocators


class CreateUpdateIssuePageElements(BasePageElement):

    @property
    def create_issue_page_title(self):
        return Element(CreateUpdateIssuePageLocators.create_issue_title)

    @property
    def project_dropdown_arrow(self):
        return Element(CreateUpdateIssuePageLocators.project_dropdown_arrow)

    @property
    def project_dropdown(self):
        return Element(CreateUpdateIssuePageLocators.project_dropdown)

    @property
    def issue_type_dropdown_arrow(self):
        return Element(CreateUpdateIssuePageLocators.issue_type_dropdown_arrow)

    @property
    def issue_type_dropdown(self):
        return Element(CreateUpdateIssuePageLocators.issue_type_dropdown)

    @property
    def summary_field(self):
        return Element(CreateUpdateIssuePageLocators.summary_field)

    @property
    def description_text_tab(self):
        return Element(CreateUpdateIssuePageLocators.description_text_tab)

    @property
    def description_field(self):
        return Element(CreateUpdateIssuePageLocators.description_field)

    @property
    def create_btn(self):
        return Element(CreateUpdateIssuePageLocators.create_button)

    @property
    def summary_error_message(self):
        return Element(CreateUpdateIssuePageLocators.summary_error_message)