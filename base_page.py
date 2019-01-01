

class BasePage(object):
    url = None

    def __init__(self, driver):
        print('== init - base page ==')
        self.driver = driver

    def got_to(self):
        self.driver.get(self.url)
        print('== go to webpage ==')
