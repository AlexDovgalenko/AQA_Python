import string
import random
import datetime
import os.path


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

if __name__ == '__main__':
    my_path = os.path.abspath(os.path.dirname('../__file__'))
    path_to_csv = os.path.join(my_path, "test_data/jsons/create_issue_payloads")
    print(read_issue_data_from_csv(path_to_csv))