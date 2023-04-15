"""
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
"""
import datetime
from dateutil import parser # pip install Python-dateutil

if __name__ == '__main__': # 只当前文件自己能运行

    import time # 时间函数
    start = time.clock()
    # start = time.time()
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))

    # dateutil.parser 将字符串日期转化成易读的日期格式
    print(parser.parse("Aug 28 2099 12:00AM"))

    end = time.clock()
    # end = time.time()
    print('共经历： %6.3f' % (end - start))
else:
    print('禁止其他文件使用该模块！')

'''
Output:
13/03/2017
05/01/1941
06/01/1941
05/01/1942
2099-08-28 00:00:00
'''