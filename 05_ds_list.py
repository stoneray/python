# 1. 列表
print([1,2,4,6])    # [1, 2, 4, 6] 创建列表使用[]，匿名列表
print([1,2,4,6,'',False,3.4])    # [1, 2, 4, 6, '', False, 3.4] 列表可以存储不同类型的数据
arr = [1, 2, 4, 6, '', False, 3.4]  # 字符串是序列，列表也是序列，可以使用foreach挨个打印每个元素
for each in arr:
    print(each)
print(arr[len(arr) - 1])  # 3.4。使用下标打印某个元素。等同于 print(rthme[-1])
