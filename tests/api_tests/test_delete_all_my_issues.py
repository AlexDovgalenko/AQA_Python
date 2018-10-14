import requests
from configurations import config
from utils import common_utils
import pytest
import os.path

os.path.dirname('../../__file__')

baseUrl = config.Config.JIRA_BASE_URL
api_url = config.Config.JIRA_REST_API_URL
username = config.Config.JIRA_USERNAME
password = config.Config.JIRA_PASS
headers = {
    'Content-Type': "application/json",
}
# # global variable to store Issue ID created in JIRA
# issue_id = ''

#
# @pytest.fixture()
# def get_issue_list_by_user_id(user_mame):
#     payload = '{"jql":"reporter = %s","startAt":0, "maxResults": 1000, "fields":["id"]}' % user_mame
#     r = requests.request("POST", baseUrl + api_url + '/search', data=payload, headers=headers, auth=(username, password))
#     issue_id_list = []
#     for i in r.json().get('issues'):
#         issue_id_list.append(i['id'])
#     return issue_id_list



@pytest.mark.parametrize("issue_id", get_issue_list_by_user_id(username))
def test_delete_issues(issue_id, logger):
    """
    Comment "@pytest.mark.skip" decorator for "test_delete_issues" to delete all issues created by desired username
    """
    global username
    requests.request("DELETE", baseUrl+api_url+"/issue/"+issue_id, headers=headers, auth=(username, password))
    logger.debug("deleting issue with ID# {}".format(issue_id))
