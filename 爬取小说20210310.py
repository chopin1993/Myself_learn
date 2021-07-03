# coding:utf-8

import time

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

"""
# 获取各个章节的URL，生成列表
url_chapter = "https://www.wodeshucheng.com/book_174323/"
page_chapter = requests.get(url=url_chapter, headers=headers).text
print(page_chapter)
tree_chpater = etree.HTML(url_chapter)
chpater_list = tree_chpater.xpath("/html/body//ul[2]/li[2]/dl/dd/a/@href")
# print(chpater_list)
# 拼接生成完整的URL
full_url_List = []
for urls1 in chpater_list:
    post_url = "https://www.wodeshucheng.com/" + urls1
    full_url_List.append(post_url)
print(full_url_List)
"""

urls = ["https://yuedu.bmsgzw.cn/book/2621/26210001","https://yuedu.bmsgzw.cn/book/2621/26210002",
        "https://yuedu.bmsgzw.cn/book/2621/26210003","https://yuedu.bmsgzw.cn/book/2621/26210004",
        "https://yuedu.bmsgzw.cn/book/2621/26210005","https://yuedu.bmsgzw.cn/book/2621/26210006",
        "https://yuedu.bmsgzw.cn/book/2621/26210007","https://yuedu.bmsgzw.cn/book/2621/26210008",
        "https://yuedu.bmsgzw.cn/book/2621/26210009","https://yuedu.bmsgzw.cn/book/2621/26210010",
        "https://yuedu.bmsgzw.cn/book/2621/26210011","https://yuedu.bmsgzw.cn/book/2621/26210012",
        "https://yuedu.bmsgzw.cn/book/2621/26210013","https://yuedu.bmsgzw.cn/book/2621/26210014",
        "https://yuedu.bmsgzw.cn/book/2621/26210015","https://yuedu.bmsgzw.cn/book/2621/26210016",
        "https://yuedu.bmsgzw.cn/book/2621/26210017","https://yuedu.bmsgzw.cn/book/2621/26210018",
        "https://yuedu.bmsgzw.cn/book/2621/26210019","https://yuedu.bmsgzw.cn/book/2621/26210020",
        "https://yuedu.bmsgzw.cn/book/2621/26210021","https://yuedu.bmsgzw.cn/book/2621/26210020",
        "https://yuedu.bmsgzw.cn/book/2621/26210021","https://yuedu.bmsgzw.cn/book/2621/26210022",
        "https://yuedu.bmsgzw.cn/book/2621/26210023","https://yuedu.bmsgzw.cn/book/2621/26210024",
        "https://yuedu.bmsgzw.cn/book/2621/26210025","https://yuedu.bmsgzw.cn/book/2621/26210026",
        "https://yuedu.bmsgzw.cn/book/2621/26210027","https://yuedu.bmsgzw.cn/book/2621/26210028",
        "https://yuedu.bmsgzw.cn/book/2621/26210029","https://yuedu.bmsgzw.cn/book/2621/26210030"]
for url in urls:
    url = url
    page = requests.get(url=url, headers=headers).text
    time.sleep(5)
    # print(page)
    tree = etree.HTML(page)
    novel = tree.xpath("//*[@id='context']/div/div[2]/text()")  #("/html/body/div[3]/div/div[5]/text()")
    for text in novel:
        print(text)
        with open("摆渡人3-无境之爱.text", "a", encoding="utf-8") as fp:
            fp.write(text)  # text形式写入文件
print("爬取完成！！")
