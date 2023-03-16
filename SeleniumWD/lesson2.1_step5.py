from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

with webdriver.Chrome() as browser:

    browser.get('https://suninjuly.github.io/math.html')
    x= browser.find_element('id', 'input_value').text

    browser.find_element(By.TAG_NAME, "input").send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.find_element('id','robotCheckbox').click()

    browser.find_element('id', 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()

    time.sleep(3000)