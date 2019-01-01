from base_page import BasePage
from base_element import *
from locators import *


class MainPage(BasePage):
    """Class with all elements located on the main page"""
    url = "https://www.netguru.co/"

    @property
    def close_agreement_message(self):
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.AGREEMENT_BUTTON[0],
            value=MainPageLocators.AGREEMENT_BUTTON[1]
        )

    @property
    def close_cookies_message(self):
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.CLOSE_COOKIES_BUTTON[0],
            value=MainPageLocators.CLOSE_COOKIES_BUTTON[1]
        )

    @property
    def right_slide_bar(self):
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.RIGHT_SLIDE_BAR_BUTTON[0],
            value=MainPageLocators.RIGHT_SLIDE_BAR_BUTTON[1]
        )
    @property
    def nav_bar_toggle(self):
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.NAV_BAR_TOGGLE_BUTTON[0],
            value=MainPageLocators.NAV_BAR_TOGGLE_BUTTON[1]
        )

    @property
    def go_to_estimate(self):
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.ESTIMATE_PROJECT_NAV_BUTTON[0],
            value=MainPageLocators.ESTIMATE_PROJECT_NAV_BUTTON[1]
        )


