#!/usr/bin/python
# -*- coding=UTF-8 -*-

testList = [] # 空链表
testList = [10086, '中国移动', [1, 2, 3, 4], 0]
testList.append('aaa')
testList.append('bbbbbbbbbb')
for i in range(0, len(testList), 2):   # [0, 4)   间隔 2
    testList.append(i)
    print(testList[i])