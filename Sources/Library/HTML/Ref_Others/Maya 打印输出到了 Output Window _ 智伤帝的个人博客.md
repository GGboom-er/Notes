---
tags: [html, Ref_Others]
---

# 🌐 Maya 打印输出到了 Output Window _ 智伤帝的个人博客.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Maya 打印输出到了 Output Window _ 智伤帝的个人博客.html](file:///Y:/GGbommer/Lib/Http/Maya%20打印输出到了%20Output%20Window%20_%20智伤帝的个人博客.html)
- **文件名称**：Maya 打印输出到了 Output Window _ 智伤帝的个人博客.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[Maya 打印输出到了 Output Window _ 智伤帝的个人博客.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya 打印输出到了 Output Window | 智伤帝的个人博客

加载中...

![avatar]()

[文章

301](/archives/)

[标签

63](/tags/)

[分类

70](/categories/)

---

[主页](/)

[时间线](/archives/)

[标签](/categories/)

[分类](/tags/)

[友情链接](/link/)

[系列总结](javascript:void(0);)

* [效率提升指南](/categories/%E6%95%88%E7%8E%87%E6%8F%90%E5%8D%87%E6%8C%87%E5%8D%97/)
* [Unreal Python](/categories/%E6%B8%B8%E6%88%8F%E5%BC%80%E5%8F%91/Unreal/Python)
* [Python 编程规范](/categories/Python/Python-%E7%BC%96%E7%A8%8B%E8%A7%84%E8%8C%83/)
* [Python Qt 开发教程](/categories/CG/Qt/Python%E7%BB%93%E5%90%88Qt%E7%B3%BB%E5%88%97%E5%BC%80%E5%8F%91%E6%95%99%E7%A8%8B/)
* [VScode 全面使用攻略](/tags/VScode/)
* [TiddlyWiki 使用指南](/categories/Wiki/TiddlyWiki-%E9%A3%9F%E7%94%A8%E6%8C%87%E5%8D%97)
* [Hexo博客搭建历程](/categories/%E5%89%8D%E7%AB%AF/hexo/)
* [Photogrammetry](/categories/Photogrammetry/)
* [Shader学习之路](/categories/%E6%B8%B8%E6%88%8F%E5%BC%80%E5%8F%91/Unity/Shader%E5%AD%A6%E4%B9%A0%E4%B9%8B%E8%B7%AF/)
* [Maya 研究记录](/categories/CG/Maya/Maya%20%E7%A0%94%E7%A9%B6%E8%AE%B0%E5%BD%95)
* [Vue学习之路](/categories/%E5%89%8D%E7%AB%AF/Vue/Vue%E5%AD%A6%E4%B9%A0%E4%B9%8B%E8%B7%AF/)
* [回忆录](/categories/%E5%9B%9E%E5%BF%86%E5%BD%95/)

[关于我](javascript:void(0);)

* [博客初心](/about/)
* [博客日志](/about/log.html)
* [wiki 文档](https://wiki.l0v0.com/)
* [Houdini Wiki](http://hou.l0v0.com)
* [更新计划](/about/todo.html)
* [教程计划](/about/plan.html)
* [关注列表](/about/focus.html)
* [我的笔记](/about/note/note.html)
* [我的作品](/about/my_work.html)
* [联系我](/about/contact.html)

目录

你已经读了0%

1. [1. 前言](#%E5%89%8D%E8%A8%80)
2. [2. 问题根源](#%E9%97%AE%E9%A2%98%E6%A0%B9%E6%BA%90)
3. [3. 原因探讨](#%E5%8E%9F%E5%9B%A0%E6%8E%A2%E8%AE%A8)
4. [4. 总结](#%E6%80%BB%E7%BB%93)

Maya 打印输出到了 Output Window

发表于2020-11-14|更新于2022-12-14|[CG](/categories/CG/)[Maya](/categories/CG/Maya/)[Maya 疑难杂症](/categories/CG/Maya/Maya-%E7%96%91%E9%9A%BE%E6%9D%82%E7%97%87/)

|字数总计:708|阅读时长:2分钟|阅读量:

## 前言

>   前段时间写代码，测试 maya 工具，总是突然之间发现信息输出到了 Output Window  
>   但是也不知道是什么原因造成的。  
>   因为使用的环境和工具很多，不知道是哪一个东西导致的，一直没有查出来。  
>   最近我很偶然地定位到问题所在的工具，于是去查了一下这个问题出在哪里。

## 问题根源

>   经过代码测试之后，我发现是某个历史脚本里面加了一行 reload(sys) 的代码导致的。  
>   只要在 Maya 环境下执行 reload(sys)  
>   那么输出就到了 Output Window 上了。

## 原因探讨

>   其实通过之前 焕唤 做 AppMananger 工具同步学到了 print 的操作是可以 override 的。  
>   print 背后调用的其实是 sys.stdout.write 的函数。  
>   如果将 sys.stdout 覆盖为一个新的 类 对象，并且同样提供 write 的方法。  
>   就可以将打印的操作变成我们自定义的操作。  
>   AppMananger 复写为了输出 log

>   同理，Maya 默认是输出到 Output Window 里的。  
>   通过查 Maya Python 库 maya.app.startup.gui 脚本里面可以找到相应的操作

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` | ``` # module: maya.app.gui # # This module is imported during the startup of Maya in GUI mode. # import sys import maya.app.startup.basic  # Run the user's userSetup.py if it exists maya.app.startup.basic.executeUserSetup()  import maya.app.baseUI import maya.utils  # Replace sys.stdin with a GUI version that will request input from the user sys.stdin = maya.app.baseUI.StandardInput()  # Replace sys.stdout and sys.stderr with versions that can output to Maya's # GUI sys.stdout = maya.utils.Output() sys.stderr = maya.utils.Output( error=1 )  maya.utils.guiLogHandler()  # ADSK_CLR_MGT_BEGIN import maya.app.colorMgt.customTransformUI import maya.app.colorMgt.inputSpaceRulesUI # ADSK_CLR_MGT_END  import maya.app.quickRig.quickRigUI # =========================================================================== # Copyright 2018 Autodesk, Inc. All rights reserved. # # Use of this software is subject to the terms of the Autodesk license # agreement provided at the time of installation or download, or which # otherwise accompanies this software in either electronic or hard copy form. # =========================================================================== ``` |

>   reload(sys) 操作会将这些覆盖的函数重新用回了 Python 的默认操作。  
>   所以才会导致 print **打印输出到了** Output Window 上。

>   另外这里 maya.utils.Output 这个类应该是从 C++ 里面创建出来的。  
>   在 utils.py 里面并没有定义，并且 utils.py 也有说明，部分的方法诸如 `executeInMainThreadWithResult` 是来自 C++ 的

## 总结

>   reload(sys) 的使用场景是想使用 sys.setdefaultencoding(‘utf-8’) 解决 Python2 蛋疼的 encoding 问题。  
>   然而实际使用情况下很复杂，这个操作并不能彻底解决问题，所以 python2 环境最好就规避中文，避免字符处理问题。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` # NOTE 修复中问报错提示问题 reload(sys) sys.setdefaultencoding("utf-8") # NOTE reload sys 会导致 Maya 无法将信息输出到脚本编辑器 sys.stdin = maya.app.baseUI.StandardInput() sys.stdout = maya.utils.Output() sys.stderr = maya.utils.Output(error=1) ``` |

文章作者: [智伤帝](mailto:undefined)

文章链接: <https://blog.l0v0.com/posts/2a2e288f.html>

版权声明: 本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。转载请注明来自 [智伤帝的个人博客](https://blog.l0v0.com)！

[ࠀMaya](/tags/%E0%A0%80Maya/)[ࠕPython](/tags/%E0%A0%95Python/)

打赏

* [![微信]()](//cdn.jsdelivr.net/gh/FXTD-odyssey/FXTD-odyssey.github.io@master/img/wechatimg.jpg)

  微信
* [![支付宝]()](//cdn.jsdelivr.net/gh/FXTD-odyssey/FXTD-odyssey.github.io@master/img/alipayimg.jpg)

  支付宝

相关推荐

[![cover]()

2022-08-16

Maya 顶点色单通道笔刷](

... (原文过长，已截断)