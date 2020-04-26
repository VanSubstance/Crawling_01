from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("disable-gpu") # 가속 사용 x
options.add_argument("lang=ko_KR") # 한국어
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/81.0.4044.113")
driver = webdriver.Chrome(options=options)


li = {}
list_result = []
li1 = [] #음식점 이름 key
li2 = [] #리뷰수 value
# time.sleep(5)
driver.get("https://store.naver.com/restaurants/list?filterId=s11636653&page=1&query=신촌역%20%EB%A7%9B%EC%A7%91&sessionid=M3bL4uhv%2BXwthE2rZIklQg%3D%3D&sortingOrder=reviewCount")
driver.implicitly_wait(3)
boxes = driver.find_elements_by_css_selector("#container > div.placemap_area > div.list_wrapper > div > div.list_area > ul > li")
for box in boxes:
    st_name = box.find_element_by_css_selector("span > a").text   #음식점 이름
    review = box.find_element_by_css_selector("div > div.etc_area.ellp > span").text #리뷰수
    enter_page = box.find_element_by_css_selector("span > a")
    link = enter_page.get_attribute('href')
    driver.get(link)
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    menu = soup.find('span',{'class':'category'}).text
    print([st_name[2:], menu, review[3:]])
    list_result.append([st_name[2:], menu, review[3:]])
    driver.back()

print(list_result)
driver.close()
