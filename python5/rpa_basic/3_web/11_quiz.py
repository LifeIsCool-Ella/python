from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.w3schools.com/"
browser.get(url)

time.sleep(2)

# Learn Html
elem = browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

time.sleep(5)

# How To
elem = browser.find_element(By.XPATH, '//*[@id="subtopnav"]/a[8]').click()

time.sleep(5)

#Contact Form
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]').click()

time.sleep(5)


first_name = "A"
last_name ="DEL"
country = "Canada"
subject = "내용 입력"


elem = browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
time.sleep(2)
elem = browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
time.sleep(2)
elem = browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="{}"]'.format(country)).click()
time.sleep(2)
elem = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)
time.sleep(2)
elem = browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()
