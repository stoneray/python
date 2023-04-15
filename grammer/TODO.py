Python标识符
标识符用于给程序中变量、类、方法等命名的符号。有字母、数字、下划线组成。 但不能以数字开头。 区分大小写。
（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
（__foo）代表类的私有成员；
（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。


Python保留字符
这些保留字不能用作常数或变数，或任何其他标识符名称。关键字只包含小写字母。
﻿﻿


行和缩进
Python的代码块不使用大括号（{}）来控制类，函数以及其他逻辑判断。严格用缩进来写模块。


多行语句
Python语句中一般以新行作为为语句的结束符。
使用斜杠（ \）：
﻿﻿
使用 [], {} 或 () 括号：
﻿﻿

Python中括号的意义
（）     代表元祖数据类型
[    ]     代表list
{     }     代表dic

Python 引号
Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串。 三引号可以由多行组成。 
﻿﻿


Python注释
﻿﻿



Python空行
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。 
记住：空行也是程序代码的一部分。 


同一行显示多条语句
﻿﻿
