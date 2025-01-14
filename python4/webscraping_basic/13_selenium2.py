# pip install selenium
#chrome://version
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
time.sleep(3)

'''<input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">'''

#elem = browser.find_element_by_class_name("link_login")
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()

browser.find_element(By.ID,"id").send_keys("id")
browser.find_element(By.ID,"pw").send_keys("password")

time.sleep(1)
browser.find_element(By.ID, "log.login").click()
time.sleep(1)
browser.find_element(By.ID,"id").clear()
browser.find_element(By.ID,"id").send_keys("my_id")
time.sleep(1)
print(browser.page_source)

time.sleep(5)
#browser.close()
browser.quit() 
