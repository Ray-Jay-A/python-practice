# 练习2-挑战 工单关键词统计报告

records = ['尺码不合适','质量问题','发错货','尺码不合适','质量问题','物流太慢','质量问题','尺码不合适','质量问题','物流太慢']
counts={}
with open('工单记录.txt','w',encoding='utf-8') as f:
    for r in records:
        f.write(r+'\n')

with open('工单记录.txt','r',encoding='utf-8') as f:
    for line in f:
        counts[line.strip("\n")]=counts.get(line.strip("\n"),0)+1
    for k,v in sorted(counts.items(),reverse=True):
        print(f'{k}：{v}次')

with open('统计结果.txt', 'w', encoding='utf-8') as f3:
    for k, v in counts.items():
        text = f'{k}：{v} 次'    # ← 只在这里定义一次格式（全角冒号 + 空格 + 次）
        f3.write(text + '\n')    # 文件也用它
