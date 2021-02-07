# coding:utf-8
import json
import time

import requests

if __name__ == "__main__":
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    keyword = input("请输入要查询的城市：")
    # keyword_list = ["天津"]
    # for keyword in keyword_list:#爬取多个城市
    data = {
        "cname": "",
        "pid": "",
        "keyword": keyword,
        "pageIndex": "1",
        "pageSize": "100",
    }
    response = requests.post(url=url, data=data, headers=headers).json()  # 爬取之后直接.json生成json文件
    fp = open(keyword + ".json", "w", encoding="utf-8")  # 写入文件操作
    json.dump(response, fp=fp, ensure_ascii=False)  # 将Python数据结构转换成json数据，json.loads将json转换成Python数据结构
    print(keyword+"--肯德基分店地址爬取完成！！---->时间戳：", time.asctime(time.localtime(time.time())))
