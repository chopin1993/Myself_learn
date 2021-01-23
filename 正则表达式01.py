# coding:utf-8

import re
file = open("20201215照度日志.log", mode='r', encoding="utf-8")
data = file.read()
# print(back)

find = r"通道号:05.*人体红外:有人"
read_back = re.findall(find, data)
print("匹配到的所有内容：{0}".format(read_back))
print("查看单个内容：{0}".format(read_back[0]))
print("匹配到的数量：{0}".format(len(read_back)))

file.close()
