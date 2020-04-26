from selenium import webdriver
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu") # 가속 사용 x
options.add_argument("lang=ko_KR") # 한국어
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/81.0.4044.113")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)   #3초대기
results = []
total = []
total_num = 0
driver.get("https://data.soledot.com/subwaystation/fo/subwaystationtimelist.sd")
driver.implicitly_wait(5)
boxes = driver.find_elements_by_xpath('//*[@id="frm"]/div/div/div[2]/div[2]')
for box in boxes:
    try:
        # line = box.find_element_by_css_selector("div").text
        sb_name = box.find_elements_by_css_selector("div")
        # print(line)
        for i in sb_name:
            name = i.text
            results.append(name)
    except:
        pass
for i in range(0, len(results), 3):
    total.append(results[i])
    print(results[i])
    total.append(results[i+2].split(" "))
    print(len(results[i+2]), results[i+2])
for i in range(1, len(total), 2):
    print(total[i-1])
    print(len(total[i]))
    total_num = total_num + len(total[i])
    print(total[i])
print(total_num)
print(total) # [n호선, [역....]]
only_sb=[] # 지하철역 총 집합
for i in range(1, len(total), 2):
    only_sb.extend(total[i])
print(only_sb)
driver.close()