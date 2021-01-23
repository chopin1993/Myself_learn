# coding:utf-8

# import show_info as a

def show_info(sep=":", **info):
    """关键字参数试验"""

    print("----show_Somebody_info----")
    for key, value in info.items():
        print("{0}: {1}: {2}".format(sep, key, value))


# show_info("->", 姓名="大爸爸", 年龄=27, 性别="男", 生日=1993216, 体重=60, 身高=183)


class Acount:
    """定义一个银行账户类"""

    interest_rate = 0.068

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount


account = Acount("Tom", 11_000.0)


# print("---账户信息---")
# print("账户名称：{0}".format(account.owner))
# print("账户余额：{0}".format(account.amount))
# print("利率：{0}".format(Acount.interest_rate))


class Animal(object):
    """定义动物类"""

    def __init__(self, name, age=2, gender=1, weight=1):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def age(self):
        self.age += 1
        print("age...")

    def weight(self):
        self.weight += 0.5
        print("weight")

    def eat(self):
        self.weight += 0.1
        print("动物吃...")


animal = Animal("猫", 5, 1, 20)
a = Animal("狗", 7, 1, 22)
a.eat()


# print(animal)
# print("名称：{0}".format(animal.name), end="->>")
# print("年龄：{0}".format(animal.age), end="->>")
# print("性别：{0}".format("雄性" if animal.gender == 1 else "雌性"), end="->打印结束<-")
# print("体重{0}".format(a1.weight))


# 重写方法

class Dog(Animal):

    def eat(self):
        self.weight += 0.1
        print("dog eat...")


a1 = Dog(2, 0, 10)
a1.eat()


class Pig(Animal):

    def eat(self):
        self.weight += 2
        print("pig weight...")


p1 = Pig(3, 1, 12)
p1.eat()
