# 复习-D1  pandas：退货原因统计
import pandas as pd

df = pd.read_excel('D:/learn/code/W3/工单数据.xlsx')
print(df['退货原因'].nunique())
data = df.groupby('退货原因').size().sort_values(ascending=False)
data.to_excel('D1-退货原因统计.xlsx')
print(round(df['退款金额'].sum(),2))