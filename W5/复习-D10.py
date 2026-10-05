# 复习-D10 SQL 链路独立重做：W3 工单 → SQLite → SQL

import sqlite3
import pandas as pd
data = pd.read_excel('D:/learn/code/W3/工单数据.xlsx')
conn = sqlite3.connect('D10.db')
e = conn.cursor()
data.to_sql('orders', con=conn, if_exists='replace', index=False)
print(data.shape)
print(list(data.columns))
avg_tkje = e.execute('Select 退货原因,count(*) as 单数,round(avg(退款金额),2) as 平均退款金额 from orders group by 退货原因 order by 单数 DESC')
for row in avg_tkje:
    print(row)
conn.close()