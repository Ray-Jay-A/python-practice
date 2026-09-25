# 练习3-1 把 Excel 读进来

import  pandas as pd

df = pd.read_excel('工单数据.xlsx')
print(df)
print(df.shape)
print(list(df.columns))
print(df.head(5))
print(type(df))
print(type(df['退款金额']))