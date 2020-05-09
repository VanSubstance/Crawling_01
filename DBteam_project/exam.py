from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException








options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(3)

with open('file.json','r', encoding='utf-8-sig') as f:
    data = json.load(f)
    data2 = data['hits']

dict_store = {}

naver_url = "https://map.naver.com/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
driver.get(naver_url)
idx = 750

for i in range(751,len(data2['hits'])):
    idx += 1
    print('idx =',idx)
    print(i, "=============>>", data2['hits'][i]['_source']['상호명'])
    dict_store_one = {}
    
    query = data2['hits'][i]['_source']['상호명']+" " + data2['hits'][i]['_source']['도로명주소'].split(' ')[2]
    
    store_name =  data2['hits'][i]['_source']['상호명']
    if '단란주점' in store_name:
        continue
    
    driver.find_element_by_xpath('//*[@id="search-input"]').clear()
    driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(query)
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button').click()
    
    try:
        
        click = driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl")
        
        driver.implicitly_wait(10)
        if store_name in click.text:
            click.click()
        else:
            print("--해당음식점이 없습니다")
            continue
            
        try:
            driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/ul/li[4]/a").click()
        except ElementNotVisibleException:
            driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl").click()
            driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/ul/li[4]/a").click()
        
    
    except NoSuchElementException or WebDriverException:
        print('--검색결과가 없습니다')
        
        query2 = data2['hits'][i]['_source']['상호명']+" " + data2['hits'][i]['_source']['도로명주소'].split(' ')[1]

        driver.find_element_by_xpath('//*[@id="search-input"]').clear()
        driver.find_element_by_xpath('//*[@id="search-input"]').send_keys(query2)
        driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button').click()

        try:
            click = driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl")
            if store_name in click.text:
                click.click()
            else:
                print("--해당음식점이 없습니다")
                continue
        
            try:
                driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/ul/li[4]/a").click()
            except ElementNotVisibleException:
                driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[1]/dl").click()
                driver.find_element_by_xpath("//*[@id='panel']/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/ul/li[4]/a").click()

        except NoSuchElementException:
            print('--검색결과가 없습니다')
            continue
        
    driver.switch_to.window(driver.window_handles[-1])
    url = driver.current_url
    ter = url.index("=")
    place_a_id = (url[ter:])[1:]
    
    if "#" in place_a_id:
        place_a_id = place_a_id.split('#')[0]
        
    params = {
    "id":place_a_id
    }
        
    print(place_a_id)
    
    naver_place_url = "https://store.naver.com/restaurants/detail?"
    response_url = requests.get(naver_place_url,params=params).url
    
    try:
        page = urlopen(response_url)
    except HTTPError:
        print('HTTPError')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        continue
        
    soup = BeautifulSoup(page,"html.parser")
    
    place_info = soup.select_one("#content > div:nth-of-type(2) > div.bizinfo_area > div")
    place_info_attrs = place_info.find_all("div", attrs={"class":"list_item"})
    
    dict_store_one['상호명'] = data2['hits'][i]['_source']['상호명']
    
    for i in range(len(place_info_attrs)):
        key = place_info_attrs[i].span['aria-label']
        value = place_info_attrs[i].text
        dict_store_one[key] = value
    
    info = soup.select_one('#content > div:nth-child(1) > div.biz_name_area > div > div').text
    
    if not '블로그 리뷰' in info:
        print('--블로그 리뷰 : 0')
        dict_store_one['__블로그리뷰__']=[]
        
    elif '블로그 리뷰' in info:
        headers2={
            "Referer":"https://store.naver.com/restaurants/detail?",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

        params2 = {
            "exclude":"",
            "businessId":place_a_id,
            "category":"restaurant",
            "start": 1,
            "display": 50
        }

        naver_blog_url = "https://store.naver.com/sogum/api/fsasReviews"
        res = requests.get(naver_blog_url,headers=headers2, params=params2)
        blog_dict = json.loads(res.text)
        print('--블로그 리뷰 : ',len(blog_dict['items']))
        
        all_blog_text = []
        for i in range(len(blog_dict['items'])):
            url = blog_dict['items'][i]['url']
            page = urlopen(url)
            soup_1 = BeautifulSoup(page,"html.parser")
            blog_text = []
            
            if len(soup_1.find_all(attrs={"class":"se_textarea"})) != 0:
                for t in soup_1.find_all(attrs={"class":"se_textarea"}):
                    txt = t.get_text()
                    if len(txt) == 0:
                        continue
                    blog_text.append(txt)
            elif len(soup_1.find_all(attrs={"class":"se-module se-module-text"})) != 0:
                for t in soup_1.find_all(attrs={"class":"se-module se-module-text"}):
                    txt = t.get_text()
                    if len(txt) == 0:
                        continue
                    blog_text.append(txt)
            elif len(soup_1.find_all(attrs={"align":"center"})) != 0:  
                for t in soup_1.find_all(attrs={"align":"center"}):
                    txt = t.get_text()
                    if len(txt) == 0:
                        continue
                    blog_text.append(txt)
            elif len(soup_1.find_all(attrs={"class":"post_ct"})) != 0:          
                for t in soup_1.find_all(attrs={"class":"post_ct"}):
                    txt = t.get_text()
                    if len(txt) == 0:
                        continue
                    blog_text.append(txt)    
            else:
                print('새로운 형식의 블로그')
                print(url)
                
            all_blog_text.append(blog_text)
            
        dict_store_one['__블로그리뷰__'] = all_blog_text
                    
    if not '예약자 리뷰 ' in info:
        print('--예약자 리뷰 : 0')
        dict_store_one['__예약자리뷰__'] = []
        
    elif '예약자 리뷰 ' in info:
        booking_review = []
        soup_2= soup.select_one('#content > div:nth-child(1) > div.func_btn_area > ul > li:nth-child(1) > a')
        bookingBusinessId = soup_2['href'].split('/')[-1].split('?')[0]

        for i in range(10):
            headers3 = {
                       "Referer": "https://store.naver.com/restaurants/detail",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
                    } 
            params3 = {
                      "bookingBusinessId":bookingBusinessId,
                      "page" : i,
                      "display" : 10,
                      "businessType": "restaurant"
                     }

            reviewurl = "https://store.naver.com/sogum/api/bookingReviews"

            res2 = requests.get(reviewurl, headers=headers3, params = params3)
            txt_dict = json.loads(res2.text)

            if len(txt_dict['items']) == 0:break

            for txt in range(len(txt_dict['items'])):
                review = txt_dict['items'][txt]['reviewBody']
                booking_review.append(review)
            
        print('--예약자 리뷰 : ',len(booking_review))
        dict_store_one['__예약자리뷰__'] = booking_review
            
    dict_store[query] = dict_store_one
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print()
    
    if idx % 10 == 0:
        with open('./jsonsave/text.json', 'a', encoding='UTF-8-sig') as file:
            file.write(json.dumps(dict_store, ensure_ascii=False))
            dict_store = {}
            print('****************저장완료****************') 
        
driver.close()