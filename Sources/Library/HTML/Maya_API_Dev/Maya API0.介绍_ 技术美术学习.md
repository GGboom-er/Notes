---
tags: [html, Maya_API_Dev]
---

# 🌐 Maya API（0.介绍）_ 技术美术学习.html

> **一句话总结**：TechArtLearning：API 总体介绍

## 🔗 本地文件
- [Maya API（0.介绍）_ 技术美术学习.html](file:///Y:/GGbommer/Lib/Http/Maya%20API（0.介绍）_%20技术美术学习.html)
- **文件名称**：Maya API（0.介绍）_ 技术美术学习.html
- **资源类型**：html
- **归属分类**：Maya_API_Dev
- **本地路径**：[[Maya API（0.介绍）_ 技术美术学习.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya API（0.介绍）| 技术美术学习

[![](./Maya API（0.介绍）_ 技术美术学习_files/avatar.png)](https://github.com/leixingyu)

## Xingyu Lei

### 技术美工

美国加利福尼亚州

切换导航

### 

#### 特色工具（**免费**）

[不明确的](https://www.xingyulei.com/post/maya-api-intro/undefined)

分叉自

不明确的

不明确的

不明确的

[不明确的](https://www.xingyulei.com/post/maya-api-intro/undefined)

分叉自

不明确的

不明确的

不明确的

[不明确的](https://www.xingyulei.com/post/maya-api-intro/undefined)

分叉自

不明确的

不明确的

不明确的

[不明确的](https://www.xingyulei.com/post/maya-api-intro/undefined)

分叉自

不明确的

不明确的

不明确的

### 类别

* [3d 数学](https://www.xingyulei.com/categories/3d-math/)4
* [图形编程](https://www.xingyulei.com/categories/graphics-programming/)1
* [学习日志](https://www.xingyulei.com/categories/learning-log/)7
* [玛雅通讯](https://www.xingyulei.com/categories/maya-communication/)2
* [玛雅蟒蛇API](https://www.xingyulei.com/categories/maya-python-api/) 4
* [技术摘要](https://www.xingyulei.com/categories/tech-summary/)15
* [虚幻电影](https://www.xingyulei.com/categories/unreal-cinematic/)5

### 标签云

[批](https://www.xingyulei.com/tags/batch/) [C＃](https://www.xingyulei.com/tags/c/) [C++](https://www.xingyulei.com/tags/c/) [命令端口](https://www.xingyulei.com/tags/command-port/) [一般的](https://www.xingyulei.com/tags/general/) [数学](https://www.xingyulei.com/tags/math/) [玛雅人](https://www.xingyulei.com/tags/maya/) [管道](https://www.xingyulei.com/tags/pipeline/) [pyqt](https://www.xingyulei.com/tags/pyqt/) [Python](https://www.xingyulei.com/tags/python/) [渲染](https://www.xingyulei.com/tags/rendering/) [服务器](https://www.xingyulei.com/tags/server/) [插座](https://www.xingyulei.com/tags/socket/) [风格](https://www.xingyulei.com/tags/style/) [模板](https://www.xingyulei.com/tags/template/) [穿线](https://www.xingyulei.com/tags/threading/) [统一](https://www.xingyulei.com/tags/unity/) [虚幻](https://www.xingyulei.com/tags/unreal/) [视窗](https://www.xingyulei.com/tags/windows/)

# Maya API (0.介绍)

[2019-08-18](https://www.xingyulei.com/post/maya-api-intro/)

[虚拟蟒蛇火](https://www.xingyulei.com/categories/maya-python-api/)

[虚拟](https://www.xingyulei.com/tags/maya/),[蟒蛇](https://www.xingyulei.com/tags/python/)

### 概述

与 Maya 命令不同，Maya API 提供对 Maya 功能的更多低级别访问。您可以将 Maya 分为多个层：

1. 底层：系统操作系统
2. Maya Core：用 C++ 编写的整个 Maya 程序
3. Maya API：指定API暴露给开发者，可以访问Maya Core
4. Maya 命令：调用多个 Maya API 的辅助函数
5. Maya GUI：用户图形界面

而 Maya Command (MEL/Python) 最常用于编写脚本，因为它具有快速原型制作和易于学习的特点。缺点是它通常很慢并且不能提供对 Maya Core 的低级别访问。

另一方面，Maya API 很复杂，但提供更快的速度和最大的灵活性。它带有 Python 和 C++。Python API 有 1.0 和 2.0 版本。

[Python API 与 C++ API 之间的区别](http://help.autodesk.com/view/MAYAUL/2018/ENU/?guid=__files_Maya_Python_API_Differences_between_the_C_Maya_API_and_Maya_Python_API_htm)

### API1.0 与 2.0

API 1.0（2012 年之前）可以更快地访问 C++ API 2.0 中提供的更多功能，并且更加 Pythonic，但不支持某些类，例如 OpenMayaFX、OpenMayaDeformerNode。

### 一般格式

|  |  |
| --- | --- |
|  | """ |
|  | Maya Python API 1.0 |
|  | """ |
|  |  |
|  | import sys |
|  | import maya.OpenMayaMPx as mpx |
|  | import maya.OpenMaya as om |
|  |  |
|  | pluginName = 'pyTemplate' |
|  | sampleShortFlagName = '-s' |
|  | sampleLongFlagName = '-sample' |
|  |  |
|  | class PyTemplate(mpx.MPxCommand): |
|  | def \_\_init\_\_(self): |
|  | mpx.MPxCommand.\_\_init\_\_(self) |
|  |  |
|  | def doIt(self, args): |
|  | print 'doIt' |
|  | self.parseArgument(args) |
|  | self.redoIt() |
|  |  |
|  | def redoIt(self): |
|  | # this is optional |
|  | print 'redoIt' |
|  |  |
|  | def undoIt(self): |
|  | # this is also optional |
|  | print 'undoIt' |
|  |  |
|  | def parseArgument(self, args): |
|  | argData = om.MArgParser(self.syntax(), args) |
|  |  |
|  | if argData.isFlagSet(sampleShortFlag): |
|  | self.sample = argData.flagArgumentDouble(sampleShortFlag, 0) |
|  | print self.sample |
|  |  |
|  | def isUndoable(self): |
|  | # this is required when undo and redo is available |
|  | return True |
|  |  |
|  | def cmdCreator(): |
|  | return mpx.asMPxPtr(PyParticle()) |
|  |  |
|  | def syntaxCreator(): |
|  | # use this only when custom argument is defined |
|  | syntax = om.MSyntax() |
|  | syntax.addFlag(sampleShortName, sampleLongName, om.MSyntax.kDouble) |
|  | return syntax |
|  |  |
|  | def initializePlugin(mobject): |
|  | mplugin = mpx.MFnPlugin(mobject) |
|  | try: |
|  | mplugin.registerCommand(pluginName, cmdCreator, syntaxCreator) |
|  | except: |
|  | sys.stderr.write('fail to register: ' + pluginName) |
|  | raise |
|  |  |
|  | def uninitializePlugin(mobject): |
|  | mplugin = mpx.MFnPlugin(mobject) |
|  | try: |
|  | mplugin.deregisterCommand(pluginName) |
|  | except: |
|  | sys.stderr.write('fail to de-register: ' + pluginName) |
|  | raise |

[view raw](https://gist.github.com/leixingyu/358f5a9c86278a43852148c87253e3d9/raw/75ace533b9593a3d370239e58aa0d1de3fed1cf3/apiIntro1.py)
[apiIntro1.py](https://gist.github.com/leixingyu/358f5a9c86278a43852148c87253e3d9#file-apiintro1-py)
hosted with ❤ by [GitHub](https://github.com/)

|  |  |
| --- | --- |
|  | """ |
|  | Maya Python API 2.0 |
|  | """ |
|  |  |
|  | import sys |
|  | import maya.OpenMaya as 

... (原文过长，已截断)