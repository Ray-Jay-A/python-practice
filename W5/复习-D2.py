# 复习-D2  W1 基础语法：列表 + 字典 + for + if

orders = [
    {"no": "A001", "amount": 120, "vip": True},
    {"no": "A002", "amount": 30, "vip": False},
    {"no": "A003", "amount": 80, "vip": False},
]

counts = {"质量问题": 12, "尺码不合适": 8, "发错货": 3}

for i in orders:
    print(f'{i['no']} 金额 {i['amount']}')
print(len(orders))
count = 0
for i in orders:
    if i['amount'] >= 100:
        count += 1
print(count)
key = input('取出哪个问题的次数：')
if input in counts:
    print(counts[key])
else:
    print(0)


