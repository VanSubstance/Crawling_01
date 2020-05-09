from selenium import webdriver
import time
import urllib.request
keyword="건대입구역"
driver=webdriver.Chrome('C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe')
i=1
result=[]
while i<3: # 긁어올 페이지 범위    
    driver.get('https://store.naver.com/restaurants/list?filterId=s13479290&page={}&query={}%20%EB%A7%9B%EC%A7%91&sessionid=LmKnpyNLmoaBUYwZvkGFKg%3D%3D&sortingOrder=reviewCount'.format(i,keyword))
    boxes = driver.find_elements_by_tag_name('img')
    results=[]
    for box in boxes:
        if 'autoRotate' in box.get_attribute('src'):
            results.append(box.get_attribute('src'))
    result+=results
    i+=1

driver.close()
print("수집완료")
#폴더생성
import os
if not os.path.isdir('./{}'.format(keyword)):
       os.mkdir('./{}'.format(keyword))

#다운로드
from urllib.request import urlretrieve
for index, link in enumerate(result):
    start=link.rfind(".")
    end=link.rfind('&')
    # print(results[0][start:end])
    filetype=link[start:end]
    urlretrieve(link,'./{}/{}{}{}'.format(keyword,keyword,index,filetype))