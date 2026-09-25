# 练习2-4 统计关键词出现次数
with open('工单描述.txt','w',encoding='utf-8') as f:
    f.write('尺码不合适\n质量问题\n尺码不合适\n物流太慢\n质量问题\n质量问题')

with open('工单描述.txt','r',encoding='utf-8')as f:
    counts={}

    for line in f.readlines():
        if line.strip("\n") not in counts:
            counts[line.strip("\n")]=1
        else:
            counts[line.strip("\n")]+=1
        # counts[line.strip("\n")] = counts.get(line.strip("\n"), 0) + 1

    for k,v in counts.items():
        print(f'{k}：{v}次')