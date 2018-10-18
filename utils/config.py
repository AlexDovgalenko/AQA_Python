# -*- coding: utf-8 -*-


import configparser
import os


class Config(object):

    config = configparser.ConfigParser()
    config.read('config.ini')

    browser = config.get('TEST', 'browser')
    browser_resolution = config.get('TEST', 'browser_resolution')
    headless = config.getboolean('TEST', 'headless')
    fullscreen = config.getboolean('TEST', 'fullscreen')

    # protocol = config.get('ENV', 'protocol')
    base_url = config.get('ENV', 'jira_base_url')
    api_url = config.get('ENV', 'jira_api_url')
    username = config.get('ENV', 'username')
    password = config.get('ENV', 'password')
    timeout = config.getint('BASE', 'timeout')
