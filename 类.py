# 类和方法，包括纯函数、修改器、方法、特殊方法


class Time1:
    """
    表示一天内的时间
    属性：hour(小时)，minute(分钟)，second(秒)
    """

    def __init__(self, hour=0, minute=0, second=0):
        """初始化实例"""

        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """"""

        # 08:33:00
        print("%.2d:%2d:%.2d" % (self.hour, self.minute, self.second))

    def __add__(self, other):
        """操作符重载"""

        seconds = self.time_to_int + other.time_to_int
        return self.int_to_time(seconds)

    def time_to_int(self):
        """转换成秒数"""

        return self.hour * 60 * 60 + self.minute * 60 + self.second

    def print_time(self):
        print("%.2d:%.2d:%.2d:" % (self.hour, self.minute, self.second))


def int_to_time(self):
    """将整数秒转换成time对象"""

    time = Time1()
    minute, time.second = divmod(self, 60)
    time.hour, time.minute = divmod(minute, 60)


start = Time1(1, 2, 40)
end = Time1(1, 2, 40)
print(start + end)
