# 1: PC방 | 2: 노래방 | 3: 테마카페 | 4: VR, 오락실 | 5: 구기종목, 야외 |

import os

transform = ['PC방', '노래방', '테마카페', 'VR, 오락실', '구기종목, 야외']

station = ['activities']

dir_excel = (os.path.dirname(os.getcwd()) + "\\Activity").replace("\\", "/")

for i in station:
    excel = dir_excel + '/excel/' + i + '.txt'
    data = open(excel, "r", encoding='utf-8')

    
    
    "sql 파일 만들기"
    sql = dir_excel + '/sql/' + i + ".sql"
    T = open(sql, "w+t")
    
    ""
    case = []
    for i in data:
        case.append("update activities set ctgrgroup = \'" + transform[int(i[0:1]) - 1] + "\'")
        case.append(" where ctgr = \'" + i[2: -1] + "\';\n")
    for i in case:
        T.write(i)
    T.close()