# 分支和循环

# 1. 分支判断：可以让程序根据条件做一件事

# 单条件判断
if 3<5:
    print("im in")
    print("im in too")
print("im out")

print("------------------------")

# 双条件判断
if "aaa" == "aab":
    print("相等")
else:
    print("不相等")

# 多条件判断：if-elif效率比if-if高，因为if-if会多次比较，而if-elif匹配中结果后即结束流程
score = 60
if 0 <= score < 60:
    print("0")
if 60 <= score < 70:
    print("60")
if 70 <= score:
    print("70")

if 0 <= score < 60:
    print("0")
elif 60 <= score < 70:
    print("60")
elif 70 <= score:
    print("70")
else:
    print("不合法")

# 炫酷用法：[条件成立时执行的语句] if condition else  [条件不成立时执行的语句]。单条件判断和多条件判断都可使用。
print("0") if 0 <= score < 60 else print("不合法")

text = "0" if 0 <= score < 60 else "不合法"
print(text)

# 2. 循环：可以让程序根据条件不断做一件事
# while 循环
# 语法结构 while condition: statements else statements
num = 10;
while num > 0:
    if(num % 2 == 0):
        num -= 1
        continue    # 继续当前循环
    print("3 > 0")
    num -= 1
    if(num < 3):
        break   # 直接结束当前循环
else:   # Python的while可以配合else，可以检测到while循环的退出状况，这里的退出和break不同，break是进入循环后的退出，这里是没进入循环的退出
    print("while循环退出了")

# for循环
# 语法结构  for 变量 in 可迭代对象：statements
for each in "Fish":
    print(each)
for i in range(1, 20, 2):
    print(i)