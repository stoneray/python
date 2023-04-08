# 1. 布尔类型
# bool值为False的情况：
# ① 定义为False的对象：None和False
# ② 值为0的数字类型：0、0.0、0j、Decimal(0)、Fraction(0,1)
# ③ 空序列或集合：''、()、{}、[]、set()、range(0)
print(bool(1))  # True
print(bool(False))  # False
print(bool('')) # False
print(bool(' '))    # True

# 布尔类型是特殊的整数类型
print(1 == True)    # True
print(0 == False)   # True
print(False + True) # 1
print(False - True) # -1
print(False * True) # 0
print(False / True) # 0.0

# 2. 布尔运算符，又称逻辑运算符。总共三个运算符：and or not
print(3 < 4  and 4 < 5) # True  只有and两边都是True时结果为True
print(3 < 4  and 4 > 5) # False  只要and两边有一个False结果即为False
print(3 < 4  or 4 < 5)  # True 只要or两边有一个True结果就是True
print(3 < 4  or 4 > 5)  # True 只要or两边有一个True结果就是True
print(3 > 4  or 4 > 5)  # False 只有or两边都是False结果才是False
print(not 520)  # False 取反
print(not 0)  # True 取反

# and 和 or 都遵循短路逻辑，即直接扔出第一个能影响结果的数
print(4 and 5)  # 5
print(4 or 5)  # 4
print('sleep' and 'learn')  # learn
print('sleep' or 520)  # sleep
print((not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9))    # 4

# 3. 运算符优先级：先执行较高优先级的运算符，再执行较低优先级的运算符。
# 优先级：or < and < not < +- < */（这里只是列举了一小部分，所有的运算符优先级记得参考表格 ）
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)    # 4