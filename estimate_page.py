from base_element import *
from locators import *


class EstimatePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.netguru.co/estimate-project"

    @property
    def email_input_field(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=EstimatePageLocators.EMAIL_INPUT_FIELD[0],
            value=EstimatePageLocators.EMAIL_INPUT_FIELD[1]
        )