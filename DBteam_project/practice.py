from selenium import webdriver
from datetime import datetime
import time
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu") # 가속 사용 x
options.add_argument("lang=ko_KR") # 한국어
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/81.0.4044.113")
driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(3)   #3초대기

li = {}

li1 = [] #음식점 이름 key
li2 = [] #리뷰수 value
list_sub = ["강남역"] # 여기에 검색할 지하철역
start = time.time()
for name in list_sub: # "지하철역"
    print("----------------------------------------------------------\n",name)
    for i in range(1, 3): # 긁어올 페이지 범위
        print("------------------------------\n", i,"페이지")
        link_list = []
        list_result = []
        while len(list_result)==0:
            driver.get("https://store.naver.com/restaurants/list?filterId=s11636653&page={}&query={}%20%EB%A7%9B%EC%A7%91&sessionid=M3bL4uhv%2BXwthE2rZIklQg%3D%3D&sortingOrder=reviewCount".format(i, name))
            driver.implicitly_wait(5)
            boxes = driver.find_elements_by_css_selector("#container > div.placemap_area > div.list_wrapper > div > div.list_area > ul > li")
            for box in boxes:
                st_name = box.find_element_by_css_selector("span > a").text  # 음식점 이름
                review = box.find_element_by_css_selector("div > div.etc_area.ellp > span").text  # 리뷰수
                enter_page = box.find_element_by_css_selector("span > a")
                link = enter_page.get_attribute('href')
                link_list.append(link)
                # print([st_name[2:], review[3:]])
                list_result.append([st_name[2:], review[3:]])
                # print(st_name, review)
            for i in range(len(link_list)): # 음식점 분류
                driver.get(link_list[i])
                driver.implicitly_wait(5)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                menu = soup.find('span', {'class': 'category'}).text
                list_result[i].append(menu)
                print(list_result[i])     
        print(list_result)
    li[name]=list_result
currentTime=datetime.now()
print(time.time()-start)
for i in li:
    print("{} ({}): ".format(i,len(li[i])), li[i])
driver.close()
#_business_13226811 > div > div > div.tit > span > a > span
#_business_35603926 > div > div > div.tit > span > a > span
#_business_13226811 > div > div > div.etc_area.ellp > span
#_business_21607745 > div > div > div.etc_area.ellp > span:nth-child(1)
