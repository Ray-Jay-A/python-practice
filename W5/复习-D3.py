# 复习-D3 W2 文件读写：读文件 → 统计 → 写文件

with open('D:/learn/code/W2/工单记录.txt','r',encoding='utf-8') as f:
    data = f.readlines()
    lens = len(data)
    print(f'总行数：{lens}')
    print(data)
    lines ={}
    for line in data:
        r=line.strip('\n')
        lines[r] = lines.get(r,0)+1
    for k,v in lines.items():
        print(f'{k}:{v}次')

with open('D3-统计结果.txt','w',encoding='utf-8') as f:
    for k, v in lines.items():
        f.write(f'{k}： {v}次\n')




