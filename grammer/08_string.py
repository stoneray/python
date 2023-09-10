# 字符串

# 1. 字符串基本用法
print('I love Python')  # 使用单引号
print("I love Python")  # 使用双引号
print("Let's Go")   # 如果字符串内已经有单引号，就使用双引号
print('"life is short"')    # 如果字符串内已经有双引号，就使用单引号
print("\'life is short, let\'s go\'")    # 如果既有单引号，又有双引号，使用转移字符 \。其实统一全部使用\也可以
print("D:\one\two\three")    # 如何显示转义字符
print("D:\\one\\two\\three")    # 如何显示转义字符，解决
print(r"D:\one\two\three")    # 如果字符串特别长，或者是变量，想要去掉\，在字符串前添加r表示打印原始字符串
print("......\
      ------\n\
      ------") # \放在最后面表示还没结束，可以换行继续输入，如果末尾不添加\，换行相当于直接执行了
print("""
今天
明天
后天
""")    # 三引号字符串，又叫长字符串，代替上面的末尾\换行功能。一般用于程序开头的说明文档

# 判断一个字符串是否回文
s = '12321'
print("是回文数" if s == s[::-1] else "不是回文数")  # 是回文数
s = '123210'
print("是回文数" if s == s[::-1] else "不是回文数")  # 不是回文数

# 2. 字符串大小写字母换来换去
ss = 'ii love uu'
print(ss.capitalize())  # Ii love uu    首字母变大写，其他字母变小写。主要返回的并不是原字符串，只是按照这个规则生成一个字符串，因为字符串是不可变的。
print(ss.casefold())  # ii love uu  返回一个所有字母都是小写的字符串
print(ss.title())  # Ii Love Uu 将字符串中每个单词首字母变成大写，该单词 其他字母变小写
print(ss.swapcase())  # II LOVE UU  将字符串中所有字母反转，大写变小写，小写变大写
print(ss.upper())  # II LOVE UU 将所有字母变大写
print(ss.lower())  # ii love uu 将所有字母变小写。跟casefold区别是，lower只能改变英文字母，casefold还能将其他语言如德语大写变小写。

# 3. 字符串的左中右对齐
sss = '12345'
print(sss.center(4))    # 当width=4小于字符串长度时，直接展示，不变化
print(sss.center(10))   # 当width=4小于字符串长度时，会填充字符串，并将原字符串进行对齐。center 为居中对齐
print(sss.ljust(10))   # 当width=4小于字符串长度时，会填充字符串，并将原字符串进行对齐。ljust 为左对齐
print(sss.rjust(10))   # 当width=4小于字符串长度时，会填充字符串，并将原字符串进行对齐。rjust 为右对齐
print(sss.rjust(10, '-'))   # -----12345。当width=4小于字符串长度时，会填充字符串，并将原字符串进行对齐。rjust 为右对齐。filterchar='-' 表示用-填充，默认不填是用空格填充
print(sss.zfill(10))   # 0000012345。当width=4小于字符串长度时，会填充字符串，并将原字符串进行对齐。zfill 为在左侧用0填充，可用于计数场景
sss = '-12345'
print(sss.zfill(10))   # -0000012345。当width=4小于字符串长度时，会填充字符串，并将原字符串进行对齐。zfill 为在左侧用0填充，可用于计数场景，负数会自动移动-位置。

# 4. 查找
# count(sub [,start [,end]])    查找子字符串sub出现的次数。[start,end]表示指定下标索引范围。
# find(sub [,start [,end]])     查找子字符串sub出现的下标。从左往右，返回第一个下标
# rfind(sub [,start [,end]])    查找子字符串sub出现的下标。从右往左，返回倒数第一个下标
# index(sub [,start [,end]])    查找子字符串sub出现的下标。从左往右，返回第一个下标。和find区别在于，index找不到会报错，find找不到返回-1
# rindex(sub [,start [,end]])   查找子字符串sub出现的下标。从右往左，返回倒数第一个下标

