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
    ESTIMATE_SUBMIT_BUTTON = (By.XPATH, '//*[@id="hsForm_36a16954-d5ff-4d10-94ce-e82e601422c2_1212"]/div[10]/div[2]/input')
    DEVICE_DESKTOP_BUTTON = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div')
    DEVICE_FRONTEND_BUTTON = (By.XPATH, '/html/body/div[1]/section/div/div[2]/div[2]/div')
    EMAIL_INPUT_FIELD = (By.NAME, 'email')
    FIRSTNAME_INPUT_FIELD = (By.NAME, 'firstname')
    LASTNAME_INPUT_FIELD = (By.NAME, 'lastname')
    PHONE_INPUT_FIELD = (By.NAME, 'phone')
    DESCRIPTION_INPUT_FIELD = (By.NAME, 'short_description_of_idea')
