# 练习 2.3 追加 + 文件指针

f=open("退货原因.txt",'w',encoding="UTF-8")
reasons = ["质量问题","尺码不合适","发错货","不想要了","物流太慢"]
for reason in reasons:
    f.write(f'{reason}\n')
f.close()

with open("退货原因.txt","a",encoding="UTF-8")  as f1:
    f1.write("包装破损\n")
    f1.write("少发件\n")


with open("退货原因.txt","r",encoding="UTF-8")  as f2:
    print(f2.tell())
    lines = f2.readlines()
    print(f2.tell())
    print(f2.seek(0))
    for i,line in enumerate(lines,start=1):
        print(f'第{i}行：{line.strip("\n")}')




