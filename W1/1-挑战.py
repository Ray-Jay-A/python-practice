#练习 1-挑战 工单批量判断
def judge(amount, is_vip):
    # amount = 退款金额，is_vip = 是不是 VIP 客户
    if is_vip and amount >= 100:
        return "直接同意退款"
    elif amount < 50:
        return "直接同意退款"
    else:
        return "转人工审核"


orders = [
    {"no": "A001", "amount": 120, "vip": True},
    {"no": "A002", "amount": 30, "vip": False},
    {"no": "A003", "amount": 80, "vip": False},
]

for i in orders:
    result = judge(i['amount'], i['vip'])
    print(f"订单{i["no"]}：{result}")