# 练习 4-5 请求 → 存 weather.json → 读回来

import requests
import json

url = 'https://api.open-meteo.com/v1/forecast'
params = {'latitude':39.90, 'longitude':116.40, 'current':'temperature_2m'}

r = requests.get(url,params=params,timeout=10)
print(r.raise_for_status())
data = r.json()
print(data['current']['temperature_2m'])

with open('weather.json', 'w',encoding='utf-8') as f:
    json.dump(data, f,ensure_ascii=False,indent=2)

with open('weather.json', 'r',encoding='utf-8') as f:
    data2 = json.load(f)
    print(data2['current']['temperature_2m'])
    print(type(data2))





