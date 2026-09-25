# ======================================================================
# 【对照用】这个文件分两半：
#   上半 = 你写的原版（全部注释掉了，留作对照）
#   下半 = AI 改好的版本（只改了几处，改动都写在旁边注释里）
# ======================================================================


# ----------------------------------------------------------------------
# 你的原版（注释掉，留作对照）
# ----------------------------------------------------------------------
# # 练习 4-挑战 封装 get_weather(city) 函数
#
# import requests
# import json
#
# url = 'https://api.open-meteo.com/v1/forecast'
# def get_weather(city):
#     coords= {'北京':{'latitude':39.90,'longitude':116.40}
#                  ,'上海':{'latitude':31.23,'longitude':121.47}
#                  ,'广州':{'latitude':23.13,'longitude':113.26}
#                  ,'香港':{'latitude':22.32,'longitude':114.17}}
#     if city not in coords:
#         return '没有收录这个城市：{}'.format(city)
#
#     else:
#         paramas = {'latitude':coords[city]['latitude'],
#                     'longitude':coords[city]['longitude'],
#                     'current':'temperature_2m'}
#         r = requests.get(url, params=paramas, timeout=10)
#         print(r.raise_for_status())
#
#     try:
#         data = r.json()
#         return data['current']['temperature_2m']
#     except requests.exceptions.RequestException as e:
#         return e
#
#
# print(get_weather('北京'))
# print(get_weather('上海'))
# print(get_weather('广州'))
# print(get_weather('香港'))
# print(get_weather('火星'))


# ----------------------------------------------------------------------
# AI 修改版（对照用）
# ----------------------------------------------------------------------

# 这块在干什么：只拿 requests 就够了（json 这题没用到，删掉）
import requests

url = 'https://api.open-meteo.com/v1/forecast'


# 这块在干什么：定义一个函数 —— 输入城市名，返回该城市气温（或一句提示）
def get_weather(city):
    # 这块在干什么：城市 → 经纬度 的对照表
    coords = {
        '北京': {'latitude': 39.90, 'longitude': 116.40},
        '上海': {'latitude': 31.23, 'longitude': 121.47},
        '广州': {'latitude': 23.13, 'longitude': 113.26},
        '香港': {'latitude': 22.32, 'longitude': 114.17},
    }

    # 这块在干什么：错误处理 1 —— 城市不在表里，提前返回一句提示
    if city not in coords:
        return f'没有收录这个城市：{city}'      # 改动：.format() 换成 f-string

    # 这块在干什么：把要发给服务器的参数拼成一个字典
    # 改动：去掉了 else（上面 if 里已经 return，这里少缩进一层更清爽）
    params = {
        'latitude': coords[city]['latitude'],
        'longitude': coords[city]['longitude'],
        'current': 'temperature_2m',            # 固定参数
    }

    # 这块在干什么：错误处理 2 —— 把「所有危险动作」都放进 try 里
    # 重点改动：requests.get 和 raise_for_status() 从 try 外面搬进来了
    # （真正会出错的是它们：网络断、域名错、404/500）
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()                    # 改动：去掉 print（不打印 None）
        data = r.json()
        return data['current']['temperature_2m']
    except requests.exceptions.RequestException as e:
        return f'查询失败：{e}'                  # 改动：返回提示文字，而不是异常对象


# 这块在干什么：调用函数，测 5 个城市（最后一个走「不在表里」那条路）
print(get_weather('北京'))
print(get_weather('上海'))
print(get_weather('广州'))
print(get_weather('香港'))
print(get_weather('火星'))
