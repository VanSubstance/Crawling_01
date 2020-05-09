"테이블들 선언"

"""
"1. 지하철역 테이블"
"""

"SQL 파일 생성"
T = open('Table_Station.sql', 'w')

"테이블 생성 코드 작성"
T.write("SET DEFINE OFF;\n")
T.write("DROP TABLE STATIONS;\n")
T.write("create table STATIONS (\"STATION_NAME\" varchar(60), \"RATE\" FLOAT(1));\n")
"STATION_NAME을 Primary Key로 사용"
T.write("CREATE UNIQUE INDEX \"STATION_NAME_PK\" ON \"STATIONS\" (\"STATION_NAME\");\n")
"Primary Key 조건 설정"
T.write("ALTER TABLE \"STATIONS\" ADD CONSTRAINT \"STATION_NAME_PK\" PRIMARY KEY (\"STATION_NAME\");\n")


"""
"2. 맛집 테이블"
"""
T = open('Table_Restaurant.sql', 'w')
T.write("SET DEFINE OFF;\n")
T.write("DROP TABLE RESTAURANTS;\n")
T.write("create table RESTAURANTS (\"STATION_NAME\" varchar(60), \"RESTAURANTS_NAME\" varchar(60), \"REV_NUM\" varchar(60), \"CTGR\" varchar(60), \"URL\" varchar(400));\n")
"RESTAURANTS_NAME을 Primary Key로 사용"
T.write("CREATE UNIQUE INDEX \"RESTAURANTS_NAME_PK\" ON \"RESTAURANTS\" (\"RESTAURANTS_NAME\");\n")
"Primary Key 조건 설정"
T.write("ALTER TABLE \"RESTAURANTS\" ADD CONSTRAINT \"RESTAURANTS_NAME_PK\" PRIMARY KEY (\"RESTAURANTS_NAME\");\n")
T.write("ALTER TABLE \"RESTAURANTS\" MODIFY (\"RESTAURANTS_NAME\" NOT NULL ENABLE);\n")
"Foreign Key로 연결"
T.write("ALTER TABLE \"RESTAURANTS\" ADD CONSTRAINT \"RESTAURANTS_FK\" FOREIGN KEY (\"STATION_NAME\") REFERENCES \"STATIONS\" (\"STATION_NAME\") ENABLE;\n")


"""
"3. 놀거리 테이블"
"""
T = open('Table_Activity.sql', 'w')
T.write("SET DEFINE OFF;\n")
T.write("DROP TABLE ACTIVITIES;\n")
T.write("create table ACTIVITIES (\"STATION_NAME\" varchar(60), \"STORE_NAME\" varchar(60), \"REV_NUM\" varchar(60), \"CTGR\" varchar(60), \"URL\" varchar(400));\n")
"RESTAURANTS_NAME을 Primary Key로 사용"
T.write("CREATE UNIQUE INDEX \"STORE_NAME_PK\" ON \"ACTIVITIES\" (\"STORE_NAME\");\n")
"Primary Key 조건 설정"
T.write("ALTER TABLE \"ACTIVITIES\" ADD CONSTRAINT \"STORE_NAME_PK\" PRIMARY KEY (\"STORE_NAME\");\n")
T.write("ALTER TABLE \"ACTIVITIES\" MODIFY (\"STORE_NAME\" NOT NULL ENABLE);\n")
"Foreign Key로 연결"
T.write("ALTER TABLE \"ACTIVITIES\" ADD CONSTRAINT \"ACTIVITIES_FK\" FOREIGN KEY (\"STATION_NAME\") REFERENCES \"STATIONS\" (\"STATION_NAME\") ENABLE;\n")


"""
"4. 명소 테이블"
"""
T = open('Table_Places.sql', 'w')
T.write("SET DEFINE OFF;\n")
T.write("DROP TABLE PLACES;\n")
T.write("create table PLACES (\"STATION_NAME\" varchar(60), \"PLACE_NAME\" varchar(60), \"REV_NUM\" varchar(60), \"CTGR\" varchar(60), \"URL\" varchar(400));\n")
"RESTAURANTS_NAME을 Primary Key로 사용"
T.write("CREATE UNIQUE INDEX \"PLACE_NAME_PK\" ON \"PLACES\" (\"PLACE_NAME\");\n")
"Primary Key 조건 설정"
T.write("ALTER TABLE \"PLACES\" ADD CONSTRAINT \"PLACE_NAME_PK\" PRIMARY KEY (\"PLACE_NAME\");\n")
T.write("ALTER TABLE \"PLACES\" MODIFY (\"PLACE_NAME\" NOT NULL ENABLE);\n")
"Foreign Key로 연결"
T.write("ALTER TABLE \"PLACES\" ADD CONSTRAINT \"PLACES_FK\" FOREIGN KEY (\"STATION_NAME\") REFERENCES \"STATIONS\" (\"STATION_NAME\") ENABLE;\n")




