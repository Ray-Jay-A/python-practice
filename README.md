# python语法练习 （以下内容的全部数据均为虚假数据，个人学习用，非商用，不涉及任何同名产品）
## W1 Python 基础练习
运行方式：在 PyCharm 里打开对应文件，点运行（▶）
数据：全部为自己编的假数据
实现：变量与 f-string，列表索引，字典与 .get()，条件判断，for 循环，工单批量处理 + 工单退款判断（judge 函数）

## W2 Python 文件读写
open 的四种模式（r / w / a / a+）、read / readline / readlines、逐行读、文件指针（tell / seek）、把统计结果写成一份报告
关于关闭文件：用 open 打开的，最后要自己写 .close()；用 with 打开的，会自动关闭，不用自己写

## W3 pandas 入门（读 Excel → 统计 → 出报告）
读 Excel（read_excel）、取列、sum / mean / len、value_counts、groupby + agg、sort_values、to_excel、matplotlib 柱状图
产出：毕业作品 P0 —— 运行一次生成「退货原因统计报告.xlsx」+「退货原因柱状图.png」

## W4 调 API（requests + JSON）
requests 用来给 API 发请求、把返回数据取回来；返回的是 Response 对象，里面有状态码和正文，正文常用 JSON，用 .json() 一解析就变成字典
用到：requests.get / .json() / params / headers / requests.post / try-except / raise_for_status / json.dump 与 json.load
产出：第一次调用 DeepSeek API（`code\W4\4-deepseek.py`）

## W5 SQL 与 SQLite（读数据 → 存进数据库 → 用 SQL 查）

- 在廖雪峰的在线 SQL 上练了：`SELECT` / `WHERE` / `ORDER BY` / `COUNT` / `AVG` / `GROUP BY` / `INSERT` / `UPDATE` / `DELETE`
- 用 Python 自带的 `sqlite3`（不用装数据库）：`connect` / `cursor` / `execute` / `commit` / `fetchall`
- 用 pandas 把 Excel 灌进数据库：`df.to_sql(...)`；再用 `pd.read_sql(...)` 读回来
- 复现：`python sql_challenge.py` → 在 `工单.db` 里生成 `orders` 表，查出「每种退货原因各多少单」

## 文件一览
- `W1\` —— W1 练习（`1-1.py` … `1-挑战.py`）
- `W2\` —— W2 练习（`2-1.py` … `2-挑战.py`）+ 它产生的假数据（`退货原因.txt` / `工单描述.txt` / `工单记录.txt` / `统计结果.txt`）
- `W3\` —— W3 练习（`3-1.py` … `3-挑战.py`）+ `3-柱状图.py` + 假数据（`工单数据.xlsx`）+ 产出（`退货原因统计报告.xlsx` / `退货原因柱状图.png`）
- `W4\` —— W4＝调 API：`requests.get` / `.json()` / `params` / `try-except` / `json 存读`
- `README.md` —— 本文件
- `W5\` —— W5＝SQL 与 SQLite：`sql_demo.py`（建表/插入/查询）+ `sql_challenge.py`（Excel → SQLite → SQL）+ 复习题 `复习-D1.py` … `复习-D11.py`


