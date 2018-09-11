import requests
from configurations import config
from utils import common_utils
import pytest
import os.path


class TestLoginToJira:

    os.path.dirname('../../__file__')

    baseUrl = config.Config.JIRA_BASE_URL
    username = config.Config.JIRA_USERNAME
    password = config.Config.JIRA_PASS
    headers = {
        'Content-Type': "application/json",
    }

    @pytest.mark.parametrize("username, password, response_code", [
        (username, password, 200),
        (common_utils.rnd_string_gen(10), password, 401),
        (username, common_utils.rnd_string_gen(10), 401)
        ])
    def test_jira_login(self, username, password, response_code, logger):
        logger.debug("USERNAME IS: {}".format(username))
        response = requests.request("GET", self.baseUrl, headers=self.headers, auth=(username, password))
        logger.debug("RESPONSE STATUS CODE: {}".format(response.status_code))
        logger.debug("EXPECTED STATUS CODE: {}".format(response_code))
        assert response.status_code == response_code

