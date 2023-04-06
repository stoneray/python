# Python中的函数
# 1. type() Python中的王中王函数。
# 用法一：根据对象类型返回type对象，通常跟object.__class__返回的对象相同
# 用法二：根据提供的参数创造新的类型，造物者。

# 用法一
print(type("123"))  # <class 'str'>
print(type(123))    # <class 'int'>
print(type(12.34))  # <class 'float'>
print(float)      # <class 'float'>
print(type(12.34) is float) # True
print(type(123)("520")) # 520。等同于 int("520)
print(type("123")(520)) # 520。等同于 str(520)
print(type([])("520")) # ['5', '2', '0']
print(type(())([5,2,0])) # (5, 2, 0)
print(type({}).fromkeys("keys")) # {'k': None, 'e': None, 'y': None, 's': None}

# 定义一个最简单的类
class ObjectPython:
    pass

c = ObjectPython
print(type(c))  # <class '__main__.Object'>
print(c.__class__)  # <class '__main__.Object'>
print(type(ObjectPython)) # <class 'type'>
print(type(type))   # <class 'type'> type是Python的起点，类似Java中的Object，在Java中万事万物都是Object的子类，Python中万事万物起源都是type

# 用法二
O = type('ObjectPython',(), {}) # 参数一（类的名字）、参数二（父类）、参数三（类的属性和方法）。这里的类O等价于类ObjectPython
o = O()
print(o.__class__)  # <class '__main__.ObjectPython'>
print(O.__bases__)  # (<class 'object'>,) 查看O类的父类。Python中object是所有类的默认父类

D = type('D', (O,), {}) # 指定父类
print(D.__bases__)  # 查看父类，可以看到D的父类是：(<class '__main__.ObjectPython'>,)

E = type('E', (), dict(x=12,y=34))  # 指定类的属性
print(E.x)  # 输出 12
print(E.y)  # 输出 34

def funC(self, name = "funC"):
    print(f"hello {name}")

F = type('F', (), dict(say=funC))
f = F()
f.say() # 输出 hello funC
f.say("嘿嘿嘿") # 输出 hello 嘿嘿嘿

# 2.__init_subclass__ 3.6新增的类方法，目的是加强父类对子类的管理

class CC:
    def __init_subclass__(cls):
        print("父爱如山")
        cls.xx = 250

class DD(CC):
    xx = 520
print(DD.xx)    # 父爱如山  250。这里的250是父类里定义的，父类定义的能覆盖子类

class CC:
    def __init_subclass__(cls, val):
        print("父爱如山")
        cls.xx = val

class DD(CC, val=250):
    xx = 520
print(DD.xx)    # 父爱如山  250。这里的250是父类里定义的，父类定义的能覆盖子类。指定父类中变量使用的是val变量赋值形式。