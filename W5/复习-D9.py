# 复习-D9   pandas（W3 第三轮）：「退货日期」这条轴

import pandas as pd
data = pd.read_excel('D:/learn/code/W3/工单数据.xlsx')
print(data.shape)

print(data['退货日期'].min())
print(data['退货日期'].max())
print(data.sort_values('退货日期')[['工单号', '退货日期']].head(3))
print(data.value_counts('退货日期',ascending=False).head(1))
