# 列表和元组
# 1. 列表的定义
print([1,2,4,6])    # [1, 2, 4, 6] 创建列表使用[]，匿名列表
print([1,2,4,6,'',False,3.4])    # [1, 2, 4, 6, '', False, 3.4] 列表可以存储不同类型的数据
arr = [1, 2, 4, 6, '', False, 3.4]  # 字符串是序列，列表也是序列，可以使用foreach挨个打印每个元素
for each in arr:
    print(each)
print(arr[len(arr) - 1])  # 3.4。使用下标打印某个元素。等同于 print(rthme[-1])
# 列表切片，输出数组区间。开始
print(arr[0:3]) # [1, 2, 4]           指定起始位置
print(arr[:5]) # [1, 2, 4, 6, '']     仅指定结束位置，初始位置从0开始
print(arr[6:]) # [3.4]                仅指定初始位置，结束位置到末尾
print(arr[:]) # [1, 2, 4, 6, '', False, 3.4]       打印整个列表
print(arr[0:6:2]) # [1, 4, '']          初始位置：结束位置：间隔。每隔2个数取出一个元素
print(arr[::2]) # [1, 4, '', 3.4]
print(arr[::-2]) # [3.4, '', 4, 1]      间隔为负数，表示倒序取元素
print(arr[::-1]) # [3.4, False, '', 6, 4, 2, 1]     倒序整个列表。完美的东西都是极致简单的。
# 列表切片，结束

# 2. 列表基本操作：CRUD
nums = [0]

# 2.1 添加元素
print(nums.append(1))   # 在列表nums末尾增加一个元素，append一次只能增加一个元素
print(nums) # [0, 1]
print(nums.extend([3,4,5]))   # 在列表nums末尾增加一个列表，extend方法的参数必须是一个可迭代对象，新的内容追加到原列表最后一个元素后面。
print(nums) # [0, 1, 3, 4, 5]
nums[len(nums):] = [7,8,9]  # 切片在Python中至关重要，无切片不Python。效果相当于extend
print(nums) # [0, 1, 3, 4, 5, 7, 8, 9]
nums.insert(5,6)    # insert在指定位置添加元素
print(nums) # [0, 1, 3, 4, 5, 6, 7, 8, 9]
nums.insert(len(nums),10)   # 在末尾添加元素，相当于append
print(nums) # [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]

# 2.2 删除元素
nums.remove(1)  # 删除指定元素，注意这里不是下标为1的元素，是值=1的元素，即1本身。如果有两个1，只会删除第一个1
print(nums) # [0, 3, 4, 5, 6, 7, 8, 9, 10]
# nums.remove(111)    # ValueError: list.remove(x): x not in list 删除不存在的元素会直接报错
nums.pop(1) # 删除下标=1的元素，即3
print(nums) # [0, 4, 5, 6, 7, 8, 9, 10]
nums.clear()    # 清空整个列表
print(nums) # []

# 2.3 修改
letters = ['A', 'B', 'C', 'E']
letters[2] = '3'    # 替换指定下标的元素
print(letters)  # ['A', 'B', '3', 'E']
letters[2:] = ['4', '5', '6']   # 使用切片替换一段区间内元素，闭区间。
print(letters)  # ['A', 'B', '4', '5', '6']

nums = [2,4,8,3,9,3]
nums.sort() # 正序排序列表
print(nums)  # [2, 3, 3, 4, 8, 9]
nums.reverse()  # 倒序排序列表。等同于 nums.sort(reverse=True)
print(nums)  # [9, 8, 4, 3, 3, 2]
letters.reverse()   # 如果列表内是字符串，反转列表
print(letters)  # ['6', '5', '4', 'B', 'A']

# 2.4 查
print(nums.count(3))  # 2   查询列表nums内有几个元素3。如果列表太大时count方法效率会很低
print(letters.index('B'))  # 3   查看列表中指定元素的下标值
nums[nums.index(3)] = 2
print(nums)  # [9, 8, 4, 2, 3, 2]   如果一个元素值存在多个，只会返回第一个下标
# print(letters.index('B', 0, 2))  # ValueError: 'B' is not in list   index方法可以指定在一个区间内查找目标值，如果查不到会报错。

nums_copy1 = nums.copy()    # 使用copy方法复制整个列表。属于shallow copy 即浅拷贝
nums_copy2 = nums[:]    # 使用切片复制整个列表，效果等同于copy方法。属于shallow copy 即浅拷贝
print(nums_copy1)  # [9, 8, 4, 2, 3, 2]
print(nums_copy2)  # [9, 8, 4, 2, 3, 2]

