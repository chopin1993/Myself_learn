# coding:utf-8

import re
import xlsxwriter


def log2re(name):
    """
    文本文件筛选后生成表格，v1.1版本，筛选单个参数，多个参数（枚举）
                    ,v1.2版本，筛选参数在不同帧中，温度、湿度、NTC温度在不同的帧里面

    1.打开文件
    2.匹配文本
    3.建立工作簿、工作表
    4.设置字体格式（表头、内容）
    5.循环写入
    :param name:
    :return:
    """
    with open(name, mode="r", encoding="utf-8") as handle:
        "打开文件"
        log = handle.read()

        "匹配文本"
        # find = r".*?通道号:(\d*).*?大量程照度[(]窗磁状态[)]:(\d*).*?自然光照度:(\d*).*?温度:([\d.]*).*?湿度:([\d.]*)"  # 多个参数
        # find = r"湿度:([\d.]*)" # 单个参数
        """查找-温度-数据"""
        find_temp = r"CD 78 05 00.*?[(]查询[)]传感器数据：.*?1:.*?类型:温度  数据:([\d.]*)"
        back_temp = re.findall(find_temp, log)
        print(back_temp)
        print(len(back_temp))

        """查找-湿度-数据"""
        find_hum = r"CD 78 05 00.*?[(]查询[)]传感器数据：.*?1:.*?类型:湿度  数据:([\d.]*)"
        back_hum = re.findall(find_hum, log)
        print(back_hum)
        print(len(back_hum))

        """查找-NTC-数据"""
        find_ntc = r"CD 78 05 00.*?[(]查询[)]传感器数据：.*?1:.*?类型:外接[(]传感器[)]温度  数据:([\d.]*)"
        back_ntc = re.findall(find_ntc, log)
        print(back_ntc)
        print(len(back_ntc))

        """创建工作表、工作簿"""
        wb = xlsxwriter.Workbook("原始数据.xlsx")
        wb_temp = wb.add_worksheet("温度")
        wb_hum = wb.add_worksheet("湿度")
        wb_ntc = wb.add_worksheet("NTC")

        """设置字段格式"""
        header = {
            'bold': False,  # 粗体
            'font_name': '微软雅黑',
            'font_size': 10,
            'border': True,  # 边框线
            'align': 'center',  # 水平居中
            'valign': 'vcenter',  # 垂直居中
            'bg_color': '#66DD11'  # 背景颜色
        }

        text = {
            'font_name': '微软雅黑',
            'font_size': 9,
            'border': True,
            'align': 'lift',  # 左对齐
            'valign': 'vcenter'
        }

        header_pm = wb.add_format(header)
        text_pm = wb.add_format(text)
        # wb.set_column('C:C', 15)  # C列宽度
        # wb.set_column('A:A', 15)
        # wb.set_column('B:B', 15)
        # wb.set_column('D:D', 15)
        # wb.set_column('E:E', 15)

        # "写入表头"
        # ws.write(0, 0, "湿度", header_pm)
        # ws.write(0, 1, "大量程照度", header_pm)
        # ws.write(0, 2, "自然光照度", header_pm)
        # ws.write(0, 3, "温度", header_pm)
        # ws.write(0, 4, "湿度", header_pm)

        "温度-循环写到表格中-单个参数"
        row = 0
        col = 0
        for t in back_temp:
            if row == -1:
                wb_temp.write(row + 1, col, t, header_pm)
                row += 1
            else:
                wb_temp.write(row + 1, col, t, text_pm)
                row += 1

        "湿度-循环写到表格中-单个参数"
        row = 0
        col = 0
        for h in back_hum:
            if row == -1:
                wb_hum.write(row + 1, col, h, header_pm)
                row += 1
            else:
                wb_hum.write(row + 1, col, h, text_pm)

        "NTC-循环写到表格中-单个参数"
        row = 0
        col = 0
        for h in back_hum:
            if row == -1:
                wb_ntc.write(row + 1, col, h, header_pm)
                row += 1
            else:
                wb_ntc.write(row + 1, col, h, text_pm)

    wb.close()


if __name__ == "__main__":
    log2re("一致性测试1222.log")
