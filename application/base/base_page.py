# -*- coding: utf-8 -*-

import configurations.config
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



