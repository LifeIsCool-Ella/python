from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

#from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome()
browser.maximize_window()

url ="https://flight.naver.com/"
browser.get(url)

#browser.find_element(By.LINK_TEXT, "가는 날 선택").click()

#browser.find_element(By.XPATH, f"div[text()='가는 날']/..").click()

#div[text()='가는 날']/.. or div[contains(text(),'가는 날')]

#browser.find_element(By.LINK_TEXT, "28")[1].click()
#browser.find_element(By.LINK_TEXT, "29")[1].click()

#url2 = "https://flight.naver.com/flights/international/ICN-CAN-20250211/CAN-ICN-20250215?adult=1&fareType=Y"
#browser.get(url2)

# Copy XPath
browser.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div/a[4]/div/button[1]").click()

try :
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id='__next']/div/div/main/article/div[2]/div/div[2]/div[8]/button[1]"))
    print(elem.text)
finally : 
    browser.quit() 
    
time.sleep(10)
