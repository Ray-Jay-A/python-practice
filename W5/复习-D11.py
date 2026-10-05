# 复习-D11 W1 基础语法（第三轮）：写一个函数 + 批量调用

def level(amount):
    if amount >=500:
        return '大额'
    elif amount >0 and amount <200:
        return '小额'
    else:
        return '中额'
orders = [
    {"no": "TK-1001", "amount": 620},
    {"no": "TK-1002", "amount": 210},
    {"no": "TK-1003", "amount": 90},
    {"no": "TK-1004", "amount": 500},
    {"no": "TK-1005", "amount": 200},
]
count_amount_level = 0
for i,order in enumerate(orders,start=1):
    amount_level = level(order['amount'])
    print(f'第{i}单：{order["no"]} 金额：{order["amount"]}->{amount_level}')
    if amount_level == '大额':
        count_amount_level +=1
print(f'有{count_amount_level}个大额')
