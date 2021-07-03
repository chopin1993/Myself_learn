# coding:utf-8
# 爬取百度热榜新闻2021-02-17
import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    url = 'https://www.baidu.com/s?wd=%E7%83%AD%E7%82%B9%E6%96%B0%E9%97%BB&rsv_spt=1&rsv_iqid=0xd97945400049d38f&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=88093251_57_hao_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=17&rsv_sug1=10&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=5732&rsv_sug4=49084'
    page_text = requests.get(url=url, headers=headers).text
    # print(page_text)
    tree = etree.HTML(page_text)
    hot_news_list = tree.xpath("//*[@id='con-ar']/div[2]/div/div/table/tbody/tr/td/a/@title")  # 获取新闻标题
    row_news_url_list = tree.xpath("//*[@id='con-ar']/div[2]/div/div/table/tbody/tr/td/a/@href")  # 获取新闻url
    # print(news_url)
    post_url_list = []  # 存储热搜的URL
    for news_url in row_news_url_list:
        post_url = "https://www.baidu.com/" + news_url
        post_url_list.append(post_url)
    # print(post_url_list)
    fp = open('百度热搜.text', 'w', encoding='utf-8')
    for news in hot_news_list:
        fp.write(news + '   ' + '\n')
    print('爬取完成！共 {0} 条热点新闻。'.format(len(hot_news_list)))
    for i in post_url_list:
        fp.write(i + '\n')
