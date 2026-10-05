# sql_demo SQL 第 3 天 · 预计 35 分钟（可拆两段：读 ~12 + 练 ~20）
import sqlite3
conn = sqlite3.connect('demo.db')
c = conn.cursor()
# c.execute('create table if not exists orders (id INTEGER PRIMARY KEY,reason TEXT,amount REAL)  ')
# c.execute('insert into orders(reason , amount) values("质量问题",198.11 )')
# c.execute('insert into orders(reason , amount) values("尺码不合适",332.62)')
# c.execute('insert into orders(reason , amount) values("质量问题",465.32)')
conn.commit()
rows = c.execute('select * from orders').fetchall()
print(len(rows))
for row in rows:
    print(row)
rows = c.execute('select reason,count(*) from orders group by reason').fetchall()
print(f'按原因统计：{rows}')
conn.close()
