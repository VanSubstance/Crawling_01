import pandas as pd
import os

station = ['Line_08_01', 'Line_08_02', 'Line_08_03']

dir_excel = (os.path.dirname(os.getcwd()) + "\\Activity").replace("\\", "/")

for i in station:
    excel = dir_excel + '/excel/' + i + '.csv'
    data = pd.read_csv(excel, encoding='UTF-8')

    
    
    "sql 파일 만들기"
    sql = dir_excel + '/sql/' + i + ".sql"
    T = open(sql, "w+t")
    
    #T.write("SET DEFINE OFF;\n")

    "data의 행 수만큼 반복"
    "case에 sql 언어로 작성해서 sql 파일에 기제"
    for i in range(data.shape[0]):
        "SQL에 업로드할 정보가 담긴 존나 큰 튜플덩어리"
        case = []
        line = data.iloc[i].copy()
        for j in range(len(line)):
            if type(line[j]) is str:   
                temp = list(line[j]) 
                for k in range(len(temp)):
                    if temp[k] == '&':
                        temp[k] = '\&'
                temp = ''.join(temp)
                line[j] = temp
                line[j] = line[j].replace("\'", "\\\'")
        line[1] = line[1].replace(" station", "")
        line[1] = line[1].replace(" Station", "")
        case.append("insert ignore into ACTIVITIES (STATION_NAME, ACTIVITY_NAME, REV_NUM, CTGR, URL) values (")
        case.append("\'%s\'" % line[1])
        case.append(", \'%s\'" % line[2])
        case.append(", \'%s\'" % line[3])
        case.append(", \'%s\'" % line[4])
        case.append(", \'%s\'" % line[5])
        case.append(");\n")
        
        for i in case:
            T.write(i)
            
    T.close()