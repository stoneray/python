Python语法

os.path.dirname(__file__)的使用：和运行时指定的py文件路径有关，显示全路径或空

Anaconda
conda、anaconda这些概念的差别
conda可以理解为一个工具，也是一个可执行命令，其核心功能是包管理与环境管理。包管理与pip的使用类似，环境管理则允许用户方便地安装不同版本的python并可以快速切换。Anaconda则是一个打包的集合，里面预装好了conda、某个版本的python、众多packages、科学计算工具等等，所以也称为Python的一种发行版。其实还有Miniconda，顾名思义，它只包含最基本的内容——python与conda，以及相关的必须依赖项，对于空间要求严格的用户，Miniconda是一种选择。


4、P图
1）把图片变小
from PIL import Image

im = Image.open("orig.jpg" )
im.thumbnail((128,128))
im.save("xiao_jpg","JPEG")

2）将计算机显示的RGB中 RB 调换
from PIL import Image

im = Image.open("orig.jpeg")
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om. save("BGR.jpg")

3）截图图片轮框
from PIL import Image
from PIL import ImageFilter
im = Image.open("orig.jpg")
om = im.filter(ImageFilter.CONTOUR)
om.save("Contour.jpg")

5、世界超算 Linpack 测试
查看文件有多少行： wc -l test.txt 
适用于科学计算，超算领域等，可以获取文件中需要的数据，并整理成 excel 文件
6、图像字符化
https://www.cnblogs.com/mrchige/p/6379911.html


1、人工智能 AI
AI：机器实现的智能，用来扩展人的智能 

2、AI发展的条件 
1）大量的数据 
2）运算能力 
3）算法 

3、AI涉及的技术 
1）深度学习 
2）机器学习 

4、编程利器 
jupyter notebook（在线编程软件） 

5、Python是最好的AI编程语言？！ 
深度学习三部曲；神经网络 -> 一堆函数 -> 最好的函数 

6、爬虫 
是获取网络数据的，机器人程序 
Baidu、Google等都在用爬虫 
Python开发效率高，周期短，适合做爬虫 
URL（资源定位）：C:/User/S/Desktop/hello.png 

7、安装、升级Python 
使用 Anaconda 安装更方便 

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar -zxvf Python-3.7.0 
cd Python-3.7.0 
./configure    安装配置文件 
make    编译 
make install    安装 
sudo easy_install requests    mac安装 requests 模块(她这个好像是给python2安短，python3还不能用) 

可以直接这么安装
brew install python3    pip3也会一起被安装
sudo pip3 install requests    安装 requests 模块
sudo pip3 install bs4    安装 BeautifulSoup 格式化库

8、做事情
(所有调用 print方法的地方，都可以省略掉 print方法)
# 爬取数据
import requests
r = requests.get(‘http://www/baidu.com') 
print(r.status_code)    打印返回码
print(type(r))    打印变量类型
print(r.text)    将返回数据以文本格式显示（乱码）
print(r.encoding)    查看编码
r.encoding=‘utf-8’    转码
r.text    打印（不乱码）

# 解析数据
from bs4 import BeautifulSoup    使用 bs4，获取html内需要的标签内容
soup = BeautifulSoup(r.text, “html.parser”)    用 html引擎，格式化 r.text，存入soup
print(soup.prettify)    格式化输出，是以html格式存储的了
a = soup.find_all(‘a’)    查找<a>标签，结果是 list
a.text    因为是数组，这么输出报错
print(len(a))    查看 list 大小
print(a)    查看 list 内容
print(soup.find_all(‘a’, {‘class’:’mnav'}))    使用字典，根据标签和属性，获取节点数据

# 存储数据
# 使用框架迭代起来，爬取、解析、存储
![store.png](../imgs/store.png)

9、实战：爬取网站数据
pip install scrapy    安装 scrapy 框架。scrapy 把作文题变成 填空题
scrapy startproject firstPC    创建项目 
scrapy genspider houses bj.lianjia.com    创建一个爬虫（houses.py） 
scrape crawl houeses    运行爬虫  
修改 houses.py，迭代爬取


11.词云(第三方)
https://amueller.github.io/word_cloud/auto_examples/index.html
一个栗子：http://blog.csdn.net/tanzuozhev/article/details/50789226

词云各个模板： http://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud
直接下载模板，执行 pip install cp36-win64.whl 


一、文本颜色设置
1.颜色定义说明 

格式：\033[显示方式;前景色;背景色m 
  
前景色 背景色 颜色 
--------------------------------------- 
30 40  黑色 
31 41  红色 
32 42  绿色 
33 43  黃色 
34 44  蓝色 
35 45  紫红色 
36 46  青蓝色 
37 47  白色 
  
显示方式 意义 
------------------------- 
0 终端默认设置 
1 高亮显示 
4 使用下划线 
5 闪烁 
7 反白显示 
8 不可见  
例子： 
\033[1;31;40m <!--1-高亮显示 31-前景色红色 40-背景色黑色--> 
\033[0m <!--采用终端默认设置，即取消颜色设置-->]]] 

2.ANSI控制码的说明 
\33[0m  关闭所有属性  
\33[1m  设置高亮度  
\33[4m  下划线  
\33[5m  闪烁  
\33[7m  反显  
\33[8m  消隐  
\33[30m -- \33[37m   设置前景色  
\33[40m -- \33[47m   设置背景色  
\33[nA   光标上移n行  
\33[nB   光标下移n行  
\33[nC   光标右移n行  
\33[nD   光标左移n行  
\33[y;xH  设置光标位置  
\33[2J   清屏  
\33[K    清除从光标到行尾的内容  
\33[s    保存光标位置  
\33[u    恢复光标位置  
\33[?25l   隐藏光标  
\33[?25h   显示光标 

class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)


课程：https://www.bilibili.com/video/BV1c4411e77t/?p=41&spm_id_from=pageDriver&vd_source=bf007f669137adabccc2477d6798283d（学习到这一节了）