# 3. 列表的高级操作
# 3.1 列表的拼接
a = [1,2]
b = [3,4]
print(a + b)    # [1, 2, 3, 4]
print(a * 3)    # [1, 2, 1, 2, 1, 2]    将列表a中元素重复3次
# 3.2 嵌套列表
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 嵌套列表是矩阵，多用于计算及图形学、机器计算等领域

# 遍历嵌套列表，矩阵输格式出
# 1 2 3
# 4 5 6
# 7 8 9
for i in matrix:
    for each in i:
        print(each, end = ' ')
    print()

print(matrix[0])    # [1, 2, 3] 一次下标取出一维数组。0表示第一行。
print(matrix[0][0]) # 1     二次下标取出单个元素。00表示第一行第一列。

# 注意：通过*拷贝嵌套列表的坑
A = [0] * 3 # [0, 0, 0]
for i in range(3):
    A[i] = [0] * 3
print(A)    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 通过*构造嵌套数组，正确

B = [[0] * 3] * 3   # [[]] * 3 是对[]地址进行了三次copy，而不是真正创建了三个数组
print(B)    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 通过*构造嵌套数组，错误

A[1][1] = 1
B[1][1] = 1
print(A)    # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(B)    # [[0, 1, 0], [0, 1, 0], [0, 1, 0]] # 发现全部元素都改变了，因为B方式创建的数组三行是同一个元素，指向了同一个内存地址，下面就是证明。

print(A[0] is A[1]) # False
print(B[0] is B[1]) # True

# 3.3 浅拷贝和深拷贝
x = [1,2,3]
y = x
x[1] = 1
print(x)    # [1, 1, 3]
print(y)    # [1, 1, 3] x和y指向的是同一个内存区域

y = x[:]
x[0] = 0
print(x)    # [0, 1, 3]
print(y)    # [1, 1, 3] 浅拷贝会生成一个新对象

x = [[1,2,3],[4,5,6],[7,8,9]]
y = x.copy()
x[1][1] = 999
print(x)    # [[1, 2, 3], [4, 999, 6], [7, 8, 9]]
print(y)    # [[1, 2, 3], [4, 999, 6], [7, 8, 9]] 浅拷贝只会拷贝外层对象，嵌套对象只会拷贝其引用，解决办法就是深拷贝

import copy
y = copy.copy(x)    # 使用copy模块实现浅拷贝
y = copy.deepcopy(x)    # 使用copy模块实现深拷贝，深拷贝后修改x的值，y不会跟着改变了。但是效率比浅拷贝低。

# 什么是方法？什么是函数？可以先理解成一个东西的不同叫法。

# 3.4 列表推导式（高级东西）
# 语法一：[expression for target in iterable]    列表推导式一定是个列表，所以使用[]。一定有一个for循环，左侧expression决定最终输出的列表内容。
nums = [1, 2, 6, 3 ,4, 5]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums) # [2, 4, 12, 6, 8, 10]  使用for循环将数组中每个元素扩大2倍

nums = [each + 1 for each in nums]
print(nums) # [3, 5, 13, 7, 9, 11]  使用列表推导式将数组中每个元素+1。列表推导式比for循环效率高一倍，因为列表推导式底层被解释成C语言执行。两者区别是：for直接对数组进行修改，列表表达式最终会再生成一个新数组。
print([i+1 for i in range(10)]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([[0] * 3 for i in range(3)])  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 使用列表推导式创建二维数组

# 语法二：[expression for target in iterable if condition]
print([each + 1 for each in range(10) if each % 2 == 0])    # [1, 3, 5, 7, 9] 执行顺序：for - if - expression。

# 语法三：列表推导式的嵌套 [expression for target in iterable1 for target in iterabl2 ... for target in iterableN]
print([y for i in matrix for y in i])   # [1, 2, 3, 4, 5, 6, 7, 8, 9]   将二维数组展开成一维
print([x + y for x in 'aaa' for y in 'bbb'])    # ['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']

_ = []  # _表示一个无关紧要的变量，用完就扔。
for x in 'aaa':
    for y in 'bbb':
        _.append(x+y)
print(_)    # ['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']    双层循环和上面效果一样

# 语法四：终极形态。[expression for target in iterable1 if condition1 for target in iterable2 if condition2 ... for target in iterableN if conditionN]
# KISS原则：列表推导式可以无限复杂，但过于复杂不便于后续维护，使用中把握好程度。
