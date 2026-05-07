---
tags: [html, Python_Tools]
---

# 🌐 Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园.html

> **一句话总结**：mayapy 环境下 Cython 安装

## 🔗 本地文件
- [Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园.html](file:///Y:/GGbommer/Lib/Http/Maya%20mayapy.exe%20安装%20Cython，编译%20pyd%20-%20ibingshan%20-%20博客园.html)
- **文件名称**：Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园.html
- **资源类型**：html
- **归属分类**：Python_Tools
- **本地路径**：[[Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园

[![返回主页](./Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园_files/logo.gif)](https://www.cnblogs.com/ibingshan/)

# [ibingshan](https://www.cnblogs.com/ibingshan/)

## Tech-Artist

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/ibingshan/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/ibingshan)
* [管理](https://i.cnblogs.com/)
* [订阅](javascript:void(0))
  [![订阅](./Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园_files/xml.gif)](https://www.cnblogs.com/ibingshan/rss/)

随笔- 149 
文章- 0 
评论- 19 
阅读-
33万

# [Maya mayapy.exe 安装 Cython，编译 pyd](https://www.cnblogs.com/ibingshan/p/10346354.html)

# Maya mayapy.exe 安装 Cython，编译 pyd

## 前言

在 [Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑](https://www.cnblogs.com/ibingshan/p/10334471.html) 中最后提到，使用  VCForPython27 编译的 pyd，不能在 maya 中使用，这跟编译 mayapy.exe 的 msc 有很大关系，运行 mayapy.exe 就能获取 python 的版本 和 msc 的版本，至于 msc 和 VS 的版本对应，请参阅：[MSC VS 版本对应](https://www.cnblogs.com/ibingshan/p/10343037.html)

## 软件安装

maya2014 （如果想用公版的python，则在运行编译前，要设置环境变量：set VS90COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools，那么下面就不用 mayapy.exe了）

vs 2010（只要安装就行，mayapy.exe 会自动找到 msc）

## 编译和安装 Cython 到 maya2014 的 python lib 中

这里我们需要 Cython 源码，用 maya2014 的 python.exe 来运行 Cython 的 setup.py，这样会自动找到 vs2010 的 msc 来编译 Cython，这样才会和 maya 的 python.exe 的 msc 版本一致。

下载 [Cython-0.26](https://codeload.github.com/cython/cython/zip/0.26)，或者在github上下载最新的版本 <https://github.com/cython/cython>

### 编译预准备：

在编译前，我们需要在 maya 的安装路径中配置一下编译需要的 python 头文件和 python.lib，根据参考：[maya环境下，py -> pyd](http://blog.sina.com.cn/s/blog_137fc1d750102wvm6.html)，里面说的过程是对的，但是细节却有错误，根据编译中的错误提示，我是这样做的：

以下的目的都是以maya的安装目录为前缀的：

1.在 /Python 文件夹中新建一个 include 和 libs 文件夹（这两个文件夹是必须的，我是根据编译过程中的报错找到的这两个文件夹）

2.拷贝 /lib/python27.lib 到 Python/libs

3.拷贝 /include/python2.7 中所有的文件到 Python/include

### 编译

1.把下载的 cython 压缩包解压到任何路径（不建议中文路径或者一些奇葩路径）

2.管理员运行 cmd （win 系统），因为最后会拷贝编译好的 package 到 maya 的安装目录下，可能需要一些权限，尤其是如果 maya 安装在 C 盘。

3.cd 到 解压后的 cython 目录下运行 "[ maya安装目录 ]\bin\mayapy.exe" setup.py install

4.没有报错就表示成功，运行 mayapy.exe >>> import Cython 可以检测是否安装成功

## 编译 pyd

同样，我们需要用 mayapy.exe 来运行我们的 setup.py：mayapy.exe setup.py build\_ext --inplace

至于 setup.py 如何编写，请参考 [Python 2.7 cython cythonize py 编译成 pyd 谈谈那些坑](https://www.cnblogs.com/ibingshan/p/10334471.html) 中相关部分即可

## 编译后的 pyd 兼容性

用 maya2014 的 cython 编译出来的 pyd 能兼容到 maya2018，至于更高版本，可能到了使用 python3 的maya就不兼容了。

max2018 python 也兼容，可能也跟 maya 一样，python3 的 max python 就不再兼容

官方版的 python2 也是兼容的

## 注意点

### \_\_init\_\_.py 不能编译成 pyd

### 关于 .py 中的 \_\_file\_\_ 属性，虽然能编译通过，但是编译成 pyd 后，会报 "\_\_file\_\_ is not defined" 的错误，所以这个要特殊处理一下，\_\_file\_\_属性是import 一个py 模块后产生的，所以我们可以把相关的变量定义到 \_\_init\_\_.py 中

### pyd 和 pyc 混合使用

在测试中，由于我的一个模块中有 \_\_file\_\_ 属性，所以我把 pyd 重命名，拷贝一个 pyc 到相应目录下，发现一些 import 该模块的模块中的属性不完整，所以建议：pyd 不要引用 相关联的而不被编译成pyd 的 pyc，py 和 pyc 可以引用 pyd

### 转pyd的py中尽量不要用try，比如导入一个pyd，这个pyd中导入一个不存在的模块，第一次会报出importError，但是你再导入pyd的时候，那个pyd会变成一个默认空的built in模块，并不会报错，这个有点坑

未经博主允许，禁止直接转载本博客任何内容（可以在文章中添加链接，禁止原文照搬），如需直接原文转载对应文章，请在该文章中留言联系博主，谢谢！！

分类:
[编程\_Python](https://www.cnblogs.com/ibingshan/category/1328442.html), [编程\_Maya](https://www.cnblogs.com/ibingshan/category/1377546.html)

标签:
[Maya](https://www.cnblogs.com/ibingshan/tag/Maya/), [cython](https://www.cnblogs.com/ibingshan/tag/cython/), [pyd](https://www.cnblogs.com/ibingshan/tag/pyd/), [vs](https://www.cnblogs.com/ibingshan/tag/vs/), [msc](https://www.cnblogs.com/ibingshan/tag/msc/), [编译](https://www.cnblogs.com/ibingshan/tag/%E7%BC%96%E8%AF%91/)

[好文要顶](javascript:void(0);)
[关注我](javascript:void(0);)
[收藏该文](javascript:void(0);)
[![](./Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园_files/icon_weibo_24.png)](javascript:void(0); "分享至新浪微博")
[![](./Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园_files/wechat.png)](javascript:void(0); "分享至微信")

[![](./Maya mayapy.exe 安装 Cython，编译 pyd - ibingshan - 博客园_files/20190926102046.png)](https://home.cnblogs.com/u/ibingshan/)

[ibingshan](https://home.cnblogs.com/u/ibingshan/)  
[粉丝 - 14](https://home.cnblogs.com/u/ibingshan/followers/)
[关注 - 1](https://home.cnblogs.com/u/ibingshan/followees/)

[+加关注](javascript:void(0);)

0

0

[«](https://www.cnblogs.com/ibingshan/p/10343037.html)  上一篇： [MSC VS 版本对应](https://www.cnblogs.com/ibingshan/p/10343037.html "发布于 2019-01-31 17:52")
  
[»](https://www.cnblogs.com/ibingshan/p/10374101.html)  下一篇： [git branch & checkout fetch 的使用和冲突解决](https://www.cnblogs.com/ibingshan/p/10374101.html "发布于 2019-02-14 13:33")

posted @
2019-02-01 17:00 
[ibingshan](https://www.cnblogs.com/ibingshan/) 
阅读(2197) 
评论(0) 
[编辑](https://i.cnblogs.com/EditPosts.aspx?postid=10346354) 
[收藏](javascript:void(0)) 
[举报](javascript:void(0))

[刷新评论](javascript:void(0);)[刷新页面](https://www.cnblogs.com/ibingshan/p/10346354.html#)[返回顶部](https://www.cnblogs.com/ibingshan/p/10346354.html#top)

登录后才能查看或发表评论，立即 [登录](javascript:void(0);) 或者
[逛逛](https://www.cnblogs.com/) 博客园首

... (原文过长，已截断)