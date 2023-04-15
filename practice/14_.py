"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""


# expected 2 blank lines!
def reducenum(n):
    print("{} = ".format(n), end='')
    if n < 0 or not isinstance(n, int):
        print('请输入正确数字！')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:
        for i in range(2, int(n + 1)):   # TypeError: 'float' object cannot be interpreted as an integer ???
            if n % i == 0:
                n /= i   # n 等于 n/index
                if n == 1:
                    print(i)
                else :
                    print('{} * '.format(i), end='')
                break

reducenum(90)
reducenum(100)
'''
Output:
90 = 2 * 3 * 3 * 5
100 = 2 * 2 * 5 * 5
'''