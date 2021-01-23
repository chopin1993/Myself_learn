
import xlsxwriter
import re


def log2re(name):
    """
    文本文件筛选后生成表格，V1.01版本,一次筛选出多个通道

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
        find = r".*?通道号:(\d*).*?大量程照度[(]窗磁状态[)]:(\d*).*?自然光照度:(\d*).*?温度:([\d.]*).*?湿度:([\d.]*)"
        # find = r"湿度:([\d.]*)"
        back = re.findall(find, log)
        print(back)

    wb = xlsxwriter.Workbook("数据筛选.xlsx")
    ws = wb.add_worksheet("原始数据")

    # 字段格式
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
    ws.set_column('C:C', 15)  # C列宽度
    ws.set_column('A:A', 15)
    ws.set_column('B:B', 15)
    ws.set_column('D:D', 15)
    ws.set_column('E:E', 15)

    "写入表头"
    ws.write(0, 0, "湿度", header_pm)
    # ws.write(0, 1, "大量程照度", header_pm)
    # ws.write(0, 2, "自然光照度", header_pm)
    # ws.write(0, 3, "温度", header_pm)
    # ws.write(0, 4, "湿度", header_pm)

    "循环写到表格中-单个参数"
    row = 0
    col = 0
    for numb in back:
        if row == -1:
            ws.write(row+1, col, numb, header_pm)
            row += 1
        else:
            ws.write(row+1, col, numb, text_pm)
            row += 1

    # "循环写到表格中-多个参数"
    # for row, row_data in enumerate(back): # 使用枚举
    #     for col, col_data in enumerate(row_data):
    #         if row == -1:
    #             ws.write(row+1, col, col_data, header_pm)
    #         else:
    #             ws.write(row+1, col, col_data, text_pm)

    wb.close()


if __name__ == "__main__":
    log2re("20201215照度日志.log")
