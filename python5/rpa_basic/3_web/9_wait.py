from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://flight.naver.com/")

#time.sleep(10)
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(5)
#browser.find_element(By.LINK_TEXT,'31')[0].click()
elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.LINK_TEXT, '31'))[0]
#time.sleep(5)
browser.find_element(By.LINK_TEXT,'3')[1].click()
time.sleep(5)
browser.find_element(By.LINK_TEXT,'항공권 검색')

#try :
#    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]'))
#    print(elem.text)
#except:
#    print("실패했어요")


time.sleep(5)

browser.quit()