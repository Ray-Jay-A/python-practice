# 复习-D4  W4 网络+JSON：读 JSON → 存 JSON → 读回

import json

# ① 读回来，看整份数据
with open("D:/learn/code/W4/weather.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)

# ② 取出温度和单位，拼成一句打印
temp = data["current"]["temperature_2m"]
unit = data["current_units"]["temperature_2m"]
print(temp)                       # 28.8
print(unit)                       # °C
print(f"当前温度：{temp} {unit}")  # 当前温度：28.8 °C

# ③ 把自己造的记录存成 JSON（中文原样 + 缩进 2 格）
records = {"城市": "北京", "温度": 28.8, "单位": "°C"}
with open("D:/learn/code/W5/D4-我的记录.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

# ④ 再读回来
with open("D:/learn/code/W5/D4-我的记录.json", "r", encoding="utf-8") as f:
    back = json.load(f)           # 换个名字，别和上面的 data 混
print(back["城市"])               # 北京
