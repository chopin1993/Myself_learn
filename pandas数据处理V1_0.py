# coding:utf-8
"""温湿度光照度传感器数据筛选与整理"""
import re
import pandas as pd


def handle_file(name):
    """
    1.读取文件；
    2.正则表达式提取值,生成列表（列表中的元素是元祖）；
    :param name:
    :return:
    """
    with open(name, mode="r", encoding="utf-8") as handle:
        file = handle.read()
        find = r".*?通道号:(\d*).*?大量程照度[(]窗磁状态[)]:(\d*).*?自然光照度:(\d*).*?温度:([\d.]*).*?湿度:([\d.]*)"
        re_back = re.findall(find, file)
        return re_back


def re_back_to_excel(back):
    """
    将正则表达式提取的值写入Excel；
    :param back:
    :return:
    """
    book = pd.DataFrame(back, columns=["通道号", "大量程照度", "自然光照度", "温度", "湿度"])
    book_back = book.to_excel("数据处理.xlsx", sheet_name="原始数据")
    return book_back


def book_handle(book_back):
    """
    1.筛选通道数据，工作表中的指定行（通道号）；
    2.将各个通道数据添加到各自的表格中；
    :param book_back:
    :return:
    """
    col = pd.read_excel(book_back, sheet_name="原始数据")
    find_5 = col.iloc[0:10000:5]  # 通道05数据
    find_6 = col.iloc[1:10000:5]  # 通道06数据
    find_7 = col.iloc[2:10000:5]  # 通道07数据
    find_8 = col.iloc[3:10000:5]  # 通道08数据
    find_9 = col.iloc[4:10000:5]  # 通道09数据
    with pd.ExcelWriter('数据处理.xlsx') as work_book:  # 增加配置合适的行高列宽20200106
        """将各个通道数据添加到各自的表格中"""
        col.to_excel(work_book, sheet_name="原始数据备份.xlsx", index=False, header=True)
        find_5.to_excel(work_book, sheet_name='通道05', index=False, header=True)
        find_6.to_excel(work_book, sheet_name='通道06', index=False, header=True)
        find_7.to_excel(work_book, sheet_name='通道07', index=False, header=True)
        find_8.to_excel(work_book, sheet_name='通道08', index=False, header=True)
        find_9.to_excel(work_book, sheet_name='通道09', index=False, header=True)
    return work_book


if __name__ == "__main__":
    re_back_to_excel(handle_file("20201215照度日志.log"))
    book_handle("数据处理.xlsx")
