"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

year = int(input("输入年：\n"))
month = int(input("输入月：\n"))
day = int(input("输入日：\n"))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
sum = 0
#是否正常月
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print("月份输入错误！")

# 是不是闰年
leap = 0
if year % 4 == 0:
    leap = 1
# 是否大于2月
if leap == 1 and month > 2:
    sum += day + 1
print("当前是第 %d 天" %sum)
'''
Output:
输入年：
2032
输入月：
3
输入日：
3
当前是第 63 天
'''