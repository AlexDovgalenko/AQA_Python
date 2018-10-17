import string
import random
import datetime
import os.path
import requests
import pytest
import logging
import time
from utils.config import Config


baseUrl = Config.base_url
api_url = Config.api_url
username = Config.username
password = Config.password
my_path = os.path.abspath(os.path.dirname('__file__'))
headers = {
        'Content-Type': "application/json",
        }
logger = logging.getLogger()

def rnd_string_gen(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_current_datetime_str():
    return ''.join(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def read_issue_data_from_csv(file_path):
    with open(file_path) as f:
        payloads_data = []
        for row in f:
            payloads_data.append(str(row).rstrip('\n').split('|'))
    return payloads_data


def read_line_from_file(file_path):
    with open(file_path) as f:
        return f.read()


def create_issue_api(issue_count=None):

    path = os.path.join(my_path, "test_data/jsons/create_issue")
    payload = read_line_from_file(path)
    datetime = get_current_datetime_str()
    payload_fin = payload % datetime
    issues_list = []

    if issue_count == None:
        r = requests.request("POST", baseUrl+api_url+"/issue", data=payload_fin, headers=headers, auth=(username, password))
        if 'id' in r.json():
            issues_list.append(r.json()['id'])
    else:
        x = 0
        while x < issue_count:
            r = requests.request("POST", baseUrl + api_url + "/issue", data=payload_fin, headers=headers,
                                 auth=(username, password))
            if 'id' in r.json():
                issues_list.append(r.json()['id'])
                x += 1
    return issues_list


def get_field_to_update(field):
    path = os.path.join(my_path, "test_data/csv/update_issue.csv")
    issues_list = read_issue_data_from_csv(path)
    # type(issues_list)
    # print(issues_list)
    field_value = ''
    if field == 'summary':
        field_value = issues_list[0][1]
    elif field == 'severity':
        field_value = issues_list[1][1]
    elif field == 'assignee':
        field_value = issues_list[2][1]
    return field_value


@pytest.fixture()
def get_issue_list_by_user_id(user_mame):
    payload = '{"jql":"reporter = %s","startAt":0, "maxResults": 1000, "fields":["id"]}' % user_mame
    r = requests.request("POST", baseUrl + api_url + '/search', data=payload, headers=headers, auth=(username, password))
    issue_id_list = []
    for i in r.json().get('issues'):
        issue_id_list.append(i['id'])
    return issue_id_list


@pytest.fixture
def delete_all_my_issues(username):
    """
    Comment "@pytest.mark.skip" decorator for "test_delete_issues" to delete all issues created by desired username
    """
    # global username
    for issue_id in get_issue_list_by_user_id(username):
        requests.request("DELETE", baseUrl+api_url+"/issue/"+issue_id, headers=headers, auth=(username, password))
        # print(issue_id)
        logger.debug("deleting issue with ID# {}".format(issue_id))


if __name__ == '__main__':
    # my_path = os.path.abspath(os.path.dirname('../__file__'))
    # path_to_csv = os.path.join(my_path, "test_data/jsons/create_issue_payloads")
    # print(read_issue_data_from_csv(path_to_csv))
    # print(read_line_from_file(file_path=os.path.join(my_path, "test_data/jsons/create_issue")))
    # print(create_issue_api(5))
    # print(get_field_to_update('assignee'))
    test_delete_issues(username, logger)
