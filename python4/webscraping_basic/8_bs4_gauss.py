import requests
from bs4 import BeautifulSoup

url = "https://wikidocs.net/book/14314"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("div", attrs={"class":"list-group"})
#title=cartoons[0].a.get_text()
#print(title)
#print(cartoons)
#link = cartoons[0].a["href"]
#print(link)


for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = cartoon.a["href"]
    print(title, link)
    
cartoons = soup.find_all("span", attrs={"style":"padding-left:20px"})
    
for cartoon in cartoons:
    text = cartoon.get_text()
    print(text)    
    
    