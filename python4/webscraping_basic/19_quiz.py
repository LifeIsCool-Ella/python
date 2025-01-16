import requests
from bs4 import BeautifulSoup

#url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
url = "https://new.land.naver.com/complexes/111515?ms=37.4980129,127.107268,17&a=APT:ABYG:JGC:PRE&e=RETAIL"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())
    
data_rows = soup.find("table", attrs={"class":"info_table_wrap"}).find("tbody").find_all("tr")    
for index, row in enumerate(data_rows):
    columns = row.find_all("th")
    print("============= 매물 {} ================".format(index+1))
    
    print(columns[0].get_text())
    