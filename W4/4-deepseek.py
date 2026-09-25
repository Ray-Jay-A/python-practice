# 练习 4-deepseek 接 DeepSeek
import json

import requests
import os
from dotenv import load_dotenv
load_dotenv(r'D:/learn/key.env')
api_key = os.environ['DEEPSEEK_API_KEY']

url ='https://api.deepseek.com/chat/completions'
header = {'Authorization': 'Bearer ' + api_key}
body = {
    'model':'deepseek-v4-flash',
    'messages':[
        {'role':'system','content':'你是电商客服助手，回答要简短,专业'},
        {'role':'user','content':'用一句话解释什么是 JSON',}
    ]
}
try:
    r = requests.post(url,headers = header, json=body,timeout=60)
    print(r.status_code)
    data = r.json()
    print(data)
    print(data['choices'][0]['message']['content'])
except requests.exceptions.RequestException as e:
    print(e)

with open('deepseek_reply.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False)

with open('deepseek_reply.json','r',encoding='utf-8') as f:
    data2 = json.load(f)
    print(data2)
    print(data2['usage']['total_tokens'])






