# _*_ coding:utf-8 _*_


import psycopg2

conn = psycopg2.connect(dbname='qhsoam_dev', user='pguser', password='pguser', host='127.0.0.1', port='8101')
cur = conn.cursor()
# 查询sql
cur.execute("select wtid from onedata order by rectime desc limit 100")
# 插入sql
# cur.execute( "INSERT INTO public.onedata (wfid, wtid, rectime, windspeed, realpower, theorypower, wtstatus, limitstatus, faultcode, stopcode, envitemp, beginelec, endelec, limitcode, defresipid, upresipid, upstopcode, uprectime) VALUES ('632809', '632809058', '2019-03-27 02:31:00', '15.66', '1566.00', '1576.55', 'null', '0', '', '', '-26.44', '6.32', '16.32', '', '8', NULL, NULL, NULL);")
# 获取结果
rows = cur.fetchall()
for row in rows:
    print(row[0])

# 提交事务
conn.commit
cur.close()
conn.close()
