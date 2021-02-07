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
text_h3 = tree.xpath(
    "//section[@class='list']//div[@class='property-content-title']/h3/text()")  # //div[@class='property-content-title']/h3/text()
# print(text)
fp = open('58.text', 'w', encoding='utf-8')
for h3 in text_h3:
    fp.write(h3+'\n')
print('完成！')
