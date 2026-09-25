# 练习 2.1 把退货原因写进文件
f=open("退货原因.txt",'w',encoding="UTF-8")
reasons = ["质量问题","尺码不合适","发错货","不想要了","物流太慢"]
for reason in reasons:
    f.write(f'{reason}\n')
f.close()