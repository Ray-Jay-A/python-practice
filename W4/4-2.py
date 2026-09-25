# 练习 4-2 把 JSON 取出来、打印几个字段

import requests
url = 'https://api.open-meteo.com/v1/forecast?latitude=22.72&longitude=114.25&current=temperature_2m'

r = requests.get(url)

data = r.json()

print(type(data))
print(data)
print(data["timezone"])
print(data["current"]["temperature_2m"])
print(data["current"])

temp = data["current"]["temperature_2m"]
print(f'香港当前气温：{temp}°C')

