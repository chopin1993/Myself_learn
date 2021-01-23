# coding:utf-8

class calculation:
    """
    计算多种图形面积
    可打印分割线
    """

    def sum1(*numbers, multiple=1):  # *number，是一个组装成元祖的可变参数
        """多个数字之和"""

        print("多个数字之和:", end="")
        total = 0.0
        for i in numbers:
            total += i
        return total * multiple

    def mul1(*numbers, multiple=1):
        """多个数之积"""

        print("多个数之积:", end="")
        total = 1.0
        for i in numbers:
            total *= i
        return total * multiple

    def area_triangle(self, g, multiple=2):
        """三角形面积"""

        print("三角形面积:", end="")
        total = self * g
        return total / multiple

    def area_squareness(self, k):
        """矩形面积"""

        print("矩形面积:", end="")
        total = self * k
        return total

    def area_round(r=1, pi=3.1415926):
        """圆形面积"""

        print("圆形面积:", end="")
        total = pi * r * r
        return total

    def print_line(self="****", times=10):
        """打印分割线，使用的字符及字符重复次数可自定义"""

        print(self * times)

    def c_f(self):
        """摄氏度转换为华氏度"""
        f = self * 9 / 5 + 32
        return f

    def f_c(self):
        c = (self - 32) * 5 / 9
        return c


cal = calculation
print(cal.sum1(111, 222))
cal.print_line()
print(cal.f_c(12))
# 函数式调用类中的方法\类调用


# print(calculation.sum1(122, 1212, multiple=2))
# calculation.print_line()
# print(calculation.mul1(2, 3, 4, 5, 6))
# calculation.print_line("----", 20)
# print(calculation.area_triangle(3, 5))
# calculation.print_line()
# print(calculation.area_triangle(3, 4))

# 方法调用\对象调用

# start = calculation
# print(start.sum1(90, 10, 90))
