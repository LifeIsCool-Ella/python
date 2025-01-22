from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

browser.switch_to.frame('iframeResult')

#elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[2]')
#elem = browser.find_element(By.ID, 'vehicle1')
#elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Audi"]')
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text()="Au")]')
elem.click()

time.sleep(5)

browser.quit()