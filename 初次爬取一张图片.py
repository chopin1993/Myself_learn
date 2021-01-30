# coding:gbk
import os
import re

import requests

# 需求：爬取糗事百科中糗图板块下的所有糗图图片
if not os.path.exists("./糗图库"):  # 早桌面创建一个文件夹来存储图片数据
    os.mkdir("./糗图库")

url = "https://www.qiushibaike.com/imgrank/"  # 爬取整张“热图”页面
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
# 使用通用爬虫爬取
page_text = requests.get(url=url, headers=headers).text
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'  # 正则聚焦提取需要的数据
img_src_list = re.findall(ex, page_text, re.S)
# print(img_src_list)
for src in img_src_list:
    src = "https:" + src
    img_data = requests.get(url=src, headers=headers).content
    img_name = src.split("/")[-1]  # 将图片网址的最后一段作为图片名称（以“/”做列表切片）
    img_path = "./糗图库/" + img_name
    with open(img_path, "wb") as fp:
        fp.write(img_data)
        print(img_name, "爬取了一个图片！！")
