from selenium.webdriver.common.by import By


class MainPageLocators:
    """Class containing locators from the main page: /"""

    AGREEMENT_BUTTON = (By.ID, 'hs-eu-confirmation-button')
    CLOSE_COOKIES_BUTTON = (By.CLASS_NAME, 'cookie-msg__close')
    RIGHT_SLIDE_BAR_BUTTON = (By.CLASS_NAME, 'main-slider__arrow--right')
    NAV_BAR_TOGGLE_BUTTON = (By.CLASS_NAME, 'navbar-toggle')
    ESTIMATE_PROJECT_NAV_BUTTON = (By.XPATH, '//*[@id="main-nav"]/a')
    CAREERS_PAGE_NAV_BUTTON = (By.XPATH, '//*[@id="main-nav"]/ul/li[7]/a')

class EstimatePageLocators:
    """Class containing locators from the career page: /estimate-project"""
    EMAIL_INPUT_FIELD = (By.ID, 'email-36a16954-d5ff-4d10-94ce-e82e601422c2_6830')

class CareerPageLocators:
    """Class containing locators from the career page: /career"""

    ELMO_BUTTON_2 = (By.CSS_SELECTOR, '#root > div > div._2ngXYtlcHXA-EjBwuz_RKI > button > i')
