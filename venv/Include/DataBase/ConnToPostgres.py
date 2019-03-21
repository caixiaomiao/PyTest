#_*_ coding:utf-8 _*_


import psycopg2
conn=psycopg2.connect(database='ssjz',user='postgres',password='postgres',host='127.0.0.1',port='5434')
cur=conn.cursor()
cur.excute("select * from onedata order by rectime desc limit 100")
rows=cur.fetchall()
print(rows)
conn.commit
cur.close()
conn.close()