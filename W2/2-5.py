# 练习2-5 重写最卡那题（追加 + 文件指针，用 "a+" 一个对象搞定）
with open("退货原因.txt","w",encoding='utf-8')as f:
    f.write("质量问题\n尺码不合适\n发错货\n不想要了\n物流太慢\n")

with open("退货原因.txt","a+",encoding='utf-8')as f:
    print(f'刚打开，指针在{f.tell()}')
    f.write("包装破损\n少发件\n")
    f.seek(0)
    print(f'seek(0)后，指针在{f.tell()}')
    for i,lines in enumerate(f.readlines(),start=1):
        print(f'第{i}行：{lines.strip("\n")}')

