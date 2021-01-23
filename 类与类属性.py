# coding = utf-8

class Animal(object):  # 定义一个类，根类是object
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义示例变量
        self.sex = sex
        self.__weight = weight

    def set_weight(self, weight):  # 定义setter访问器，需要带变量
        self.__weight = weight

    def get_weight(self):  # 定义getter访问器，不需要带变量，但是getter必须在setter后面，顺序不能颠倒
        return self.__weight


a = Animal(2, 0, 10.0)

print("--一般输出结果--", end="\n")
print("a体重:{0:0.1f}".format(a.get_weight()))
a.set_weight(123.45)  # 调用setter访问器
print("a体重:{0:0.3f}".format(a.get_weight()))


class Animal1(object):  # 定义一个类，根类是object
    """定义动物类"""

    def __init__(self, age1, sex1=1, weight1=0.0):
        self.age1 = age1  # 定义示例变量
        self.sex1 = sex1
        self.__weight1 = weight1

    @property  # 修饰getter访问器
    def weight1(self):
        return self.__weight1

    @weight1.setter  # 修饰setter访问器
    def weight1(self, weight1):  # setter必须在后面getters，顺序不能颠倒
        self.__weight1 = weight1


a1 = Animal1(2, 0, 10.0)

print("--修饰器输出结果--")
print("a1体重:{0:0.1f}".format(a1.weight1))
a1.weight1 = 123.45         # 调用setter访问器，类似于---a.set_weight(123.45)---
print("a1体重:{0:0.3f}".format(a1.weight1))
