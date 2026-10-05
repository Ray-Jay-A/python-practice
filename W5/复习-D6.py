# 复习-D6 W1 基础语法（第二轮）：列表 + 字典 + for + if

#假数据
tickets = [
    {"no": "A001", "reason": "质量问题",   "amount": 260, "vip": False},
    {"no": "A002", "reason": "尺码不合适", "amount": 120, "vip": True},
    {"no": "A003", "reason": "发错货",     "amount": 90,  "vip": False},
    {"no": "A004", "reason": "质量问题",   "amount": 310, "vip": True},
]

counts = {"质量问题": 5, "尺码不合适": 3}
count = 0

for amounts in tickets:
    if amounts['amount'] >= 200:
        print(f'{amounts['no']} {amounts['reason']} {amounts['amount']} 【大额】')
        count += 1
    else:
        print(f'{amounts['no']} {amounts['reason']} {amounts['amount']}')
print(f'金额>=200的有：{count}单')

reason = counts.get('质量问题')
print(reason)
reason = counts.get('包装破损',0)
print(reason)


