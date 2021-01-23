# coding:utf-8
# 爬取百度翻译，20210117

import json
import time

import requests

url = "https://fanyi.baidu.com/sug"
keyword = input("输入查询的关键词")
data = {
    "kw": keyword
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
response = requests.post(url=url, data=data, headers=headers)
dic_obj = response.json()
file_name = keyword + ".json"
fp = open(file_name, "w", encoding="utf-8")
json.dump(dic_obj, fp=fp, ensure_ascii=False)
print("百度翻译爬取完成！！---->时间戳：", time.asctime(time.localtime(time.time())))
