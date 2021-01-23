# coding:gbk
"""
V1.4,在V1.3基础上增加猜过数字的统计
"""

import random

a = 1  # 至少要猜一次

# 统计猜过的数字
list1 = []

# 0-20中生成随机数
numb = random.randint(0, 20)

# 通过键盘输入数字
guess = int(input("-->键盘输入数字0-20,来猜猜："))
list1.append(guess)

# 猜数字
print("---嗯......我来看看你猜的对不对---")

while numb != guess:
    if numb < guess:
        print("-->猜大了，再给你次机会", end="-->")
        guess = int(input("-->键盘输入数字,再来猜猜："))

        # 猜过的数字添加到列表
        list1.append(guess)

        # 记录次数
        a += 1
    elif numb > guess:
        print("-->猜小了，再给你次机会", end="-->")
        guess = int(input("-->键盘输入数字,再来猜猜："))

        # 猜过的数字添加到列表
        list1.append(guess)

        # 记录次数
        a += 1
    else:
        # 记录次数
        a += 1


print("--厉害，恭喜！猜对了,是：{0} ；   统计你猜的次数：{1} 次--".format(guess, a))
print("--你猜过的数字有：{0}--".format(list1))
