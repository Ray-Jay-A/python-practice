# Sql_Challenge SQLite 挑战

import sqlite3
import pandas as pd
data = pd.read_excel('D:/learn/code/W3/工单数据.xlsx')
conn = sqlite3.connect('工单.db')
e = conn.cursor()
data.to_sql('orders', conn, index=False, if_exists='replace')
conn.commit()
sql = 'select 退货原因, count(*) as th from orders group by 退货原因 order by th desc'
for row in e.execute(sql):
    print(row)
total = e.execute('select round(sum(退款金额),2) from orders ').fetchall()[0][0]
print(f'退款金额总计：{total}')
conn.close()
