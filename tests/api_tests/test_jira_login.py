import requests
from configurations import config
from utils import common_utils
import pytest
import os.path

@allure.story("Testing login to Jira via API")
class TestLoginToJira:

    os.path.dirname('../../__file__')

    baseUrl = config.Config.JIRA_BASE_URL
    username = config.Config.JIRA_USERNAME
    password = config.Config.JIRA_PASS
    headers = {
        'Content-Type': "application/json",
    }

    @allure.title("Test Login to Jira via API")
    @pytest.mark.parametrize("user_name, pass_word, response_code", [
        (username, password, 200),
        ("wrong_user", password, 401),
        (username, "wrong_pass", 401)
        ])
    def test_jira_login(self, user_name, pass_word, response_code, logger):
        logger.debug("USERNAME IS: {}".format(user_name))
        response = requests.request("GET", self.baseUrl, headers=self.headers, auth=(user_name, pass_word))
        logger.debug("RESPONSE STATUS CODE: {}".format(response.status_code))
        logger.debug("EXPECTED STATUS CODE: {}".format(response_code))
        assert response.status_code == response_code, "Actual status code {0} is not equal to expected {1}".format(response.status_code, response_code)

