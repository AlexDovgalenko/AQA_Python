import requests
from configurations import config
from utils.common_utils import get_issue_list_by_user_id
import pytest
import os.path
import allure

step = allure.step
os.path.dirname('../../__file__')

baseUrl = config.Config.JIRA_BASE_URL
api_url = config.Config.JIRA_REST_API_URL
username = config.Config.JIRA_USERNAME
password = config.Config.JIRA_PASS
headers = {
    'Content-Type': "application/json",
}


@allure.story("Testing Jira issues deletion via API")
@allure.title("Delete all issues , created by certain user via API")
@pytest.mark.parametrize("issue_id", get_issue_list_by_user_id(username))
def test_delete_issues(issue_id, logger):
    """
    Comment "@pytest.mark.skip" decorator for "test_delete_issues" to delete all issues created by desired username
    """
    with step("Delete all issues , created by certain user via API"):
        global username
        requests.request("DELETE", baseUrl+api_url+"/issue/"+issue_id, headers=headers, auth=(username, password))
        logger.debug("deleting issue with ID# {}".format(issue_id))
