# coding:utf-8
# 爬取同花顺网站自选股票
import time

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}
"""股票名称：阳光电源，隆基股份，贵州茅台，华友钴业，华友钴业，亿纬锂能，比亚迪"""
url_list = ['http://stockpage.10jqka.com.cn/300274/', 'http://stockpage.10jqka.com.cn/601012/',
            'http://stockpage.10jqka.com.cn/600519/', 'http://stockpage.10jqka.com.cn/603799/',
            'http://stockpage.10jqka.com.cn/300014', 'http://stockpage.10jqka.com.cn/002594']
for url in url_list:
    url = url
    time.sleep(0.5)
    page_text = requests.get(url=url, headers=headers).text
    # print(page_text)
    tree = etree.HTML(page_text)
    stock_name = tree.xpath("//div[@class='m_header']//strong/@stockname")
    stock_code = tree.xpath("//div[@class='m_header']//strong/@stockcode")
    price_details = tree.xpath("//div[2]/div[2]/div[2]/table/tbody/tr[4]/td[4]/span")  # 重新配置xpath路径
    print(price_details)
    back_data = stock_name + stock_code
    print('股票数据：', back_data)
print('---全部爬取完成---')
