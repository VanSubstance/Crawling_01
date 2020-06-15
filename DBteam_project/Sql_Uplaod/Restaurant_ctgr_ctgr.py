# 1: 양식 | 2: 일식 | 3: 한식 | 4: 카페, 디저트 | 5: 주점 | 6: 분식, 패스트푸드 | 7. 중식, 동양식

import os

transform = ['양식', '일식', '한식', '카페, 디저트', '주점', '분식, 패스트푸드', '중식, 동양식']

station = ['restaurants']

dir_excel = (os.path.dirname(os.getcwd()) + "\\Restaurant").replace("\\", "/")

for i in station:
    excel = dir_excel + '/excel/' + i + '.txt'
    data = open(excel, "r", encoding='utf-8')

    
    
    "sql 파일 만들기"
    sql = dir_excel + '/sql/' + i + ".sql"
    T = open(sql, "w+t")
    
    ""
    case = []
    for i in data:
        case.append("update restaurants set ctgrgroup = \'" + transform[int(i[0:1]) - 1] + "\'")
        case.append(" where ctgr = \'" + i[2: -1] + "\';\n")
    for i in case:
        T.write(i)
    T.close()