from selenium.webdriver.support.ui import WebDriverWait

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.netguru.co/"

    def got_to_webpage(self):
        self.driver.get(self.url)

    def accpt_agreement(self):
        agreement = self.driver.find_element_by_id("hs-eu-confirmation-button")
        agreement.click()

    def click_slider_right(self):
        button = self.driver.find_element_by_xpath("//*[@id='hs_cos_wrapper_widget_1493373930279']/span/div/div[3]")
        button.click()

    def open_Elmo(self):
        button = self.driver.find_element_by_xpath("//*[@id='root']/div/div[2]/button")
        button.click()

    def write_to_Elmo(self):
        pass

    def close_Elmo(self):
        pass