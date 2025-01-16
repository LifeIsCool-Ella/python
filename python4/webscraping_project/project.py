import requests 
from bs4 import BeautifulSoup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    cast1 = soup.find("span", attrs={"class":"temperature down"}).get_text()
    cast2 = soup.find("span", attrs={"class":"blind"}).get_text()
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text() #.replace("도씨","")
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()
    
    morning_rain_rate = soup.find("span", attrs={"class":"weather_left rainfall"}).get_text()#.strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"weather_left rainfall"}).get_text()#.strip()
    
    dust = soup.find("li", attrs={"class":"item_today level2"})
    pm10 = dust.find_all("span")[0].get_text() 
    pm25 = dust.find_all("dd")[1].get_text()
    
    
    
    print(cast)
    print(" 현재 {} ").format(curr_temp)
    print(" 현재 {} (최저 {} / 최고 {})").format(curr_temp, min_temp, max_temp)
    print(" 오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print(" 미세먼지 {}".format(pm10))
    print(" 미세먼지 {}".format(pm25))

if __name__ == "__main__" : 
    scrape_weather() 
    
    