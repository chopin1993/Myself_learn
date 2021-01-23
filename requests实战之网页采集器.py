# coding:utf-8
import requests

# UA伪装：伪装成浏览器做反爬取处理，作为requests.get中的headers参数
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
url = "https://www.sogou.com/sogou"
# 处理URL携带的参数：封装到字典中
kw = input("enter a word")
param = {
    "query": kw
}
response = requests.get(url=url, params=param, headers=headers)
page_text = response.text
file_name = kw + ".html"
with open(file_name, "w", encoding="utf-8") as fp:
    fp.write(page_text)
print(file_name, "保存成功！")
