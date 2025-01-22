from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle)

time.sleep(5)

elem = browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles
for handle in handles:
    print(handle)
    browser.switch_to.window(handle)
    print(browser.title)
    print()
    
print("현재 핸들 닫기")
browser.close()

print("처음 핸들로 돌아가기")
browser.switch_to.window(curr_handle)
print(browser.title)

time.sleep(3)
browser.get('https://www.daum.net')

time.sleep(5)
#browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.quit()