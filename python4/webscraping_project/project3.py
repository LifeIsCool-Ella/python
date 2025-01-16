import requests 
from bs4 import BeautifulSoup


def create_soup(url) : 
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup 

def print_news(index, title, link):
    print("{}.{}".format(index+1, title))
    print("(링크 : {})".format(link))

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/section/105"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"sa_list"}).find_all("li", limit=3)
    
    for index, news in enumerate(news_list) : 
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 
            
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()
        
    

if __name__ == "__main__" : 
    scrape_it_news() 
    
    