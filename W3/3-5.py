# 练习 3-5 把统计结果导出 Excel

import pandas as pd

df = pd.read_excel('工单数据.xlsx')

amount = df.groupby('退货原因').agg(
    单数 = ('退款金额','count'),
    总金额 = ('退款金额','sum'),
).round(2)

print(amount)
amount.to_excel('退货原因统计.xlsx')