from base_element import *
from locators import *


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.netguru.co/"

    def got_to_webpage(self):
        self.driver.get(self.url)
        print('== go to webpage ==')

    @property
    def close_agreement_message(self):
        print('== accept agreement ==')
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.AGREEMENT_BUTTON[0],
            value=MainPageLocators.AGREEMENT_BUTTON[1]
        )

    @property
    def close_cookies_message(self):
        print('== accept agreement ==')
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.CLOSE_COOKIES_BUTTON[0],
            value=MainPageLocators.CLOSE_COOKIES_BUTTON[1]
        )

    @property
    def right_slide_bar(self):
        print('== right slide bar ==')
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.RIGHT_SLIDE_BAR_BUTTON[0],
            value=MainPageLocators.RIGHT_SLIDE_BAR_BUTTON[1]
        )
    @property
    def nav_bar_toggle(self):
        print('== nav_bar_toggle ==')
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.NAV_BAR_TOGGLE_BUTTON[0],
            value=MainPageLocators.NAV_BAR_TOGGLE_BUTTON[1]
        )

    @property
    def go_to_careers(self):
        print('== go_to_career ==')
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.CAREERS_PAGE_NAV_BUTTON[0],
            value=MainPageLocators.CAREERS_PAGE_NAV_BUTTON[1]
        )

    @property
    def go_to_estimate(self):
        print('== go_to_estimate ==')
        return BaseElement(
            driver=self.driver,
            by=MainPageLocators.ESTIMATE_PROJECT_NAV_BUTTON[0],
            value=MainPageLocators.ESTIMATE_PROJECT_NAV_BUTTON[1]
        )


