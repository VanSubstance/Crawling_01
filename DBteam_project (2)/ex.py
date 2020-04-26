from selenium import webdriver
from datetime import datetime
import time
import pandas as pd
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu") # 가속 사용 x
options.add_argument("lang=ko_KR") # 한국어
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/81.0.4044.113")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(1)   #3초대기
driver.maximize_window()



results = []
error = 0
li1 = [] #음식점 이름 key
li2 = [] #리뷰수 value
list_sub = ["신촌역"] # 여기에 검색할 지하철역
start = time.time()
for name in list_sub: # "지하철역"
    print("----------------------------------------------------------\n",name)
    link_list = []
    driver.get("https://map.naver.com/v5/search/{}%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3?c=14134216.9318967,4519047.8811907,15,0,0,0,dh".format(name))
    driver.implicitly_wait(5)
    click = driver.find_element_by_css_selector('#intro_popup_close').click()
    click1 = driver.find_element_by_css_selector('#container > div.router-output > shrinkable-layout > search-layout > search-list > search-list-tabs > div > div > div.btn_box.ng-star-inserted > nm-select-box > div > button').click()
    click2 = driver.find_element_by_css_selector('#container > div.router-output > shrinkable-layout > search-layout > search-list > search-list-tabs > div > div > div.btn_box.ng-star-inserted > nm-select-box > div > ul > li:nth-child(2) > a').click()
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    boxes = soup.find_all('search-item-place')
    for box in boxes:
        name = box.find('span', {'class': 'search_title_text'}).string
        category = box.find('span', {'class': 'search_text category limit_100 ng-star-inserted'}).string
        review = box.find('span', {'class': 'count'}).string
        results.append([name,category,review])
    print(results)






    # boxes = driver.find_elements_by_css_selector("#container > div.router-output > shrinkable-layout > search-layout > search-list > search-list-contents > perfect-scrollbar > div > div.ps-content > div > div > div > search-item-place:nth-child(5)")
    # print(boxes)
    # for box in boxes:
    #     list_result = []
    #     st_name = box.find_element_by_css_selector("strong > span").text  # 장소 이름
    #     print(st_name)
    #     cate = box.find_element_by_class_name('search_text_box') #장소 분류
    #     category = cate.find_element_by_css_selector('span').text
    #     print(category)
    #     review = box.find_element_by_class_name("count").text  # 리뷰수
    #     print(review[:3])
    #     list_result.append([st_name,category,review[:3]])
    #     print(list_result)
    #     print('------------')
    #     time.sleep(1)
#     data = pd.DataFrame(results)
#     data.columns = ['name', "review", "category", "link"]
#     data.to_csv("{}.csv".format(name), encoding='cp949')
# currentTime=datetime.now()
# print("걸린시간 : ", time.time()-start)
# print("에러 수 : ", error)
# driver.close()
# print(results)

