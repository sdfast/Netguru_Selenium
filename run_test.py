from selenium import webdriver
from main_page import MainPage
import time

"""Test Setup"""
# Setting variable for automated browser driver with it's path given as raw string
browser = webdriver.Chrome(r"E:\Projekty\Netguru\chromedriver.exe")
test_value_positive = "Test Successful!"
test_value_negative = "Test Failed!"

"""Test Steps"""
# S1: Initializing driver for browser
netguru_page = MainPage(driver=browser)

# S2: Opening target page
netguru_page.got_to_webpage()

# S3: Accepting agreement and cookies message
netguru_page.close_agreement_message.click_element()
netguru_page.close_cookies_message.click_element()

# S4: Loop through slide right element
for i in range(4):
    time.sleep(1)
    netguru_page.right_slide_bar.click_element()

# S5: Go to Estimate project section
netguru_page.nav_bar_toggle.click_element()
netguru_page.go_to_estimate.click_element()

# S5: Open > Close > Open chat with Elmo
time.sleep(1)
# netguru_page.open_elmo.click_element()
# for i in range(1):
#     time.sleep(1)


# S6: input message for Elmo

# invoke JavaScript alert with test message and close
browser.execute_script("return alert(test_value_positive);")
time.sleep(2)
browser.close()