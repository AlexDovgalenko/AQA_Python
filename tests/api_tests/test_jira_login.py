import requests
from configurations import config
from utils import common_utils
import logging
import pytest


logger = logging.getLogger()
baseUrl = config.Config.JIRA_BASE_URL
username = config.Config.JIRA_USERNAME
password = config.Config.JIRA_PASS
headers = {
    'Content-Type': "application/json",
    }


@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    import logging.config
    logging.config.fileConfig('../../logging.ini')


@pytest.mark.parametrize("username, password, response_code", [
    (username, password, 200),
    (common_utils.rnd_string_gen(10), password, 401),
    (username, common_utils.rnd_string_gen(10), 401)
    ])
def test_jira_login(username, password, response_code):
    logger.debug("USERNAME IS: {}".format(username))
    response = requests.request("GET", baseUrl, headers=headers, auth=(username, password))
    logger.debug("RESPONSE STATUS CODE: {}".format(response.status_code))
    assert response.status_code == response_code

