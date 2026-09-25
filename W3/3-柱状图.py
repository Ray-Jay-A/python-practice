# 练习 3-柱状图 柱状图

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

report = pd.read_excel("退货原因统计报告.xlsx")
report = report[report["退货原因"] != "合计"]
report = report.sort_values("单数", ascending=False)

# plt.figure(figsize=(8, 5))
plt.bar(report["退货原因"], report["单数"])    # 画柱状图：x = 原因，y = 单数
plt.title("各退货原因单数分布")                  # 标题
plt.xlabel("退货原因")                          # x 轴名称
plt.ylabel("单数")                              # y 轴名称
plt.tight_layout()                              # 自动调边距，防止字被裁掉
plt.savefig("退货原因柱状图.png", dpi=150)       # 存成图片（dpi 越大越清晰）
plt.show()                                      # 弹窗看一眼（可选）

