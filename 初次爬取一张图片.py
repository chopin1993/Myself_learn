# coding:gbk
import os
import re
import time

import requests
import datetime
# 需求：爬取糗事百科中糗图板块下的所有糗图图片
if not os.path.exists("./糗图库"):  # 早桌面创建一个文件夹来存储图片数据
    os.mkdir("./糗图库")

url = "https://www.qiushibaike.com/imgrank/page/%d/"  # 爬取整张“热图”页面https://www.qiushibaike.com/imgrank/page/9/
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

starttime = datetime.datetime.now()     # 计算爬取时间，开始时间点

for page_Num in range(1, 14):
    new_url = format(url % page_Num)
    # 使用通用爬虫爬取
    page_text = requests.get(url=new_url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'  # 正则聚焦提取需要的图片url
    img_src_list = re.findall(ex, page_text, re.S)
    for src in img_src_list:
        src = "https:" + src
        img_data = requests.get(url=src, headers=headers).content
        img_name = src.split("/")[-1]  # 将图片网址的最后一段作为图片名称（以“/”做列表切片）
        img_path = "./糗图库/" + img_name
        with open(img_path, "wb") as fp:
            fp.write(img_data)
            print(img_name, "爬取了一个图片！！")
print("All ready!!--->>爬取时间：", time.asctime(time.localtime(time.time())))
endtime = datetime.datetime.now()       # 计算爬取时间，结束时间点
print("爬取用时(秒)：", (endtime - starttime).seconds)
