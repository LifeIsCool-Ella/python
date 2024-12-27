#pip install beautifulsoup4
#pip install lxml

import requests
from bs4 import BeautifulSoup

#url = "https://comic.naver.com/webtoon"
url= "https://wikidocs.net/book/14314"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())

print(soup.a)
print(soup.a.attrs)
#print(soup.a["span"])

print(soup.find("a", attrs={"class","list-group-item"}))
print(soup.find(attrs={"class","list-group-item"}))

rank1 = soup.find("a", attrs={"class","list-group-item"})
print(rank1.span)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank2.span.get_text())
print(rank3.span.get_text())

#안된다...
#print(soup.find)
#print(soup.find("a", attrs={"class":"GlobalNavigationBar__button_creators--ssg_1"}))
#print(soup.find("li", attrs={"class":"AsideList__item--i30ly"}))
#rank1 = soup.find("li", attrs={"class":"AsideList__item--i30ly"})
#rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a)
#rank2 = rank1.next_sibling.next_sibling
#rank3 = rank2.next_sibling.next_sibling
#print(rank3.a.get_text())
#next_sibling.next_sibling("li")
#rank2 = rank3.previous_sibling.previous_sibling
#print(rank2.a.get_text())
#print(rank1.parent)
#rank2 = rank1.find_next_sibling("li")

#print(rank2.a.get_text())
#rank3 = rank2.find_next_sibling("li")
#print(rank3.a.get_text())
#rank2 = rank3.find_previous_sibling("li")
#rank1.find_next_siblings("li")

#rank4=rank3.find_next_siblings("a")
#print(rank4.span.get_text())

stringtitle = soup.find("a", string="04. OpenAI API 사용(GPT-4o 멀티모달)")

print(stringtitle)

