# -*- coding: utf-8 -*-

from utils.config import Config
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def page_title(self):
        return self.driver.title

    def open(self, url):
        return self.driver.get(url)

    def reload(self):
        return self.driver.refresh()
    
    def wait_for_ajax(self):
        wait = WebDriverWait(self.driver, Config.timeout)
        try:
            wait.until(lambda driver: self.driver.execute_script('return jQuery.active') == 0)
            wait.until(lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            pass



