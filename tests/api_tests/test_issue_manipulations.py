import requests
from configurations import config
from utils import common_utils
# import logging
import pytest
import os.path


class TestIssueManipulations():

    os.path.dirname('../../__file__')

    # logger = logging.getLogger()
    baseUrl = config.Config.JIRA_BASE_URL
    api_url = config.Config.JIRA_REST_API_URL
    username = config.Config.JIRA_USERNAME
    password = config.Config.JIRA_PASS
    headers = {
        'Content-Type': "application/json",
        }
    # global variable to store Issue ID created in JIRA
    issue_id = ''

    @pytest.fixture(scope='module', autouse=True)
    def payload_type(payload_type):
        my_path = os.path.abspath(os.path.dirname('../../__file__'))
        payload = []
        if payload_type == 'create':
            path = os.path.join(my_path, "test_data/jsons/create_issue_payloads")
            payload = common_utils.read_issue_data_from_csv(path)
        elif payload_type == 'update':
            path  = os.path.join(my_path, "test_data/jsons/update_issue_payloads")
            payload = common_utils.read_issue_data_from_csv(path)
        elif payload_type == 'search':
            path = os.path.join(my_path, "test_data/jsons/search_issue_payloads")
            payload = common_utils.read_issue_data_from_csv(path)
        return payload

    def teardown_class(self):
        # logger.debug("deleting issue with ID: {}".format(issue_id))
        requests.request("DELETE", self.baseUrl+self.api_url+"/issue/"+issue_id, headers=self.headers, auth=(self.username, self.password))

    @pytest.mark.parametrize("payload, expected_status_code", payload_type("create"))
    def test_create_issue(self, payload, expected_status_code):
        datetime = common_utils.get_current_datetime_str()
        payload_fin = payload % datetime
        r = requests.request("POST", self.baseUrl+self.api_url+"/issue", data=payload_fin, headers=self.headers, auth=(self.username, self.password))
        assert r.status_code == int(expected_status_code)
        if 'id' in r.json():
            global issue_id
            issue_id = r.json()['id']

    @pytest.mark.dependency(depends = ['test_create_issue'])
    @pytest.mark.parametrize("payload, expected_status_code", payload_type("update"))
    def test_update_issue(self, payload, expected_status_code):
        global issue_id
        r = requests.request("PUT", self.baseUrl+self.api_url+'/issue/'+issue_id, data=payload, headers=self.headers, auth=(self.username, self.password))
        assert r.status_code == int(expected_status_code)

    @pytest.mark.parametrize("payload, expected_status_code", payload_type("search"))
    def test_search_for_issue(self, payload, expected_status_code):
        r = requests.request("POST", self.baseUrl+self.api_url+'/search', data=payload, headers=self.headers, auth=(self.username, self.password))
        assert r.status_code == int(expected_status_code)
