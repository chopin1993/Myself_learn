# coding:utf-8
# 函数传参+函数的嵌套调用，20201209-21:28

from 可变参数 import print_line
# def print_line(char, times):
#     """打印分割线，使用的字符及字符重复次数可自定义"""
#
#     print(char * times)


def print_5_lines(char="+", times=1, fre=1):
    """
    打印多行分割线。
    行数通过fre形参传递行数
    :param char 使用的字符
    :param times 一行中，每个字符打印的次数
    :param fre 打印行数
    """

    row = 0
    while row < fre:
        print_line(char, times)
        row += 1


print_5_lines()     # 使用函数默认参数运行
print_5_lines("#", 20, 3)      # 使用实参传递，自定义打印的字符，长度，行数
