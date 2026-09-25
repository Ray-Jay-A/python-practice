# 练习 3-2算「退款金额」的总和 / 平均
import pandas as pd
df = pd.read_excel('工单数据.xlsx')

amounts = df.loc[:,'退款金额']
print(round(amounts.sum(),2))
print(round(amounts.mean(),2))
print(len(amounts))
print(amounts.max())
print(amounts.min())
