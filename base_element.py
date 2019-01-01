from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_page import *


class BaseElement:
    """ Basic class that is initialized on all page objects"""
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        self.set_element()

    def set_element(self):
        """Sets elements based on given locators"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def input_text(self, txt):
        """Method allows sending text to input fields"""
        self.web_element.send_keys(txt)
        return None

    def click_element(self):
        """Method which allows clicking elements based on given locators"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None
