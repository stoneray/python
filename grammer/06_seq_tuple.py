# 元组：元组是不可变的数组

rhyme = (1,2,'ccc')
print(rhyme)    # (1, 2, 'ccc') 视觉上看，数组使用[]，元组使用()
rhyme = 1,3,4,'dddd'
print(rhyme)    # (1, 3, 4, 'dddd') 元组也可以去掉()，只要使用逗号分隔就是元组
# rhyme[0] = 1    # TypeError: 'tuple' object does not support item assignment    元组不支持修改，修改会报错
print(rhyme[::-1])  # ('dddd', 4, 3, 1) 元组具有数组一样的查操作
print(rhyme.count(1))   # 1 查询元组内某个元素个数
print(rhyme.index('dddd'))  # 3 查询元组内某个元素下标
s = (1,2,3)
t = (4,5,6)
print(s+t)  # (1, 2, 3, 4, 5, 6)    同数组
print(s*3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)   同数组
w = s,t
print(w)    # ((1, 2, 3), (4, 5, 6))    嵌套元组
for each in w:
    print(each) # 循环打印元组，同数组
arr = [i for i in rhyme]
print(arr)  # [1, 3, 4, 'dddd'] 列表表达式也可以使用元组，元组转数组，注意不存在元组表达式 (i for i in rhyme)
one = (520)
print(type(one))    # <class 'int'> 创建只包含一个元素的元组，错误用法。这么写生成的是个int
one = (520,)
print(type(one))    # <class 'tuple'>   创建只包含一个元素的元组，正确用法。一定要有逗号
t = (123,'abc',3.14)    # 装包
a,b,c = t   # 元组的拆包    a=123, b='abc', c=3.14
a,b,c = [123,'abc',3.14]   # 数组的拆包    a=123, b='abc', c=3.14
a,b,c = 'xyz'   # 字符串的拆包    a=, b=y', c=z
# a,b = t   # ValueError: too many values to unpack (expected 2)  不管哪种拆包，左侧元素数量一定要和右侧相等，否则会报错。
a,*b = t    # 解决办法：使用*。a=123, b=剩下的所有元素，b=['abc', 3.14]
x,y = 12, 34    # 多次赋值，底层实现就是元组的装包和拆包。即 _ = (12,34)   x,y = _

# 元组里内容一定不可以改变吗？
s=[1,2]
t=[3,4]
w=(s,t)
w[0][0]=999
print(w)    # ([999, 2], [3, 4])    如果元组里的内容是数组，数组内容是可以改的