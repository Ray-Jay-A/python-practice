# 复习-D7 W2 文件读写（第二轮）：写 → 追加 → 读回 + enumerate

with open('D7-工单备注.txt','w',encoding='utf-8') as f:
    f.write("A001 已退款\n"
            "A002 等待客户确认\n"
            "A003 已补发\n"
            "A004 客户催过一次\n"
            "A005 已退款\n")

with open('D7-工单备注.txt','a',encoding='utf-8') as f:
    f.write("A006 已补发\n"
            "A007 等待客户确认\n")

with open('D7-工单备注.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    print(f'总行数：{len(lines)}')
    for i,line in enumerate(lines,start=1):
        line = line.strip('\n')
        print(f'第{i}行：{line}')


