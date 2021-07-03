# coding:utf-8
# 爬取梨视频
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
url = 'https://www.pearvideo.com/'
page_text = requests.get(url=url, headers=headers).text
# print(page_text)
tree = etree.HTML(page_text)
video_url = tree.xpath("//*[@id='pcCoverVideo']/@data-url")[
    0]  # //*[@id='vervideoTlist']/div/div/div/a/div[2]/div[2]/text()
video_name = tree.xpath("//*[@id='vervideoTlist']/div/div/div/a/div[2]/div[2]/text()")[0]
# print(video_url)
# print(video_name)
dic = {
    'name': video_name,
    'url': video_url
}
# 尚未完成，之后做，获取视频二进制后持久化
