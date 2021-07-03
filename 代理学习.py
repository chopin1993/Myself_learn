# coding:utf-8
import requests

url = 'https://www.baidu.com/s?wd=IP'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
page_text = requests.get(url=url, headers=headers, proxies={'http://': '175.44.108.135:9999'}).text  # 代理参数proxies
with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
