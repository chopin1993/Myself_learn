# coding:utf-8
# 爬虫四步走：1.指定URL 2.发起请求  3.获取响应数据    4.数据持久化。
import requests
import time

# 指定URL
url = "https://www.hao123.com/?tn=48020221_35_hao_pg"
# 发起请求
back = requests.get(url=url)
# 获取响应数据
file = back.text
# print(file)
# 数据持久化
with open("file", mode='w', encoding="utf-8") as fp:
    fp.write(file)
print("爬取数据完成！！！爬取时间：", time.asctime(time.localtime(time.time())))
