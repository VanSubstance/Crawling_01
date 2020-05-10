import pandas as pd

StationList = pd.read_csv('E:/Studying/DB/Crawling_01/DBteam_project/Station/Stations.csv', encoding = 'UTF-8')
station = StationList.values[:, 0]

for i in station:
    excel = 'E:/Studying/DB/Crawling_01/DBteam_project/Place/excel/' + i + '.csv'
    data = pd.read_csv(excel, encoding='UTF-8')

    "SQL에 업로드할 정보가 담긴 존나 큰 튜플덩어리"
    case = []
    
    "sql 파일 만들기"
    sql = "E:/Studying/DB/Crawling_01/DBteam_project/Place/sql/" + i + ".sql"
    T = open(sql, "w+t")
    
    T.write("SET DEFINE OFF;\n")

    "data의 행 수만큼 반복"
    "case에 sql 언어로 작성해서 sql 파일에 기제"
    for i in range(data.shape[0]):
        line = data.iloc[i]
        case.append("insert into PLACES (STATION_NAME, PLACE_NAME, REV_NUM, CTGR, URL) values (")
        case.append("\'%s\'" % line[0])
        case.append(", \'%s\'" % line[1])
        case.append(", \'%s\'" % line[2])
        case.append(", \'%s\'" % line[3])
        case.append(", \'%s\'" % line[4])
        case.append(");\n")
        
        for i in case:
            T.write(i)
            
    T.close()

    