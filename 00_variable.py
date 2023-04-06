# 变量、字符串和运算符

# 1.变量：支持中文和英文，不允许数字开头
x = 123
y = 321
loveyou123 = 456
# 520u = 520    # 不允许数字开头
中文名 = 789   # Python3之后允许使用中文

print(x)
print(y)
print(loveyou123)
print(中文名)

x, y = y,x  # 优雅的交换x和y的值
print(x)
print(y)

# 2. 字符串
print('I love Python')  # 使用单引号
print("I love Python")  # 使用双引号
print("Let's Go")   # 如果字符串内已经有单引号，就使用双引号
print('"life is short"')    # 如果字符串内已经有双引号，就使用单引号
print("\'life is short, let\'s go\'")    # 如果既有单引号，又有双引号，使用转移字符 \。其实统一全部使用\也可以
print("D:\one\two\three")    # 如何显示转义字符
print("D:\\one\\two\\three")    # 如何显示转义字符，解决
print(r"D:\one\two\three")    # 如果字符串特别长，或者是变量，想要去掉\，在字符串前添加r表示打印原始字符串
print("......\
      ------\n\
      ------") # \放在最后面表示还没结束，可以换行继续输入，如果末尾不添加\，换行相当于直接执行了
print("""
今天
明天
后天
""")    # 三引号字符串，又叫长字符串，代替上面的末尾\换行功能。一般用于程序开头的说明文档

# 3. 运算
print(1 + 2)    # 数据运算
print("1" + "2")    # 字符串拼接
# print(1 + "2")  # unsupported operand type(s) for +: 'int' and 'str'
print("每天爱你三遍\n" * 3)   # 利用乘法循环打印
