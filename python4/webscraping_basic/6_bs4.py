#pip install beautifulsoup4
#pip install lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
#안된다...
#print(soup.find)
#print(soup.find("a", attrs={"class":"GlobalNavigationBar__button_creators--ssg_1"}))
#print(soup.find("li", attrs={"class":"AsideList__item--i30ly"}))
#rank1 = soup.find("li", attrs={"class":"AsideList__item--i30ly"})
#print(rank1.a)
#rank2 = rank1.next_sibling.next_sibling
#rank3 = rank2.next_sibling.next_sibling
#next_sibling.next_sibling("li")
#rank2 = rank1.find_next_sibling("li")
# previous_sibling
# rank1.find_next_siblings("li")

webtoon = soup.find("a", text="텍스트")
print(webtoon)