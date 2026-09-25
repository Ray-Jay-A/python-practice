# 练习 4-4 错误处理（让程序不崩）

import requests
url = 'https://api.open-meteo.com/v1/forecast'
params = {'latitude':39.90,'longitude':116.40,'current':'temperature_2m'}
try:
    r = requests.get(url,timeout=10, params=params)
    r.raise_for_status()
    print(r.status_code)
    data = r.json()
    print(data['current']['temperature_2m'])
except requests.exceptions.RequestException as e:
    print(e)
# r = requests.get(url,timeout=0.001,params=params)
# print(r.raise_for_status())
# data = r.json()
# print(data['current']['temperature_2m'])

url = 'https://api.open-meteo.com/v1/forecast/notfound'
try:
    r = requests.get(url,timeout=10)
    r.raise_for_status()
    print('第二段不应该执行这里')
except requests.exceptions.RequestException as e:
    print("第二段如期出错（程序没崩）",e)


