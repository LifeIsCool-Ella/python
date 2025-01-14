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

import requests
from bs4 import BeautifulSoup

url ="https://play.google.com/store/movies?hl=ko&gl=KR"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
         , "Accept-Language": "ko-KR,ko;q=0.8,en -US;q=0.5,en;q=0.3"
}

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})
print(len(movies))

with open("movie.html", "w",  encoding="utf8") as f:
    #f.write(res.text)
    f.write(soup.prettify())
    
for movie in movies : 
    try:
        #title = movie.find("div", attrs ={"class":["Epkrse"]}).get_text()    
        #print(title)
        
        original_price = movie.find("span", attrs={"class":"VfPpfd VixbEe"})
        if original_price :
            original_price = original_price.get_text()
        else :
            #print(title, "")
            continue
        #link = movie.find("a", attrs={"class": "Si6A0c ZD8Cqc"}).get_text() 
        text = movie.find("a", attrs={"class": "Si6A0c ZD8Cqc"}).get_text() 
        #print(text)
        link = movie.find("a", attrs={"class": "Si6A0c ZD8Cqc"})["href"] 
        #print(link)
        
        print(f"제목 : {text}")
        print(f"금액 : {original_price}" )
        print(f"링크 : {link}" )
        print("-"*120)
    finally:
        print('')
        
browser.quit()

    
    
    