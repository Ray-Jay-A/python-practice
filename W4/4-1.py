# 练习 4-1 发第一个 GET 请求

import requests
url = 'https://api.open-meteo.com/v1/forecast?latitude=22.72&longitude=114.25&current=temperature_2m'
r = requests.get(url)
print(r.status_code)

print(type(r))
print(r.text[:200])
