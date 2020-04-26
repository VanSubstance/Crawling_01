from selenium import webdriver
from datetime import datetime
import time
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("disable-gpu") # 가속 사용 x
options.add_argument("lang=ko_KR") # 한국어
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/81.0.4044.113")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)   #3초대기


driver.get("https://map.naver.com/v5/subway/1000/-/-/-?c=14332751.7939536,4274399.2466463,15,0,0,0,dh")
driver.implicitly_wait(5)
driver.find_element_by_css_selector("#intro_popup_close > span").click()
boxes = driver.find_elements_by_css_selector("#container > subway-content > div > div.__subway-engine-transform > div.__subway-engine-layer.__subway-engine-baseLine > svg > g")

source = driver.page_source
bs = BeautifulSoup(source, 'html.parser')
entire = bs.select('#container > subway-content > div > div.__subway-engine-transform > div.__subway-engine-layer.__subway-engine-baseLine > svg > g')
# li_list = entire.find_all('g')
for li in li_list:
    try:
        sub_name = entire.select
        sub = box.text()
        print(li.text)

    except:
        pass

driver.close()