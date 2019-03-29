# _*_ coding:utf-8 _*_

import sqlite3

# 查询记录：
conn = sqlite3.connect('F:\\sqliteTest\\test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from realtimedata')
# 获得查询结果集:
values = cursor.fetchall()
for value in values:
    #获取第三列的值
    print(value[2])

conn.commit();
cursor.close()
conn.close()
