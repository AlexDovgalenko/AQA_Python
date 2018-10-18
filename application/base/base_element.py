import logging
import time
import selenium.webdriver.support.expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import application.locators as locators
from utils.config import Config

logger = logging.getLogger()



class BasePageElement(object):
    """
    Singleton class for all page elements objects
    """
    __shared_state = {}

    def __init__(self, driver=None):
        self.__dict__ = self.__shared_state
        self.driver = driver or self.__shared_state['driver']
        self.locators = locators
        if '__driver' not in globals():
            globals().update({'__driver': self.driver})
        if globals()['__driver'].session_id != self.driver.session_id:
            globals().update({'__driver': self.driver})


class BaseElement(object):
    def __init__(self):
        # due to BasePageElement is a singleton - it always contains webdriver instance in positive case
        # so we can avoid passing driver instance to all page elements
        self._driver = globals().get('__driver')
        self.elem = None

    @property
    def wd_wait(self):
        return WebDriverWait(self._driver, Config.timeout, 3)

    @property
    def action_chains(self):
        return ActionChains(self._driver)

    def split_locator(self, locator):
        """
        :param locator:
         :type locator list or tuple
        :return:
        """
        self.locator_by = locator[0]
        self.locator_value = locator[1]
        self.locator_description = locator[2] if len(locator) == 3 else ""
        return self

    def clear(self):
        self.elem.clear()


class WebDriverElement(BaseElement):
    def __init__(self, element):
        """
        :param element: selenium WebElement instance
         :type element WebElement
        """
        super(WebDriverElement, self).__init__()
        self.elem = element
        self._driver = self.elem.parent

    def click(self):
        logger.info("Clicking element <{}>".format(self.elem.id))
        self.elem.click()
        logger.info("Element clicked")
        return self

    def submit(self):
        self.elem.submit()
        logger.info("Submitting element {}".format(self.elem.id))
        return self

    def hover(self):
        hover = self.action_chains.move_to_element(self.elem)
        hover.perform()
        return self

    def get_attribute(self, name):
        """
        :param name: name of the attribute
        :type name str
        :rtype: str
        """
        logger.info("Getting attribute {} from element <{}>".format(name, self.elem.id))
        attr = self.elem.get_attribute(name)
        logger.info("Attribute value: {}".format(attr))
        return attr

    def extract_text(self):
        """
        :rtype: basestring
        """
        text = self.elem.text
        logger.debug("Extracted text: {}".format(text))
        return text

    def fill_with(self, text):
        logger.info("Sending text {}".format(text))
        self.elem.send_keys(text)

    def find_in_context_one(self, locator):
        """
        :param locator:
        :type locator list or tuple
        :rtype: WebDriverElement
        """
        return Element(self.elem.find_element(*locator))

    def find_in_context_all(self, locator):
        """
        :param locator:
        :type locator list or tuple
        :rtype: WebDriverElement
        """
        return Element(self.elem.find_elements(*locator))

    def is_selected(self):
        """
        :rtype: bool
        """
        is_selected = self.elem.is_selected()
        logger.info("Element {} is selected: {}".format(self.elem.id, is_selected))
        return is_selected

    def is_visible(self):
        """
        :rtype: bool
        """
        is_visible = self.elem.is_displayed()
        logger.info("Element {} is visible: {}".format(self.elem.id, is_visible))
        return is_visible

    def is_invisible(self):
        try:
            self.elem = WebDriverWait(self._driver, timeout=1, ignored_exceptions=(TimeoutException)).until(
                ec.invisibility_of_element_located((self.locator_by, self.locator_value)))
            if self.elem:
                return self.elem
        except:
            pass
        return False

    def is_enabled(self):
        """
        :rtype: bool
        """
        attr = bool(self.elem.get_attribute('disabled'))
        logger.info("Element {} is enabled: {}".format(self.elem.id, attr))
        return attr

    def wait_to_be_visible(self):
        self.wd_wait.until(lambda d: self.is_visible())
        return self

    def wait_to_be_invisible(self):
        self.wd_wait.until(lambda d: self.is_invisible())
        return self

    def wait_to_be_selected(self):
        self.wd_wait.until(lambda d: self.is_selected())
        return self
    
    def wait_to_be_enabled(self):
        self.wd_wait.until(lambda d: self.is_enabled())
        return self

    def wait_to_be_unselected(self):
        self.wd_wait.until_not(lambda d: self.is_selected())
        return self

    def element_screenshot(self, filename='default.png'):
        self.elem.screenshot(filename)


