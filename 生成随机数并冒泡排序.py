# coding:utf-8
import random
import docx
import time

list1 = []
timenow1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取时间戳

# 生产20个随机数
for i in range(0, 20, 1):
    a = random.randint(0, 100)
    list1.append(a)
# list1.append(timenow1)  # 类表尾部加时间戳

print(timenow1)
print(list1)


# 冒泡排序

def bubbleSort(list1):
    n = len(list1)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]


bubbleSort(list1)

print("排序后的数组:")
for i in range(len(list1)):
    time.sleep(1)
    print("%d" % list1[i])

# 随机数写入到word文档中
doc = docx.Document()
doc.add_paragraph(str(list1))
doc.save("随机数.doxc")
