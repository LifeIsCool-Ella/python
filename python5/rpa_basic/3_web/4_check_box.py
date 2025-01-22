from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame('iframeResult')

#elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')
elem = browser.find_element(By.ID, 'vehicle1')

if elem.is_selected() == False:
    print("선택하기")
    elem.click()
else:
    print("선택안함")

time.sleep(5)

browser.quit()