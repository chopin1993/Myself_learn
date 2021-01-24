# coding:utf-8
import json
import time
import requests

url = "https://movie.douban.com/j/search_subjects"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
type = input("输入：")
param = {
    "type": type,
    "tag": "热门",
    "sort": "recommend",
    "page_limit": "20",
    "page_start": "0"
}
response = requests.get(url=url, params=param, headers=headers)
list_file = response.json()
fp = open("./douban.json", "w", encoding="utf-8")
json.dump(list_file, fp=fp, ensure_ascii=False)  # 将Python数据结构转换成json数据，json.loads将json转换成Python数据结构
print("豆瓣电影爬取完成！！---->时间戳：", time.asctime(time.localtime(time.time())))
