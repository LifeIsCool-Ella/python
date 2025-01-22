from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#browser = webdriver.Chrome("./chromedriver_131.exe")
browser = webdriver.Chrome()
url = "https://www.w3schools.com/html/default.asp"
browser.get(url)
browser.maximize_window()

time.sleep(2)

elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[70]')

#actions = ActionChains(browser)
#actions.move_to_element(elem).perform()

xy = elem.location_once_scrolled_into_view
print("type : ", type(xy))
print("value : ", xy)
elem.click()

time.sleep(5)
browser.quit()