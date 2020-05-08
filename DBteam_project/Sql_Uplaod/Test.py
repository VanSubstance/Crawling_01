import pandas as pd

data = pd.read_csv('E:/Studying/DB/Crawling_01/DBteam_project/Test_GunDae.csv', encoding='cp949')

"SQL에 업로드할 정보가 담긴 존나 큰 튜플덩어리"
case = []

"sql 파일 만들기"
T = open("Sample1.sql", "w")

"테이블 생성 코드 입력"
T.write("SET DEFINE OFF;\n")
T.write("drop table SampleTable;\n")
T.write("create table SampleTable (\"NUM\" integer, \"ST_NAME\" varchar(60), \"REV_NUM\" varchar(60), \"CTGR\" varchar(60), \"URL\" varchar(400));\n")

"data의 행 수만큼 반복"
"case에 sql 언어로 작성해서 sql 파일에 기제"
for i in range(data.shape[0]):
    line = data.iloc[i]
    case.append("insert into SampleTable (NUM, ST_NAME, REV_NUM, CTGR, URL) values (")
    case.append(str(line[0]))
    case.append(", \'%s\'" % line[1])
    case.append(", \'%s\'" % line[2])
    case.append(", \'%s\'" % line[3])
    case.append(", \'%s\'" % line[4])
    case.append(");\n")
    
for i in case:
    T.write(i)


    