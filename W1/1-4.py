# 练习 1.4 条件判断：判断一张工单该不该直接退款
# 2026/9/14

def judge(amount, is_vip):
    # amount = 退款金额，is_vip = 是不是 VIP 客户
    if is_vip and amount >= 100:
        return "直接同意退款"
    elif amount < 50:
        return "直接同意退款"
    else:
        return "转人工审核"


# ---- 题目指定的三个验证输入，后面注释是"应该"的输出 ----
print(judge(120, True))     # 直接同意退款
print(judge(30, False))     # 直接同意退款
print(judge(80, False))     # 转人工审核

print(judge(100, True))    # 正好 100，VIP "直接同意退款"
print(judge(50, False))    # 正好 50，非 VIP "转人工审核"
print(judge(49.9, False))  # 差一点不到 50 "直接同意退款"
print(judge(100, False))   # 金额够但非 VIP "转人工审核"