# 1: 문화유산 | 2: 레저, 테마 | 3: 기념, 전시, 미술관 | 4: 공원, 문화 명소 |

import os

transform = ['문화유산', '레저, 테마', '기념, 전시, 미술관', '공원, 문화 명소']

station = ['places']

dir_excel = (os.path.dirname(os.getcwd()) + "\\Place").replace("\\", "/")

for i in station:
    excel = dir_excel + '/excel/' + i + '.txt'
    data = open(excel, "r", encoding='utf-8')

    
    
    "sql 파일 만들기"
    sql = dir_excel + '/sql/' + i + ".sql"
    T = open(sql, "w+t")
    
    ""
    case = []
    for i in data:
        case.append("update places set ctgrgroup = \'" + transform[int(i[0:1]) - 1] + "\'")
        case.append(" where ctgr = \'" + i[2: -1] + "\';\n")
    for i in case:
        T.write(i)
    T.close()