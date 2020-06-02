import pandas as pd

data = pd.read_csv('E:/Studying/DB/Crawling_01/DBteam_project/Station/Stations.csv', encoding='UTF-8')

"SQL에 업로드할 정보가 담긴 존나 큰 튜플덩어리"
case = []

"sql 파일 만들기"
T = open("E:/Studying/DB/Crawling_01/DBteam_project/Station/Stations.sql", "w+t")

#T.write("SET DEFINE OFF;\n")

"data의 행 수만큼 반복"
"case에 sql 언어로 작성해서 sql 파일에 기제"
for i in range(data.shape[0]):
    line = data.iloc[i]
    case.append("insert into STATIONS (STATION_NAME, RATE) values (")
    case.append("\'%s\'" % line[0])
    case.append(", \'%f\'" % line[1])
    case.append(");\n")
    
for i in case:
    T.write(i)
    
T.close()
