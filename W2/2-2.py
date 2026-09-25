# 练习 2.2 把文件读出来（read 一次全读 + 逐行读）
f=open('退货原因.txt','r',encoding='utf-8')
txt=f.read()
f.close()
print(txt)
f2=open('退货原因.txt','r',encoding='utf-8')
for i,line in enumerate(f2,start=1):
    line=line.strip("\n")
    print(f'第{i}行：{line}')
f2.close()

