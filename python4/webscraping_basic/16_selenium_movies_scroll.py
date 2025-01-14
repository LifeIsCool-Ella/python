from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

url ="https://play.google.com/store/movies?hl=ko&gl=KR"
browser.get(url)

#browser.execute_script("window.scrollTo(0, 1080)")
#browser.execute_script("window.scrollTo(0, 2080)")

#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


import time 
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
    
    
    