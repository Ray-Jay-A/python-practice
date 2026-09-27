# 复习-D5 pandas（W3）第二轮：分组统计

import pandas as pd
data = pd.read_excel('D:/learn/code/W3/工单数据.xlsx') #读取表
print(data.shape) #查看行列
print(set(data.columns))  # 查看列名
is_vip = data.groupby('是否VIP')['退款金额'].sum().round(2)  #根据是否是VIP分组查看统计退款金额
print(is_vip)
order_by = data.groupby('退货原因')['退款金额'].mean().round(2).sort_values(ascending=False) #根据退货原因分组查看退款金额的平均数 然后按从大到小排序
print(order_by)