# 5. 替换
# expandtabs([tabsize=8])   将字符串中tab替换成空格。字符串中推荐大家多用空格，少用tab，这种习惯的人较多。
# replace(old, new .count=-1)   将字符串中old段替换成new段，count指定替换的个数，默认count=-1即替换全部。
# translate(table)  按照替换规则替换，table是替换规则的表格

# 6. 字符串判断，返回的都是True/False
# startswith(prefix[, start [,end]])    # 子字符串prefix是否出现在字符串的起始位置
# endswith(suffix [,start [,end]])  # 子字符串suffix是否出现在字符串的结尾位置
# isupper()
# islower()
# istitle()
# isalpha() # 是否全为字母。空格就不是字母。
# isascii()
# isspace()
# isprintable() # 是否均是可打印的字符。转义字符如\n就不能打印。
# isdecimal()   # 判断是否数字。范围尺度最小，2²=False、I II III=False、一二三=False
# isdigit() # 判断是否数字。2²=True、I II III=False、一二三=False
# isnumeric()   # 判断是否数字。范围尺度最大，2²=True、I II III=True、一二三=True、繁体数字=True
# isalnum() # 判断是否数字。isdecimal | isdigit | isnumeric | isalpha。集大成者，前四个方法任何一个返回True，isalnum即返回True
# isidentifier()    是否是一个合法的标志符，这里说的是否是合法变量名。"520AAa"=False、"qq qq"=False
import keyword
print(keyword.iskeyword("if"))   # True。判断是否Python中的保留标识符，即是否if、while、for这些
print(keyword.iskeyword("py"))  # False

# 7. 截取字符串
# strip(chars=None) 字符串去掉左右留白，chars='www.' 去除www.字符串，默认是去除空格。
# lstrip(chars=None)    字符串去掉左侧留白
# rstrip(chars=None)    字符串去掉右侧留白
# removeprefix(prefix)  删除指定prefix的前缀
# removesuffix(suffix)  删除指定suffix的后缀

# 8. 拆分和拼接
# partition(seq)    将字符串按指定的seq分割，并返回一个三元组，三元组就是三个元素的元组。默认从左往右找，找到第一个即切割完成
# rpartition(seq)   从右往左切割
# split(seq=None, maxsplit=-1)  根据切割符seq将字符串切割成多个段落，并不是三元组了
# rsplit(seq=None, maxsplit=-1)  从右往左切割
print(".".join(["www","baidu","com"]))  # www.baidu.com. 字符串拼接，join(可迭代对象)  当数据量大时，join拼接效率远远大于+

# 9.格式化字符串
print("今天是 {} 年".format(2023))  # 今天是 2023 年    使用{}做占位符，format负责填充
print("{}看到{}".format("我","你")) # 我看到你  多个占位符替换
print("{1}看到{0}".format("我","你"))   # 你看到我  控制占位符替换使用的顺序
print("我叫{name},我{0}岁".format(18, name="tt"))   # 我叫tt,我18岁 {name}指定关键词替换，{0}指定下标替换
print("{:010}".format(520)) # 0000000520    字符串填充和对齐，格式：[[fill]align][sign][#][0][width][grouping_option][.precision][type]
print("{:+} {:-}".format(520, -502))    # +520 -502
print("{:.2f}".format(3.1415))  # 3.14
print("{:b}".format(80))    # 1010000   指定不同type，b表示二进制，x表示16进制
print("{:#b}".format(80))   # 0b1010000 #表示添加前缀区分不同进制，更人性

# 10.f字符串。Python3.6添加的简洁用法，是format的语法糖，进一步提升了Python性能。效果等同于format，Python理念在于简单，如果版本<Python3.6一定要注意不能用，许多开源软件用的是format，因为他们不知道部署的什么版本
year=2023
print(f"今年是{year}年")    # 今年是2023年
fill="+"
align="^"
width=10
prec=3
ty="g"
print(f"{3.1415:{fill}{align}{width}.{prec}{ty}}")  # +++3.14+++    冒号左边是值，冒号右边是格式