"""
题目：列表转换为字典。
"""

i = ['a', 'b']
l = [1, 2]
print(dict([i, l]))
print(dict([l, l])) # 等于 print(dict([l]))
'''
Output:
{'a': 'b', 1: 2}
{1: 2}
'''