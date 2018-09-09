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

issues_id_list = []

@pytest.mark.parametrize("payload, expected_status_code", common_utils.read_issue_data_from_csv(path_to_payload_create))
def test_create_issue(payload, expected_status_code):
    # print(type(common_utils.get_current_datetime_str()))
    # print(common_utils.get_current_datetime_str())
    # print(type(payload))
    datetime = common_utils.get_current_datetime_str()
    payload_fin = payload % datetime
    # print("payload is: " + payload)
    # print("formatted payload is: " + payload_fin)
    r = requests.request("POST", baseUrl+api_url, data=payload_fin, headers=headers, auth=(username, password))
    assert r.status_code == int(expected_status_code)
    if 'id' in r.json():
        issues_id_list.append(r.json()['id'])


# @pytest.mark.parametrize("payload, expected_status_code", common_utils.read_issue_data_from_csv(path_to_payload_update))
# @pytest.mark.parametrize("issues_id_list", issues_id_list)
# def test_update_issue(issues_id_list, payload, expected_status_code):
#     r = requests.request("POST", baseUrl+api_url, data=payload, headers=headers, auth=(username, password))
#     assert r.status_code == int(expected_status_code)
