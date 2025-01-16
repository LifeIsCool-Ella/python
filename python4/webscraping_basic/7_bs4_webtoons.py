import requests
from bs4 import BeautifulSoup

url= "https://wikidocs.net/book/14314"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a", attrs={"class":"list-group-item"})
for cartoon in cartoons:
    print(cartoon.get_text())
