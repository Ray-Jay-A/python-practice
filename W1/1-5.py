#练习1-5 循环与 enumerate
reasons =["质量问题","尺码不合适","发错货","不想要了","物流太慢"]
for i,r in enumerate(reasons,start=1):
    print(f"第{i}类：{r}")
