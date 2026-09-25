#练习1-4-重写 重写（is / == / bool() 复习）
def judge(amount,is_vip):
    if (is_vip and amount>=100) or amount<50:
        return "直接同意退款"
    else:
        return "转人工审核"

print(judge(120, True))
print(judge(30, False))
print(judge(80, False))
print(judge(100, True))
print(judge(50, False))
print(judge(49.9, False))
print(judge(100, False))
print(100 == 100) #True
print("abc" == "abc") #True
print(bool(0)) #False
print(bool("0")) #True




