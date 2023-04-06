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