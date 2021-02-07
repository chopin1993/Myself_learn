# coding:utf-8
# 网站不回复爬虫查程序    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
import requests
from bs4 import BeautifulSoup

url = "https://www.shicimingju.com/book/sanguoyanyi.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers).text
print(page_text)
soup = BeautifulSoup(page_text, "lxml")
li_list = soup.select(".book-mulu > ul > li")
fp = open("./sanguoyanyi.text", "w", encoding="utf-8")
for li in li_list:
    title = li.a.string
    detail_url = "https://www.shicimingju.com/" + li.a["href"]
    deatil_page_text = requests.get(url=url, headers=headers).text
    detail_soup = BeautifulSoup(deatil_page_text, "lxml")
    div_tag = detail_soup.find("div", class_="chapter_content")
    connect = div_tag.text
    fp.write(title + connect + '\n')
    print(title, "爬取完成！！")
