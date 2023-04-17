from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[contains(text(),'I want')]")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    x = str(calc(int(x.text)))

    result = browser.find_element(By.ID, "answer")
    result.send_keys(x)

    button = browser.find_element(By.XPATH, "//button[contains(text(),'Su)]")
    button.click()

finally:

    time.sleep(30)

    browser.quit()
