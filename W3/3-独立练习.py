# 练习 3-独立练习 个人单独完成

import pandas as pd

df = pd.read_excel('工单数据.xlsx')

is_vip = df.groupby('是否VIP',as_index=False).agg(
    单数=('退款金额','count'),
    总金额=('退款金额','sum'),
).round(2)

print(is_vip)

total = is_vip['单数'].sum()
ratio = (is_vip['单数']/total * 100).round(2)

is_vip['占比'] = ratio
is_vip = is_vip[['是否VIP','单数','占比','总金额']]
is_vip = is_vip.sort_values('单数',ascending=False) #ascending 默认True 从小到大排序

is_vip.to_excel('VIP统计.xlsx',index=False)
print(is_vip.to_string(index=False))

total_row = pd.DataFrame([{
    '是否VIP':'合计',
    '单数':is_vip['单数'].sum(),
    '占比':is_vip['占比'].sum(),
    '总金额':is_vip['总金额'].sum(),
}])

is_vip = pd.concat([is_vip,total_row],ignore_index=True)
print(is_vip)

