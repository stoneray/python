"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
"""


def score(scores):
    if scores < 0 or scores > 100:
        print('分数错误！')
        exit(0)
    if scores >= 90:
        print('A')
    elif scores >= 60:
        print('B')
    else:
        print('C')

score(int(input('输入分数：')))
'''
Output:
输入分数：111
分数错误！
'''