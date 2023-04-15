"""
题目：暂停一秒输出，并格式化当前时间。
程序分析：无。
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
print(time.strftime('%Y-%m-%d %H:%M:%S'), ' | ', time.time())
print(time.strftime('%Y-%m-%d %H:%M:%S'), time.localtime(time.time()))

'''
Output:
2017-03-04 11:00:28  |  1488596428.0922644
2017-03-04 11:00:29 time.struct_time(tm_year=2017, tm_mon=3, tm_mday=4, tm_hour=11, tm_min=0, tm_sec=29, tm_wday=5, tm_yday=63, tm_isdst=0)

'''