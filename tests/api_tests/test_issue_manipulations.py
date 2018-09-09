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
path_to_payload_update = os.path.join(my_path, "test_data/jsons/update_issue_payloads")
path_to_payload_search = os.path.join(my_path, "test_data/jsons/search_issue_payloads")

# global variable to store Issue ID created in JIRA
issue_id = ''


@pytest.mark.parametrize("payload, expected_status_code", common_utils.read_issue_data_from_csv(path_to_payload_create))
def test_create_issue(payload, expected_status_code):
    datetime = common_utils.get_current_datetime_str()
    payload_fin = payload % datetime
    r = requests.request("POST", baseUrl+api_url+"/issue", data=payload_fin, headers=headers, auth=(username, password))
    assert r.status_code == int(expected_status_code)
    if 'id' in r.json():
        global issue_id
        issue_id = r.json()['id']


@pytest.mark.parametrize("payload, expected_status_code", common_utils.read_issue_data_from_csv(path_to_payload_update))
def test_update_issue(payload, expected_status_code):
    global issue_id
    r = requests.request("PUT", baseUrl+api_url+'/issue/'+issue_id, data=payload, headers=headers, auth=(username, password))
    assert r.status_code == int(expected_status_code)


@pytest.mark.parametrize("payload, expected_status_code", common_utils.read_issue_data_from_csv(path_to_payload_search))
def test_search_for_issue(payload, expected_status_code):
    r = requests.request("POST", baseUrl+api_url+'/search', data=payload, headers=headers, auth=(username, password))
    assert r.status_code == int(expected_status_code)
