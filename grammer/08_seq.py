# 序列：列表、元组和字符串都成为序列。分可变序列（数组）和不可变序列（元组和字符串）
# 1. 能运用到序列的运算符只有+和*，+表示序列拼接，*表示将序列进行重复，即拷贝
# 2. 同一性运算符is、is not。判断两个对象是不是同一个对象，即id是否相同
import itertools

sss = (1,2)
print(id(sss))  # 4507466184
sss *= 2
print(id(sss))  # 4507820504    元组运算后变成另一个对象

sss = [1,2]
print(id(sss))  # 4346638152
sss *= 2
print(id(sss))  # 4346638152    数组运算后还是原对象

# 3. in和not in。判断某个元素是否包含在序列中
print("a" in 'abc') # True
print("a" not in 'abc') # False

x = 123
del x   # 彻底删除一个元素，再访问他会报错
# print(x)    # NameError: name 'x' is not defined
x = [1,2,3,4,5]
del x[1:4]   # 等同于 x[1:4] = []，切片也可以完成
del x[::2]  # 不等同于 x[::2] = []，会报错，数组不能做这种操作
del x[:]    # 清空一个数组，等同于 x.clear()

# 4. 与序列相关的函数。数量相当多
# 数组、元组和字符串相互转换
print(list((1,2,3)))    # [1, 2, 3] 将可迭代对象转换成数组
print(tuple([1,2,3]))   # (1, 2, 3) 将可迭代对象转换成元组
print(str([1,2,3])) # '[1, 2, 3]' 将可迭代对象转换成字符串。比较傻，只是在原来基础上加个引号
print(min([1,2,3,4]))   # 1
print(max('ABCabc'))    # c 比较每个字符的编码值，大写字母在小写字母之前。
print(min(1,2,34,4))   # 1
print(min([], default="啥都没有"))   # 啥都没有。如果入参为空，返回default默认值
# print(len(range(2**100)))   # OverflowError: Python int too large to convert to C ssize_t   len函数有最大值，超过会报错
print(sum([1,2,3,4]))   # 10
# print(sum([1,2,3,4], start=10))   # TypeError: sum() takes no keyword arguments   从start开始加，报错了，可能是版本问题。

# 反转
s = [1,2,3,0,6]
print(sorted(s))    # [0, 1, 2, 3, 6]   这里是重新生成一个对象，原来的s数组内容不变
s.sort()
print(s)    # [0, 1, 2, 3, 6]   s.sort()是对原数组进行了更改
print(sorted(s, reverse=True))  # [6, 3, 2, 1, 0]   反转
t = ['aaa', 'bbbb', 'ccc']
print(sorted(t))    # ['aaa', 'bbbb', 'ccc']    可以对字符串进行排序，比较的是每个字符串中每个字符的编码值
print(sorted(t, key=len))   # ['aaa', 'ccc', 'bbbb']    key指定len()，会对每个字符串调用len()后再排序
print(reversed(t))  # <list_reverseiterator object at 0x1062a37f0> 返回的是一个迭代器，也是一个可迭代对象。
print(list(reversed(t)))  # ['ccc', 'bbbb', 'aaa']

# all() & any()
x = [1,1,0]
y = [1,1,9]
print(all(x))   # False all判断是否所有元素都是true
print(all(y))   # True  any只要有一个元素是true
print(any(x))   # True
print(any(y))   # True

# enumerate()
season = ['Spring','Summer','Fall','Winter']
print(list(enumerate(season)))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]    创建一个枚举对象，默认从0开始
print(list(enumerate(season, 10)))  # [(10, 'Spring'), (11, 'Summer'), (12, 'Fall'), (13, 'Winter')]    创建一个枚举对象，指定起点

# zip()
x = [1,2,3]
y = [4,5,6]
z = 'abcde'
print(list(zip(x,y)))   # [(1, 4), (2, 5), (3, 6)]
print(list(zip(x,y,z))) # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]   会把z中后面未匹配到的直接丢弃
import itertools
print(list(itertools.zip_longest(x,y,z)))   # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c'), (None, None, 'd'), (None, None, 'e')] itertools模块会保留未匹配上的值

# map()：传入一个函数，后面参数为方法的参数
print(list(map(ord, 'abcd')))   # [97, 98, 99, 100] 分别对'abcd'中的字符进行ord计算
print(list(map(pow, [2,5,10],[1,2,3]))) # [2, 25, 1000] 等同于 [pow(2,1), pow(5,2), pow(10,3)]

# filter()：传入一个函数，为过滤函数，只有通过过滤函数为true的结果才会被筛选出来
print(list(filter(str.islower, 'ABCdef')))  # ['d', 'e', 'f']

# 5. 迭代器 & 可迭代对象
# 一个迭代器肯定是一个可迭代对象，可迭代对象可重复使用，迭代器是一次性的
mapped = map(ord, 'ASDFG')  # map函数返回的是一个迭代器，一次性的
for each in mapped:
    print(each)
print(list(mapped)) # [] 因为上面使用过了，这里再使用就为空了

x = [1,2,3]
y = iter(x)
print(type(x))  # <class 'list'>    数组是个可迭代对象
print(type(y))  # <class 'list_iterator'>   inter()方法可讲可迭代对象转为迭代器
print(next(y))  # 1 next方法是专门对迭代器使用的，意思是取出下一个元素
print(next(y))  # 2
print(next(y))  # 3
# print(next(y))  # StopIteration 当迭代器没数据了，再使用next会抛异常
print(next(y, '没哟了'))   # 没哟了 指定第二个参数，可以再没数据时返回默认值
