# coding:utf-8
# 爬取猫眼电影票房排行榜
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
url = 'http://piaofang.maoyan.com/dashboard'
page_text = requests.get(url=url, headers=headers).text
print(page_text)
# tree = etree.HTML(page_text)
# tr_list = tree.xpath("//*[@id='app']/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td[1]")    # //*[@id="app"]/div/div/div[2]/div[1]/div[2]/div
# print(tr_list)
# for movie in tr_list:
#     title = tree.xpath('。/td[1]/text()')
    # print(title)
