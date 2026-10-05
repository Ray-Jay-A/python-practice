# 复习-D8 W4 网络+JSON（第二轮）：带参数请求 + 错误处理

import requests
url = 'https://api.open-meteo.com/v1/forecast'
params = {'latitude':39.9,'longitude':116.4,'current':'temperature_2m'}
try:
    r = requests.get(url, params=params, timeout=10)
    print(r.status_code)
    r.raise_for_status()
    data = r.json()
    temp = data['current']['temperature_2m']  # 先取值
    unit = data['current_units']['temperature_2m']  # 单位从数据里拿，别写死
    print(f"北京现在：{temp} {unit}")  # 外层双引号、内层单引号 → 到哪都对

except requests.exceptions.RequestException as e:
    print(e)


