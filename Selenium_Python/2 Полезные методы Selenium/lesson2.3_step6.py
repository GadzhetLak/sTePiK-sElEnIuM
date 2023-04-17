from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[contains(text(),'I want')]")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    printxt = browser.find_element(By.ID, "answer")
    printxt.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[contains(text(),'Su')]")
    button.click()
finally:
    time.sleep(30)
    browser.quit()