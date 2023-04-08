# 数字类型

# 1. 整数：Python 中整数精度不受限制。
print(232323323123 / 2322435475745645)  # 0.0001000343499525686

# 2. 浮点数
print(0.1 + 0.2)    # 0.30000000000000004

i = 0
while(i < 1):
    i += 0.1
    print(i)    # 会发现很多浮点数都有精度问题，而非刚好是个浮点数

print(0.3 == 0.1 + 0.2) # False

# 如何精确使用浮点数。使用 decimal 模块即可
import decimal
a = decimal.Decimal('0.1')
b= decimal.Decimal('0.2')
c= decimal.Decimal('0.3')
print(c == a + b)   # True
print(0.00005)  # 5e-05。Python中默认使用科学计数法表示

# 3. 复数：实部+虚部。实部和虚部都是浮点数保存的
cnumber = 1+2j
print(cnumber) # (1+2j)
print(cnumber.real) # 1.0。获取实部，是个浮点数
print(cnumber.imag) # 2.0。获取虚部，是个浮点数

# 4. 运算符
print(1 + 2)    # 数据运算
print("1" + "2")    # 字符串拼接
# print(1 + "2")  # unsupported operand type(s) for +: 'int' and 'str'
print("每天爱你三遍\n" * 3)   # 利用乘法循环打印
print(3 // 2)   # 1。地板除：取比目标小的最大整数
print(-3 // 2)  # -2。地板除：取比目标小的最大整数
print(3 % 2)    # 1。取余数
print(divmod(3, 2)) # (1, 1)    divmod：同时取出两个数的地板除和余数。蕴含的数学公式：X == (x // y) * y + (x % y)
print(divmod(-3, 2))    # (-2, 1)   (地板除, 余数)
x = -520
print(-x)   # 520    表示x的相反数
print(+x)   # -520    表示x本身
print(abs(x))   # 502   表示取x的绝对值
print(abs(cnumber))   # 2.23606797749979   复数没有绝对值，但是有模，这里返回的是复数的模
print(int('520'))   # 520   int表示将值转换成整型
print(int(3.14))   # 3   int不会四舍五入，是直接截掉浮点数的小数部分
print(int(9.99))   # 9   int不会四舍五入，是直接截掉浮点数的小数部分
print(float('9.99'))   # 9.99   float与int类似，转换成浮点数
print(float(520))   # 520.0   520.0 和 520 值虽然相等，但底层存储不同
print(float('+1E6'))   # 1000000.0 科学技术法也支持
print(complex('1+2j'))   # (1+2j) complex转换成复数
# print(complex('1 + 2j'))   # ValueError: complex() arg is a malformed string  complex中的字符串不能加空格，否则会报错
print(pow(2,3)) # 8 pow(x,y) 计算x的y次方，等价于 x ** y
print(pow(2,3,5)) # 3 pow(x,y) 与 x ** y 区别在于 pow支持第三个参数，意思是对第三个参数取余。pow(x,y,z) 等价于 x ** y % z

