import requests
from configurations import config
from utils import common_utils
import logging
import pytest
import os.path

logger = logging.getLogger()
baseUrl = config.Config.JIRA_BASE_URL
api_url = config.Config.JIRA_REST_API_URL
username = config.Config.JIRA_USERNAME
password = config.Config.JIRA_PASS
headers = {
    'Content-Type': "application/json",
    }
my_path = os.path.abspath(os.path.dirname('../../__file__'))
path_to_payload_create = os.path.join(my_path, "test_data/jsons/create_issue_payloads")


@pytest.mark.parametrize("payload, expected_status_code", common_utils.read_issue_data_from_csv(path_to_payload_create))
def test_create_issue(payload, expected_status_code):
    print(payload)
    r = requests.request("POST", baseUrl+api_url, data=payload, headers=headers, auth=(username, password))
    assert r.status_code == int(expected_status_code)
