# 🏁 练习 3-挑战 · 毕业作品 P0：退货原因统计报告

import pandas as pd

# ---------- 第 1 步：读数据 ----------
df = pd.read_excel("工单数据.xlsx")

# ---------- 第 2 步：分组统计【单数 + 总金额】----------
# as_index=False → 让“退货原因”保持成普通列，后面好排序、好调列
df_report = df.groupby("退货原因", as_index=False).agg(
    单数=("退款金额", "count"),
    总金额=("退款金额", "sum"),
)

# ---------- 第 3 步：加一列【占比】----------
# total = 所有单数加起来（也就是 100）
total = df_report["单数"].sum()
df_report["占比"] = (df_report["单数"] / total * 100).round(1)

# ---------- 第 4 步：按【单数】从多到少排序 ----------
df_report = df_report.sort_values("单数", ascending=False)

# ---------- 第 5 步：把列调成 退货原因 / 单数 / 占比 / 总金额 ----------
# ⚠️ 选多列要用两层方括号
df_report = df_report[["退货原因", "单数", "占比", "总金额"]]
df_report["总金额"] = df_report["总金额"].round(2)


print(df_report.to_string(index=False))
print()
print("已生成：退货原因统计报告.xlsx")

# 造一个只有 1 行的表，内容是合计
total_row = pd.DataFrame([{
    "退货原因": "合计",
    "单数": df_report["单数"].sum(),
    "占比": round(df_report["占比"].sum(), 1),
    "总金额": round(df_report["总金额"].sum(), 2),
}])

# pd.concat = 把两个表“上下拼起来”（ignore_index=True 表示重排行号 0,1,2…）
df_report = pd.concat([df_report, total_row], ignore_index=True)

df_report.to_excel("退货原因统计报告.xlsx", index=False)   # 再存一次