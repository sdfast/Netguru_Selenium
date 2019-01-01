from selenium import webdriver
from main_page import MainPage
from estimate_page import EstimatePage
import time

"""Test Setup"""
# Setting variable for automated browser driver with it's path given as raw string
# Webdriver can also be accessed if added to system PATH, then we don't need to use webdriver file path
browser = webdriver.Chrome(r"E:\Projekty\Netguru\chromedriver.exe")

"""Test Steps"""
# S1: Initializing main page driver and opening main page in the browser
netguru_page = MainPage(driver=browser)
netguru_page.got_to()

# S2: Accepting agreement and cookies message
netguru_page.close_agreement_message.click_element()
netguru_page.close_cookies_message.click_element()

# S3: Looping through slide right element
for i in range(4):
    time.sleep(0.5)
    netguru_page.right_slide_bar.click_element()

# S4: Go to Estimate project section
netguru_page.nav_bar_toggle.click_element()
netguru_page.go_to_estimate.click_element()

# S5: Initializing estimate page driver to use EstimatePage objects
estimate_page = EstimatePage(driver=browser)
estimate_page.got_to()

# S6: Setting estimate project device and scope and scrolling down the page
estimate_page.device_desktop_check.click_element()
time.sleep(1)
browser.execute_script("window.scrollTo(0, 650);")
estimate_page.device_frontend_check.click_element()
time.sleep(1)
browser.execute_script("window.scrollTo(0, 1000);")

# S7: Filling in the estimate form
estimate_page.email_input_field.input_text('pawel.rzewuski@op.pl')
estimate_page.first_name_input_field.input_text('Pawel')
estimate_page.last_name_input_field.input_text('Rzewuski')
estimate_page.phone_input_field.input_text('793176770')
estimate_page.description_input_field.input_text('This is an automated selenium test')
# (Submitting the form is intentionally skipped in order not to spam the system with test forms)

# S8 Triggering JavaScript alert with test message, closing the browser
browser.execute_script("return alert('Test Successful!');")
time.sleep(2)
browser.close()
