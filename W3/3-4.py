# 练习 3-4 按退货原因分组求总金额
import pandas as pd

df = pd.read_excel('工单数据.xlsx')
amount = df.groupby('退货原因',as_index=True)['退款金额'].sum()
print(amount.round(2))

# 同时看 单数 + 总金额
print(df.groupby("退货原因")["退款金额"].agg(["count", "sum","mean"]).round(2))

# 每种原因各几单（= 3.3 的另一种写法）
print(df.groupby("退货原因").size())
