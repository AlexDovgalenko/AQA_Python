import logging
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
# logger = logging.getLogger()


@pytest.fixture(scope='session', autouse=True)
def logger():
    import logging.config
    logging.config.fileConfig('../../logging.ini')
    return logging.getLogger()

@pytest.fixture(scope='session')
def test_create_issue_api(logger):
    datetime = common_utils.get_current_datetime_str()
    payload = '{"fields": {"project":{"key": "AQAPYTHON"},"summary": "AQAPYTHON -- %s -- API test issue by AlexDovgalenko","description": "This issue have been created via Jira REST API for testing purposes in terms of AqAPython project","issuetype": {"name": "Bug"}}}'
    payload_fin = payload % datetime
    r = requests.request("POST", baseUrl+api_url+"/issue", data=payload_fin, headers=headers, auth=(username, password))
    if r.status_code == 201:
        issue_id = r.json()['id']
        logger.debug("Test Issue Has been created with Issue_ID {}".format(issue_id))
    else:
        logger.debug("Test issue has not been created, check JIRA availability.")
    return issue_id