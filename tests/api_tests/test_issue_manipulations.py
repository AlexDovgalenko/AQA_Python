import requests
from configurations import config
from utils import common_utils
import logging
import pytest
import os.path

@allure.story("Testing Jira issues manipulations via API")
class TestIssueManipulations:

    # os.path.dirname('../../__file__')

    # logger = logging.getLogger()
    baseUrl = config.Config.JIRA_BASE_URL
    api_url = config.Config.JIRA_REST_API_URL
    username = config.Config.JIRA_USERNAME
    password = config.Config.JIRA_PASS
    headers = {
        'Content-Type': "application/json",
        }
    # global variable to store Issue ID created in JIRA
    issue_id = []

    @pytest.fixture(scope='session', autouse=True)
    def payload_type(payload_type):
        my_path = os.path.abspath(os.path.dirname('__file__'))
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
        for x in range(len(self.issue_id)):
            requests.request("DELETE", self.baseUrl+self.api_url+"/issue/"+self.issue_id[x], headers=self.headers, auth=(self.username, self.password))
            print("deleting issue with ID: {}".format(self.issue_id[x]))

    @allure.title("Create Jira issue via API")
    @pytest.mark.parametrize("payload, expected_status_code", payload_type("create"))
    def test_create_issue(self, payload, expected_status_code):
        datetime = common_utils.get_current_datetime_str()
        payload_fin = payload % datetime
        r = requests.request("POST", self.baseUrl+self.api_url+"/issue", data=payload_fin, headers=self.headers, auth=(self.username, self.password))
        assert r.status_code == int(expected_status_code), "Status code {0} is no match to the expected Status code {1} on attempt of creating issue".format(r.status_code, int(expected_status_code))
        if 'id' in r.json():
            global issue_id
            self.issue_id.append(r.json()['id'])

    @allure.title("Update Jira issue via API")
    @pytest.mark.parametrize("payload, expected_status_code", payload_type("update"))
    def test_update_issue(self, payload, expected_status_code, test_create_issue_api):
        issue_id = test_create_issue_api
        r = requests.request("PUT", self.baseUrl+self.api_url+'/issue/'+issue_id, data=payload, headers=self.headers, auth=(self.username, self.password))
        assert r.status_code == int(expected_status_code), "Status code {0} is no match to the expected Status code {1} on attempt of updating issue".format(r.status_code, int(expected_status_code))

    @allure.title("Search for issues in Jira via API")
    @pytest.mark.parametrize("payload, expected_status_code", payload_type("search"))
    def test_search_for_issue(self, payload, expected_status_code):
        r = requests.request("POST", self.baseUrl+self.api_url+'/search', data=payload, headers=self.headers, auth=(self.username, self.password))
        assert r.status_code == int(expected_status_code), "Status code {0} is no match to the expected Status code {1} on attempt of searching for issues".format(r.status_code, int(expected_status_code))
