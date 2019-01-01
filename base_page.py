

class BasePage(object):
    """Base page class that is initialized on every page object class."""
    url = None

    def __init__(self, driver):
        self.driver = driver

    def got_to(self):
        self.driver.get(self.url)

