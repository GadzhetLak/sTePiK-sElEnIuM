from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value")
    x = str(calc(int(x.text)))

    result = browser.find_element(By.ID, "answer")
    result.send_keys(x)

    browser.execute_script("window.scrollBy(0, 100);")

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobtn.click()

    button = browser.find_element(By.XPATH, "//button[contains(text(),'Su')]")
    button.click()
finally:

    time.sleep(30)
    browser.quit()