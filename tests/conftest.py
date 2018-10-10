import logging
import requests
from utils.config import Config
from utils import common_utils
from application.pages import LoginPage, DashboardPage
from application.elements.login_page_elements import LoginPageElements
import pytest
import os.path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


base_url = Config.base_url
api_url = Config.api_url
username = Config.username
password = Config.password
headers = {
    'Content-Type': "application/json",
}
# logger = logging.getLogger()


@pytest.fixture(scope='session', autouse=True)
def logger():
    import logging.config
    logging.config.fileConfig('logging.ini')
    return logging.getLogger()


@pytest.fixture(scope='session')
def test_create_issue_api(logger):
    datetime = common_utils.get_current_datetime_str()
    payload = '{"fields": {"project":{"key": "AQAPYTHON"},"summary": "AQAPYTHON -- %s -- API test issue by AlexDovgalenko","description": "This issue have been created via Jira REST API for testing purposes in terms of AqAPython project","issuetype": {"name": "Bug"}}}'
    payload_fin = payload % datetime
    r = requests.request("POST", base_url + api_url + "/issue", data=payload_fin, headers=headers, auth=(username, password))
    if r.status_code == 201:
        issue_id = r.json()['id']
        logger.debug("Test Issue Has been created with Issue_ID {}".format(issue_id))
    else:
        logger.debug("Test issue has not been created, check JIRA availability.")
    return issue_id


# @pytest.fixture()
# def chose_browser(request):
#     d = None
#     time.sleep(3)
#     if Config.browser == 'chrome':
#         options = webdriver.ChromeOptions()
#         if Config.headless:
#             options.add_argument("--headless")
#         if Config.fullscreen:
#             options.add_argument("--kiosk")
#         options.add_argument("--no-sandbox")
#         options.add_argument('--ignore-certificate-errors')
#         options.add_argument("--disable-popup-blocking")
#
#         d = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
#                              desired_capabilities=options.to_capabilities())
#
#     elif Config.browser == 'firefox':
#         d = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#     request.addfinalizer(lambda *args: d.quit())
#     return d
#
#
# @pytest.fixture()
# def driver(request, chose_browser):
#     d = chose_browser
#     if not Config.fullscreen:
#         RESOLUTIONS = {"720p": (1280, 720), "1080p": (1920, 1080)}
#         res = RESOLUTIONS[Config.browser_resolution]
#         d.set_window_size(*res)
#     request.instance.driver = d
#     return d


@pytest.fixture(scope="function")
def up_browser(request):
    """ SetUp/TearDown selenium driver """


    if Config.browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('headless')

        d = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                             desired_capabilities=options.to_capabilities())


    elif Config.browser == 'firefox':
        d = webdriver.Firefox(executable_path=GeckoDriverManager().install())


    elif Config.browser == 'ie11':
        caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
        caps['ignoreZoomSettings'] = 'true'
        caps['ignoreProtectedModeSettings'] = 'true'
        d = webdriver.Ie(executable_path=IEDriverManager().install(), capabilities=caps)

    elif Config.browser == 'edge':
        caps = webdriver.DesiredCapabilities.EDGE
        caps['nativeEvents'] = 'true'
        caps['acceptSslCerts'] = 'true'
        caps['javascriptEnabled'] = 'true'
        caps['takes_screenshot'] = 'true'
        caps['cssSelectorEnabled'] = 'true'
        caps['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = 'true'
        d = webdriver.Edge(executable_path=EdgeDriverManager().install(), capabilities=caps)

    else:

        sys.exit(1)

    request.addfinalizer(lambda *args: d.quit())
    return d


@pytest.fixture()
def driver(request, up_browser):
    """
    Set up a single session for these tests.
    """

    RESOLUTIONS = {"HD": (1280, 750), "FullHD": (1920, 1080), "UHD": (2890, 1560)}

    d = up_browser

    res = RESOLUTIONS['HD']
    if RESOLUTIONS.get(Config.browser_resolution):
        res = RESOLUTIONS[Config.browser_resolution]

    d.set_window_size(*res)

    request.instance.driver = d

    return d



#
# @pytest.fixture()
# def login_to_jira(driver):
#     driver.get(Config.base_url)
#     LoginPage.login_as(self, Config.username, Config.password)
#     # return DashboardPage



