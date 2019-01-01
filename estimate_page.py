from base_element import *
from locators import *


class EstimatePage(BasePage):

    url = 'https://www.netguru.co/estimate-project'
    email = 'pawel.rzewuski@op.pl'
    first_name = 'Pawel'
    last_name = 'Rzewuski'
    phone_num = '793176770'
    description = 'This is a selenium test'

    @property
    def email_input_field(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.EMAIL_INPUT_FIELD[0],
            value=EstimatePageLocators.EMAIL_INPUT_FIELD[1])

    @property
    def device_desktop_check(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.DEVICE_DESKTOP_BUTTON[0],
            value=EstimatePageLocators.DEVICE_DESKTOP_BUTTON[1])

    @property
    def device_frontend_check(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.DEVICE_FRONTEND_BUTTON[0],
            value=EstimatePageLocators.DEVICE_FRONTEND_BUTTON[1])

    @property
    def email_input(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.EMAIL_INPUT_FIELD[0],
            value=EstimatePageLocators.EMAIL_INPUT_FIELD[1])

    @property
    def first_name_input(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.FIRSTNAME_INPUT_FIELD[0],
            value=EstimatePageLocators.FIRSTNAME_INPUT_FIELD[1])

    @property
    def last_name_input(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.LASTNAME_INPUT_FIELD[0],
            value=EstimatePageLocators.LASTNAME_INPUT_FIELD[1])

    @property
    def phone_input(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.PHONE_INPUT_FIELD[0],
            value=EstimatePageLocators.PHONE_INPUT_FIELD[1])

    @property
    def description_input(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.DESCRIPTION_INPUT_FIELD[0],
            value=EstimatePageLocators.DESCRIPTION_INPUT_FIELD[1])
