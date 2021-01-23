# coding:utf-8

import docx

doc = docx.Document()
doc.add_paragraph("此处必须是字符串，即类型为str()")
doc.save("test.doxc")
