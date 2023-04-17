from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("LAG")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("GG")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("G22323232ghjgjhghjG@gmail.com")

    en = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    en.send_keys("C:/Users/psk/Desktop/1/file.txt")

    button = browser.find_element(By.XPATH, "//button[contains(text(),'Su')]")
    button.click()

finally:

    time.sleep(300)

    browser.quit()
