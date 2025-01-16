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

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://learn.dict.naver.com/conversation#/endic/20250116"
    soup = create_soup(url)
    news_list = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
  
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())  
        
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())  
    print()
    
if __name__ == "__main__" : 
    scrape_english() 
    
    