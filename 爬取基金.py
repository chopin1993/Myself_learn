# coding:gbk
# 爬取自选基金数据
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}
url = 'http://fund.10jqka.com.cn/zixuan/index.html'
page_text = requests.get(url=url, headers=headers).text
# print(page_text)
tree = etree.HTML(page_text)
tr_list = tree.xpath("/html/body/div[2]/div[2]/div[2]/table//text()")
print(tr_list)

# stockcode = tree.xpath("//div[@class='m_header']//strong/@stockcode")
# price_details = tree.xpath("//div//span[@class='price_plus']/@id")
# back_data = name + stockcode + price_details