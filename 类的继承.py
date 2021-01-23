# coding:utf-8

# 类的继承

class Person:     # 根类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        template = "person [name={0}, age={1}]"
        a = template.format(self.name, self.age)
        return a


# 继承Person

class Student(Person):      # 继承person根类的特性

    def __init__(self, name, age, school):  # 定义构造方法
        super().__init__(name, age)     # 调用父类中的实例变量和方法
        self.school = school        # 子类的的实例变量
