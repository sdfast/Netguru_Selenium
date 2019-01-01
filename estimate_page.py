from base_element import *
from locators import *


class EstimatePage(BasePage):
    """Class with all elements located on the estimate page"""
    url = 'https://www.netguru.co/estimate-project'

    @property
    def device_desktop_check(self):
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.DEVICE_DESKTOP_BUTTON[0],
            value=EstimatePageLocators.DEVICE_DESKTOP_BUTTON[1])

    @property
    def device_frontend_check(self):
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.DEVICE_FRONTEND_BUTTON[0],
            value=EstimatePageLocators.DEVICE_FRONTEND_BUTTON[1])

    @property
    def email_input_field(self):
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.EMAIL_INPUT_FIELD[0],
            value=EstimatePageLocators.EMAIL_INPUT_FIELD[1])

    @property
    def first_name_input_field(self):
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.FIRSTNAME_INPUT_FIELD[0],
            value=EstimatePageLocators.FIRSTNAME_INPUT_FIELD[1])

    @property
    def last_name_input_field(self):
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.LASTNAME_INPUT_FIELD[0],
            value=EstimatePageLocators.LASTNAME_INPUT_FIELD[1])

    @property
    def phone_input_field(self):
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.PHONE_INPUT_FIELD[0],
            value=EstimatePageLocators.PHONE_INPUT_FIELD[1])

    @property
    def description_input_field(self):
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.DESCRIPTION_INPUT_FIELD[0],
            value=EstimatePageLocators.DESCRIPTION_INPUT_FIELD[1])
