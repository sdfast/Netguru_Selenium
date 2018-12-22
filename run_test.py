from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import *

# setting variable for autmating browser
browser = webdriver.Chrome(r"E:\Projekty\Netguru\chromedriver.exe")

# paassing browser to driver
netguru_page = MainPage(driver=browser)
netguru_page.got_to_webpage()


browser.implicitly_wait(2)
netguru_page.click_slider_right()
netguru_page.open_Elmo()