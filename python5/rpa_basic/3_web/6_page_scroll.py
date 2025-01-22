from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/ns/home')

elem = browser.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div[1]/form/div/div[1]/div/div[1]/input')
elem.send_keys('무선마우스')
time.sleep(2)
elem.send_keys(Keys.ENTER)

#browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div[1]/form/div/div/div/div/button[3]').click()
#browser.execute_script('window.scrollTo(0,1080)')
#browser.execute_script('window.scrollTo(0,2080)')
#browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

browser.execute_script('window.scrollTo(0,0)')

time.sleep(5)
browser.quit()