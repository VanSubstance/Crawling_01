import pymysql
import matplotlib.pyplot as plt

conn = pymysql.connect(host= 'localhost', user= 'root', password= '123456', db= 'teamdb', charset= 'utf8mb4')

cur = conn.cursor()

query = "select * from restaurants;"
cur.execute(query)
conn.commit()

Table = cur.fetchall()
maxx = 10
minn = 0
for i in Table:
    i = list(i)
    i[3] = int(i[3].replace(",", ""))
    if maxx < i[3]:
        maxx = i[3]
    if minn > i[3]:
        minn = i[3]
        
stationRevNum = [0 for i in range(maxx + 1)]
for i in Table:
    i = list(i)
    i[3] = int(i[3].replace(",", ""))
    stationRevNum[i[3]] += 1

plt.figure(figsize= (16, 8))
plt.title("Review number: box plot")
plt.boxplot(stationRevNum, vert = 0)
plt.show
"""
plt.figure(figsize = (16, 8))
plt.title("Review number: bar chart")
plt.bar(range(0, maxx + 1), stationRevNum)
plt.show
"""
query = "select ctgrgroup, count(*) from restaurants group by ctgrgroup;"
cur.execute(query)
conn.commit()

Table2 = cur.fetchall()
restCtgrNum = [0 for i in range(len(Table2))]
restCtgr = ["" for i in range(len(Table2))]
for i in range(len(Table2)):
    restCtgr[i] = Table2[i][0]
    restCtgrNum[i] = Table2[i][1]


plt.figure(figsize= (10, 5))
plt.bar(restCtgr, restCtgrNum)
plt.show   