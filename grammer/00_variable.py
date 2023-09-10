# 变量：支持中文和英文，不允许数字开头

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