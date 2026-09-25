# 练习 3-3统计每种退货原因各多少
import pandas as pd
df = pd.read_excel('工单数据.xlsx')

reason = df.loc[:,'退货原因']
counts = reason.value_counts()
print(f'{counts}\n')

counts = reason.value_counts(normalize=True)#给的是小数的占比
print(f'{counts}\n')

counts = reason.value_counts(ascending=True)#让结果从少到多
print(f'{counts}\n')