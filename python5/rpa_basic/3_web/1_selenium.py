from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import time

#browser = webdriver.Chrome("./chromedriver_131.exe")
browser = webdriver.Chrome()
url = "http://naver.com"
browser.get(url)
time.sleep(2)
elem = browser.find_element(By.LINK_TEXT, "카페")
elem.click()
time.sleep(2)
#elem.get_attribute("href")
#elem.get_attribute("class")

browser.back()
#browser.forward()
#browser.refresh()
#browser.back()

time.sleep(2)

url = "https://naver.com"
browser.get(url)
elem2 = browser.find_element(By.TAG_NAME, "a")
elem2.get_attribute("href")

time.sleep(2)

elem3 = browser.find_element(By.NAME, "query")
elem3.click()
elem3.send_keys("파이썬")
elem3.send_keys(Keys.ENTER)
time.sleep(2)


url = "https://www.daum.net"
browser.get(url)
time.sleep(2)

elem4 = browser.find_element(By.XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[3]")
elem4.click()

time.sleep(2)