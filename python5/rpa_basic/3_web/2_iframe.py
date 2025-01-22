from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

elem.click()

browser.switch_to.default_content()

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

time.sleep(5)

browser.quit()
