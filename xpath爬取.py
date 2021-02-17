# coding:utf-8
# 爬取58二手房信息
import requests
from lxml import etree

url = 'https://qd.58.com/ershoufang/?utm_source=market'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).text
# print(page_text)
tree = etree.HTML(page_text)
# print(tree)
name_list = tree.xpath(
    "//section[@class='list']//div[@class='property-content-title']/h3[@title]/text()")  # //div[@class='property-content-title']/h3/text()
# price = tree.xpath("//*[@id='__layout']/div/section/section[3]/section[1]/section[2]/div/a/div/div/p/text()")
print(name_list)
# for name in name_list:
#     print(name)
# print(text)
fp = open('58.text', 'w', encoding='utf-8')
for h3 in page_text:
    fp.write(h3)