class LocatorElement(BaseElement):
    def __init__(self, locator):
        super(LocatorElement, self).__init__()
        self.visible = False
        self.locator_by = ""
        self.locator_value = ""
        self.locator_description = ""
        self.split_locator(locator)

    @property
    def context(self):
        return Element(self.elem)

    def is_selected(self):
        self.wait_to_be_visible()
        return self.elem.is_selected()

    def is_visible(self):
        self.wait_to_be_visible()
        return self.visible

    def is_enabled(self):
        self.wait_to_be_visible()
        return self.elem.is_enabled()

    def extract_text(self):
        self.find()
        element_text = self.elem.text
        logger.info("Element <{}> contains text '{}'".format(
            self.locator_description or self.locator_value, element_text))
        return element_text

    def format_locator(self, *args, **kwargs):
        self.locator_value = self.locator_value.format(*args, **kwargs)
        return self

    def find(self):
        logger.debug("Find element <{}>".format(self.locator_description or self.locator_value))
        self.wait_to_be_visible()
        logger.debug("Element found: {}".format(self.visible))
        return self

    def find_all(self):
        logger.info("Finding all <{}> elements on the page".format(self.locator_description or self.locator_value))
        self.wait_to_be_visible()
        elements = self._driver.find_elements(self.locator_by, self.locator_value)
        logger.info("Found {} element[s]".format(len(elements)))
        return Element(elements)

    def click(self, scroll_to=False):
        logger.info("Clicking element <{}>".format(self.locator_description or self.locator_value))
        self.wait_to_be_clickable()
        if scroll_to:
            self.move_to()
        self.elem.click()
        logger.info("Element clicked")

    def submit(self):
        logger.info("Submitting element <{}>".format(self.locator_description or self.locator_value))
        self.find()
        self.elem.submit()
        logger.info("Element submitted!")
        return self

    def fill_with(self, text, clear=False, keys=None):
        logger.info("Fill element <{}> with text '{}'".format(self.locator_description or self.locator_value, text))
        self.wait_to_be_visible()
        if clear:
            self.elem.clear()
            logger.info("Element cleared!")
        self.elem.send_keys(text)
        logger.info("Element filled with text <{}>".format(text))
        if keys is not None:
            self.elem.send_keys(keys)
            logger.info("Send key <{}> to element <{}>"
                        .format(keys,
                                self.locator_description or self.locator_value))
        return self

    def clear(self):
        logger.info("Clear input of element <{}>".format(self.locator_description or self.locator_value))
        self.wait_to_be_visible()
        self.elem.clear()
        logger.info("Element cleared!")
        return self

    def move_to(self):
        self.wait_to_be_visible()
        logger.info("Scrolling to element <{}>".format(self.locator_description or self.locator_value))
        self._driver.execute_script("arguments[0].scrollIntoView(true);", self.elem)
        logger.info("Done")
        return self

    def wait_to_be_visible(self):
        logger.debug("Waiting for element <{}> to be visible".format(self.locator_description or self.locator_value))
        self.elem = self.wd_wait.until(ec.presence_of_element_located((self.locator_by, self.locator_value)))
        self.visible = True
        logger.debug("Element is visible")
        return self

    def wait_to_be_invisible(self):
        logger.debug("Waiting for element <{}> to be visible".format(self.locator_description or self.locator_value))
        self.elem = self.wd_wait.until_not(ec.presence_of_element_located((self.locator_by, self.locator_value)))
        self.visible = False
        logger.debug("Element is visible")
        return self

    def wait_to_be_clickable(self):
        logger.info("Waiting for element <{}> to be clickable".format(self.locator_description or self.locator_value))
        self.elem = self.wd_wait.until(ec.element_to_be_clickable((self.locator_by, self.locator_value)))
        return self


class Element(object):
    """ Factory class for elements """

    def __new__(cls, element_or_locator):
        if isinstance(element_or_locator, list):
            elements_container = []
            if element_or_locator and isinstance(element_or_locator[0], WebElement):
                for element in element_or_locator:
                    elements_container.append(WebDriverElement(element))
            elif element_or_locator and isinstance(element_or_locator[0], (list, tuple)):
                for element in element_or_locator:
                    elements_container.append(LocatorElement(element))
            return elements_container
        elif isinstance(element_or_locator, WebElement):
            return WebDriverElement(element_or_locator)
        else:
            return LocatorElement(element_or_locator)
