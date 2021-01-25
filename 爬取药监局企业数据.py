# coding:utf-8
import requests
import json
import time
if __name__ == "__main__":
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    data = {
        "on": "true",
        "page": "2",
        "pageSize": "15",
        "productName": "",
        "conditionType": "1",
        "applyname": "",
        "applysn": ""
    }
    id_list = []
    all_date_list = []
    json_ids = requests.post(url=url, data=data, headers=headers).json()
    for dic in json_ids["list"]:
        id_list.append(dic["ID"])
    # print(id_list)
    post_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        # print(id)
        data = {
            "id": id
        }
        detail_company = requests.post(url=post_url, headers=headers, data=data).json()
        # print(datil_company)
        all_date_list.append(detail_company)

    fp = open("all_company_detail.json","w",encoding="utf-8")
    json.dump(all_date_list,fp=fp,ensure_ascii=False)
    print("爬取药监局数据完成！--->爬取时间",time.asctime(time.localtime(time.time())))