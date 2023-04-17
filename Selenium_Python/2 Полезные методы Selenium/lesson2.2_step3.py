from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    x = int(x.text)

    e = browser.find_element(By.ID, "num2")
    e = int(e.text)

    y = x + e

    y = str(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    button = browser.find_element(By.XPATH, "//button[contains(text(),'Su')]")
    button.click()

finally:

    time.sleep(30)

    browser.quit()
