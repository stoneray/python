"""
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
"""

if __name__ == '__main__':
    import string
    from sys import stdout

    str1 = input('请输入字符串1')
str2 = input('请输入字符串2')
count = str1.count(str2)   # count 为 str1 中拥有 str2 的个数

# 读取文件内容
fp = open('a.txt')
a = fp.read()
a = a.upper()   # 小写字母 -> 大写字母
print(a)   # 输出到换行
fp.close()

fp = open('b.txt')
b = fp.read()
stdout.write(b) # 标准输出，不带换行
fp.close()

# 想文件写内容
filename = input('input a file name:\n')
fp = open(filename, 'w')
l = list(a + b)     # list() 将 ('a','b','c') -> ['a','b','c'], 原组 -> 列表
l.sort()   # list.sort()   将列表中数据排序
s = '-' # 如果s = ‘-’
s = s.join(l)   # join()的效果会变成，a-b-c
fp.write(s)
fp.close()
'''
 0-1-1-1-1-2-2-2-3-3-3-3-3-4-5-5-5-5-5-6-6-6-6-6
 '''
"""
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
"""

if __name__ == '__main__':
    import string
    from sys import stdout

    str1 = input('请输入字符串1')
str2 = input('请输入字符串2')
count = str1.count(str2)   # count 为 str1 中拥有 str2 的个数

# 读取文件内容
fp = open('a.txt')
a = fp.read()
a = a.upper()   # 小写字母 -> 大写字母
print(a)   # 输出到换行
fp.close()

fp = open('b.txt')
b = fp.read()
stdout.write(b) # 标准输出，不带换行
fp.close()

# 想文件写内容
filename = input('input a file name:\n')
fp = open(filename, 'w')
l = list(a + b)     # list() 将 ('a','b','c') -> ['a','b','c'], 原组 -> 列表
l.sort()   # list.sort()   将列表中数据排序
s = '-' # 如果s = ‘-’
s = s.join(l)   # join()的效果会变成，a-b-c
fp.write(s)
fp.close()
'''
 0-1-1-1-1-2-2-2-3-3-3-3-3-4-5-5-5-5-5-6-6-6-6-6
 '''