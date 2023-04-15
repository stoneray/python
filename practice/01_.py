"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

#!/usr/bin/python
#coding=utf-8
for i in range(3):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):
                print(i,j,k)
'''
Output:
0 1 2
0 1 3
0 1 4
0 2 1
0 2 3
0 2 4
0 3 1
0 3 2
0 3 4
0 4 1
0 4 2
0 4 3
1 2 3
1 2 4
1 3 2
1 3 4
1 4 2
1 4 3
2 1 3
2 1 4
2 3 1
2 3 4
2 4 1
2 4 3
'''