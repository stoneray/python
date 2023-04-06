一、安装
1. 卸载旧版本
   一般为了防止环境污染，需要卸载掉系统里已经存在的老版本。但对于Python也可不卸载，指定版本号使用不同版本的命令。
   切换不同版本命令：命令行输入python+Tab，自动补全系统中存在的不同版本python。截图中有python3、python3.7和python3.7m三个版本。
![./imgs/PythonTab.png][]

2. 下载
（1）使用安装包。选择对应系统的版本，推荐永远使用最新版本（不会有兼容问题吗？）
   Python官网：https://www.python.org/downloads/
   Python文档下载地址：www.python.org/doc/
   ![PythonDownload.png]

（2）使用源码压缩包。源码下载完需要自己解压和编译安装。wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz

3. 安装
（1）Unix-like系统安装
   tar -xf Python-3.5.2.tar.xz
   yum install -y openssl-devel zlib-devel        # 注意安装两个依赖包
   ./configure --prefix=/opt/Python     # 指定安装目录（这个有点意思）
   make
   make install
   ln -s /opt/Python/bin/python3 /usr/bin/python3     # 软链，这样就可不配置环境变量直接使用

【Mac系统】最近的Macs系统都自带有Python环境 。注意：Mac和Linux下可能同时存在Python3.0 和 Python2.0，因此对应的命令是 pip3。 

（2）Windows系统安装
点击下载包，下一步，下一步... 
注意：安装的时候，要选择 pip（用来安装第三方模板） 和 add python.exex to Path.命令行下运行 pip 检测是否已安装 

（3）安装pip：为Python3安装pip3 
① 安装setuptools 
wget --no-check-certificate  https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26
tar -zxvf setuptools-19.6.tar.gz
cd setuptools-19.6.tar.gz
python3 setup.py build
python3 setup.py install
② 安装pip3
wget --no-check-certificate  https://pypi.python.org/packages/source/p/pip/pip-8.0.2.tar.gz#md5=3a73c4188f8dbad6a1e6f6d44d117eeb
tar -zxvf pip-8.0.2.tar.gz
cd pip-8.0.2
python3 setup.py build
python3 setup.py install

自定义一些选项修改Modules/Setup

4. 环境配置
（1）Unix-like系统
在 csh shell: 输入 setenv PATH "$PATH:/usr/local/bin/python" 
在 bash shell (Linux): 输入 export PATH="$PATH:/usr/local/bin/python"  
在 sh 或 ksh shell: 输入 PATH="$PATH:/usr/local/bin/python"  

注意: /usr/local/bin/python 是Python的安装目录。 

（2）Windows系统环境配置
在命令提示框中(cmd) : 输入 path=%path%;C:\Python  
在 "计算机"- "属性" -"高级系统设置"- "系统变量" - "Path" ：输入 D:\Python32 
注意: C:\Python 是Python的安装目录。Python 3.6.0 可选择自动添加到Path。 

（3）几个重要的环境变量
PYTHONPATH：PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。 
PYTHONSTARTUP：Python启动后，先寻找PYTHONSTARTUP环境变量，然后执行此文件中变量指定的执行代码。 
PYTHONCASEOK：加入PYTHONCASEOK的环境变量, 就会使python导入模块的时候不区分大小写. 
PYTHONHOME：另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或PYTHONPATH目录中，使得两个模块库更容易切换。 

5. 验证安装配置成功
python -V 正确显示python版本号（与安装的版本号一致）即表示安装成功！

二、Python 使用
注意：如果使用有问题，如明明装了ssl，import ssl 却提示不存在该module，那说明是使用的 python 版本不对。

1. 运行
（1）交互式编程客户端。命令行输入 C:\>python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print ("hello python！")

（2）脚本式编程。
① 使用命令+脚本文件
$ python test.py
【注】test.py文件内容：print ("Hello, Python!")

② 直接执行脚本文件，要求脚本文件可被执行。
$ chmod +x test.py     # 脚本文件添加可执行权限
$ ./test.py
【注】 test.py文件内容如下
#!/usr/bin/python
#编码在Python3.X之后默认使用utf-8了
# -*- coding: UTF-8 -*- #设置形式1
#coding=utf-8   #设置形式 2
print("你好, Python!")

2. 命令行常用参数
$python -h

3. 常用 IDE
① PyCharm 下载地址 : https://www.jetbrains.com/pycharm/download/
② Sublinme Text
③ Eclipse+Pydev
注意：设置好编辑器的编码为utf-8。Undo 和 Redo 

4. 安装第三方库（pip/pip3）
第三方库都会在Python官方的pypi.python.org网站注册。
pip install Pillow # 处理图片
pip install numpy # 科学计算的Numpy库
pip install Jinja2 # 生成文本的模板工具

5. Python 解释器
默认情况下，python的解释器会搜索 sys.path 路径。 
>>> import sys
>>> sys.path    # 查看路径地址

修改path路径两种方法： 
① 直接修改path路径。运行时修改，运行结束后失效。 
>>> import sys
>>> sys.path.append('/User/myPythonPath')

② 设置环境变量
该环境变量会自动被添加到模块搜索路径中。
PYTHONPATH
