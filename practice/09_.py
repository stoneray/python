"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
程序分析：关键是计算出每一项的值。
"""
from functools import reduce   # python 3.x 之后改的
'''
Tn = 0
Sn = []
n = int(input('n = :\n'))
a = int(input('a = :\n'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

Sn = reduce(lambda x,y : x + y,Sn)
print(Sn)
'''

# 凡是要对一个集合进行操作的，并且要有一个统计结果的，能够用循环或者递归方式解决的问题，一般情况下都可以用reduce方式实现。
# def reduce(function, sequence, initial=None): function必须是二元函数
# lambda 将函数简化为一个表达式。
list = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, list)
print(sum)
exit(0)


# 生成N位的数字
def repeat(n, num):
    assemble = 0
    for co in range(n):
        assemble += num * (10 ** co)
    return assemble

# 注意int类型，比较坑
i = int(input('输入深度：\n'))
numin = int(input('输入数字：\n'))
sum = 0
for times in range(1, int(i + 1)):
    sum += repeat(times, numin)
print(sum)