# coding：utf-8
# 魔镜摄影图片爬取--单页爬取后下载图片
import os

import requests
from lxml import etree

if not os.path.exists("F:/魔镜美女"):  # 在F盘创建一个文件夹来存储图片数据
    os.mkdir("F:/魔镜美女")

url = "https://www.520mojing.com/thread-28491-1-19.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

page_piku = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_piku)
td_list = tree.xpath("//td[@class='t_f']/ignore_js_op/img/@src")  # xpath解析网页文件
# print(td_list)
for p_url in td_list:
    get_photo = requests.get(url=p_url, headers=headers).content
    img_name = p_url.split("/")[-1]  # 将图片网址的最后一段作为图片名称（以“/”做列表切片）
    img_path = "F:/魔镜美女/" + img_name  # 路径和文件名
    with open(img_path, "wb") as fp:
        fp.write(get_photo)  # 二进制形式写入文件
        print(img_name, "爬取了一个图片！！")

print("爬取到的图片数量：", len(td_list))
