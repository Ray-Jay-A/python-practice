# 练习 4-3  用 params 查指定城市天气

import requests
url = 'https://api.open-meteo.com/v1/forecast'
params = {'latitude':22.657604,'longitude':114.064626,'current':'temperature_2m'}

r = requests.get(url, params=params)
print(r.status_code)

print(r.url)
temperature = r.json()
print(temperature['timezone'])
print(temperature['current']['temperature_2m'])





