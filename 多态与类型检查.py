# coding:utf-8

# 几何图形
class Fig:
    def draw(self):  # 父类方法
        print("Fig draw...")


# 椭圆形
class Ell(Fig):
    def draw(self):  # 重写父类方法
        print("Ell draw...")


# 三角形
class Tri(Fig):
    def draw(self):  # 重写父类方法
        print("Tri draw...")


print("--继承的调用--")
f1 = Fig()
f1.draw()  # Fig draw...

f2 = Ell()
f2.draw()  # Ell draw...

f3 = Tri()
f3.draw()  # Tri draw...

print("--类型检查--")
print(isinstance(f1, Tri))  # False
print(isinstance(f2, Tri))  # False
print(isinstance(f3, Tri))  # True
print(isinstance(f2, Fig))  # True
print("--检查子类——")
print(issubclass(Fig, Ell))  # False
print(issubclass(Ell, Fig))  # True
print(issubclass(Tri, Fig))  # True
print(issubclass(Ell, Tri))  # False
print(issubclass(Tri, Ell))  # False
