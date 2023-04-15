a = 'a'
b = 'b'
c = a + b # 字符串拼接

delimiter = '-'
myList = ['1', '2', '3', '4', '5']
print(delimiter.join(myList)) # 1-2-3-4-5 注意myList必须是str

str1 = input('请输入字符串1')
str2 = input('请输入字符串2')
count = str1.count(str2)   # count 为 str1 中拥有 str2 的个数

sStr1 = 'abcdefg'
sStr2 = 'cde'
print(sStr1.find(sStr2)) # 查找字符串