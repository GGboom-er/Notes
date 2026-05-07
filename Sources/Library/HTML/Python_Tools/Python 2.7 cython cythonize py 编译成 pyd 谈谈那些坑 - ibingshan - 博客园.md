---
tags: [html, Python_Tools]
---

# 🌐 Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园.html](file:///Y:/GGbommer/Lib/Http/Python%202.7%20cython%20cythonize%20py%20编译成%20pyd%20谈谈那些坑%20-%20ibingshan%20-%20博客园.html)
- **文件名称**：Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园.html
- **资源类型**：html
- **归属分类**：Python & 开发环境
- **本地路径**：[[Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园

[![返回主页](./Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园_files/logo.gif)](https://www.cnblogs.com/ibingshan/)

# [ibingshan](https://www.cnblogs.com/ibingshan/)

## Tech-Artist

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/ibingshan/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/ibingshan)
* [管理](https://i.cnblogs.com/)
* [订阅](javascript:void(0))
  [![订阅](./Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园_files/xml.gif)](https://www.cnblogs.com/ibingshan/rss/)

随笔- 149 
文章- 0 
评论- 19 
阅读-
33万

# [Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑](https://www.cnblogs.com/ibingshan/p/10334471.html)

# Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑

# 前言

基于 python27 的 pyc 很容易被反编译，于是想到了pyd，加速运行，安全保护

## 必要准备

安装cython：pin install cython

下载安装：[VCForPython27.msi](https://www.microsoft.com/en-us/download/details.aspx?id=44266)

Cython document：<https://cython.readthedocs.io/en/stable/src/userguide/source_files_and_compilation.html>

假如有以下目录结构：

myPackage/

\_\_init\_\_.py

myModule.py

subFolder/

\_\_init\_\_.py

subModule.py

setup.py　　--这是用来 build python extension 的，也就是 pyd

setup.py代码：

[![复制代码](./Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园_files/copycode.gif)](javascript:void(0); "复制代码")

```
 1 import setuptools  # important
 2 from distutils.core import setup
 3 from Cython.Build import cythonize
 4 from distutils.extension import Extension
 5 extensions = []
 6 extensions.append(Extension('myModule',['myModule.py']))
 7 extensions.append(Extension('subFolder.subModule',['subFolder/subModule.py']))
 8 
 9 setup(
10     ext_modules = cythonize(extensions, compiler_directives={'language_level': 2}),
11     
12 )
```

[![复制代码](./Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑 - ibingshan - 博客园_files/copycode.gif)](javascript:void(0); "复制代码")

## 设置环节变量（用.bat）

set VS90COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools

## 在 myPackage/ 目录下开启cmd（win系统），编译pyd

python.exe setup.py build\_ext --inplace

## 给 setup.py 添加自定义参数

请参考：[Python argparse 模块](https://www.cnblogs.com/ibingshan/p/10383875.html)

额外参考：<https://stackoverflow.com/questions/677577/distutils-how-to-pass-a-user-defined-parameter-to-setup-py?noredirect=1&lq=1>

## 编译过程（如果顺利）和 setup.py 代码解析：

**cythonize()**：会在 py 文件所在的相应文件夹生成 .c 或者 .cpp 文件（这个取决于**Extension()** 的 language 参数，language = 'c' 或者 'c++'）

**setup.py build\_ext**：在myPackage/目录下生成一个build文件夹，里面有编译的一些中间产物，最终把 pyd 复制到 py 文件所在的相应位置（pyd最终复制的路径是由Extension()来决定的）

**Extension()**：它有很多参数，只说代码中的参数

**参数 1**：这个参数就是 pyd 最终被拷贝的路径，在编译成功后，会看到 copying build\lib.win-amd64-2.7\xxx.pyd -> xxx\xxx，后面的 xxx\xxx 就是Extension的第一个参数：'xxx.xxx' （没看错，这里是用点 . 来分隔，简直坑），而且路径的前缀是cmd运行路径，如果第一个参数是'\*'（就像官方文档里面的例子一样），它代表cmd运行的当前路径，也就是 myPackage/ ，也就是说，所有 pyd 都会被拷贝到这里来

**参数 2**：这是 py 或者 pyx（Cython格式）的相对路径，是指 cmd（并非setup.py） 的所在路径（因为我是在 waf 的 wscript 中 执行编译的，waf 会把 cmd 的路径改变到它的 build 路径下，如果单独使用setup.py，应该不会有这个问题）

## 编译过程中会遇到的一些警告或者错误（如果不顺利或者不完美）和 setup.py 代码解析

### error：unresolved external symbol init\_\_init\_\_

没错，**\_\_init\_\_.py** 似乎在这里不能被编译成 pyd，所以可能要编译成 pyc 或者干脆不编译

### error：unable to find vcvarsall.bat

出现这个错误，只会看到 .c 或者 .cpp，看不到 pyd

网上大多数的解决方法：<http://www.cnblogs.com/lazyboy/p/4017567.html>

下面是我另外找到的方法（链接：<https://stackoverflow.com/questions/53172601/error-unable-to-find-vcvarsall-bat-when-compiling-cython-code>）：

1.确保安装：[VCForPython27.msi](https://www.microsoft.com/en-us/download/details.aspx?id=44266)

2.确保更新或者安装 Python 的 setuptools：

安装或者更新 setuptools：pin install -U setuptools

3.在 setup.py 中的第一行加 import setuptools，最新版的 setuptools 会自动找到 vcvarsall.bat

### FutureWarning： Cython directive 'language\_level' not set, using 2 for now (Py2). This will change in a later release!

在compiler\_directives中指定：cythonize( compiler\_directives = {'language\_level': 2} )

### is not a valid module name...Cython.Compiler.Errors.CompileError:

注意文件的路径文件夹命名，不要有中文，不要是纯数字，不要有非法字符

## py 和 pyx 编译成 pyd 的注意点

如果编译的是 .pyx ，而且这些文件中 include 一些自定义的头文件，那么 setup() 还要加 library 相关的参数，就像我们编译 c 语言一样，这里只谈 py ，所以不多说

## pyd 的使用

就像 pyc 一样正常使用（如果python安装了 PySide 或者 PyQt，可以到它们的目录下看看，它们的主要模块也是 pyd，而且 \_\_init\_\_.py 没有相应的 pyd）

import xxx

from myPackage import myModule

import myPackage.myModule as m

from myPackage.subFolder import subModule

## pyd for maya

似乎用以上的流程编译出来的 pyd 不能在 maya 中 import，似乎要用编译maya的 python.exe 一致的 MSC(微软C编译器) 版本来编译，参考链接：<https://stackoverflow.com/questions/53683874/how-to-import-pyd-files-into-maya>

这里我们用的是VCForPython27（不清楚这个到底是什么），而 maya2014 的 mayapy.exe 用的是 MSC v.1600

不过 maya 确实是可以 import 的 pyd 的，因为 maya 自身就集成了 PySide 的 pyd 模块，所以，只要接下来要找出怎么编译 maya 的 pyd 方法，或许 maya PySide 是用 C++ 来直接编写，然后编译成 pyd，不过 cythonize 已经把 py 生成了 c 或者 cpp，现在还不确定问题出在哪个阶段。

如何编译 maya 的 pyd ，请参考：[Maya mayapy.exe 安装 Cython，编译 pyd](https://www.cnblogs.com/ibingshan/p/10346354.html)

## 对 Python 的严谨性要求

由于 Cython 会把 py 转为 c 或者 cpp，所以 python 上的一些随性会导致编译的错误，也就是变得

... (原文过长，已截断)