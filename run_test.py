from selenium import webdriver
from main_page import MainPage
from estimate_page import EstimatePage
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
netguru_page.got_to()

# S3: Accepting agreement and cookies message
netguru_page.close_agreement_message.click_element()
time.sleep(1)
netguru_page.close_cookies_message.click_element()
time.sleep(1)

# S4: Loop through slide right element
for i in range(4):
    time.sleep(1)
    netguru_page.right_slide_bar.click_element()

# S5: Go to Estimate project section
netguru_page.nav_bar_toggle.click_element()
netguru_page.go_to_estimate.click_element()

# S6: Estimate page
estimate_page = EstimatePage(driver=browser)
estimate_page.got_to()
estimate_page.device_desktop_check.click_element()
time.sleep(1)
browser.execute_script("window.scrollTo(0, 650);")
time.sleep(1)
estimate_page.device_frontend_check.click_element()
browser.execute_script("window.scrollTo(0, 900);")
time.sleep(1)
browser.execute_script("window.scrollTo(0, 1200);")
time.sleep(1)

# S7: Fill in the form
estimate_page.email_input.input_text('pawel.rzewuski@op.pl')
estimate_page.first_name_input.input_text('Pawel')
estimate_page.last_name_input.input_text('Rzewuski')
estimate_page.phone_input.input_text('793176770')
estimate_page.description_input.input_text('This is a selenium automated test')


# S7 invoke JavaScript alert with test message and close browser
browser.execute_script("return alert('Test Successful!');")
time.sleep(3 )
browser.close()
