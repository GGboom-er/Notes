---
tags: [html, Python_Tools]
---

# 🌐 [指南] 如何在 Windows 64 位 Maya 中安装 numpy+scipy？ - 欧特克社区 - 玛雅.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [[指南] 如何在 Windows 64 位 Maya 中安装 numpy+scipy？ - 欧特克社区 - 玛雅.html](file:///Y:/GGbommer/Lib/Http/[指南] 如何在 Windows 64 位 Maya 中安装 numpy+scipy？ - 欧特克社区 - 玛雅.html)
- **文件名称**：[指南] 如何在 Windows 64 位 Maya 中安装 numpy+scipy？ - 欧特克社区 - 玛雅.html
- **资源类型**：html
- **归属分类**：Python & 开发环境
- **本地路径**：[[[指南] 如何在 Windows 64 位 Maya 中安装 numpy+scipy？ - 欧特克社区 - 玛雅.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

[GUIDE] How to install numpy+scipy in Maya Windows 64 bit? - Autodesk Community

* [Maya Community](https://forums.autodesk.com/t5/maya/ct-p/area-c2)
* >
* [Maya Programming forum](https://forums.autodesk.com/t5/maya-programming/bd-p/area-b50)
* >
* [GUIDE] How to install numpy+scipy in Maya Windows 64 bit?

Maya

Community

* [Forums](https://forums.autodesk.com/t5/maya/ct-p/area-c2)

Maya Programming

Welcome to Autodesk’s Maya Forums. Share your knowledge, ask questions, and explore popular Maya SDK topics.

All communityThis categoryThis boardKnowledge baseUsersProducts

cancel

[Turn on suggestions](https://forums.autodesk.com/t5/forums/v5/forumtopicpage.enableautocomplete:enableautocomplete?t:ac=board-id/area-b50/thread-id/4031&t:cp=action/contributions/searchactions&ticket=iYln13dPcHBF_-1)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

![](https://forums.autodesk.com/html/@E3EF46B230710BF938EDB3C46A0BE159/assets/machine-translation-info-icon.png)
This page has been translated for your convenience with an automatic translation service. This is not an official translation and may contain errors and inaccurate translations. Autodesk does not warrant, either expressly or implied, the accuracy, reliability or completeness of the information translated by the machine translation service and will not be liable for damages or losses caused by the trust placed in the translation service.
Translate

Lang1 
 Lang2 

中文 (CHINESE SIMPLIFIED)
ENGLISH
FRANÇAIS (FRENCH)
DEUTSCH (GERMAN)
日本語 (JAPANESE)
PORTUGUÊS (PORTUGUESE)
POLSKI (POLISH)
РУССКИЙ (RUSSIAN)
ESPAÑOL (SPANISH)
TÜRKÇE (TURKISH)
ITALIANO (ITALIAN)
한국어 (KOREAN)

## [GUIDE] How to install numpy+scipy in Maya Windows 64 bit?

14 REPLIES 14

[Back to Maya Category](https://forums.autodesk.com/t5/maya/ct-p/area-c2)

[Back to forum](https://forums.autodesk.com/t5/maya-programming/bd-p/area-b50)

[Reply](/t5/forums/replypage/board-id/area-b50/message-id/4031)

[Topic Options](# "Show option menu")

* [Subscribe to RSS Feed](/autodesk/rss/message?board.id=area-b50&message.id=4031)
* Mark Topic as New
* Mark Topic as Read
* Float this Topic for Current User
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/forums/forumtopicprintpage/board-id/area-b50/message-id/4031/print-single-message/false/page/1)

* [Back to forum](/t5/maya-programming/bd-p/area-b50/page/14 "Maya Programming")
* [Previous](/t5/maya-programming/write-directly-to-maya-color-and-depth-buffer/td-p/11317333 "Write directly to Maya color and depth buffer?")
* [Next](/t5/maya-programming/importing-gs-curves-in-python-directory-can-t-find-module/td-p/11311902 "importing GS Curves in python, directory can't find module?")

Message [1](/t5/maya-programming/guide-how-to-install-numpy-scipy-in-maya-windows-64-bit/m-p/5796722#M4031) of 15

![skuzee](https://images.profile.autodesk.com/default/user_X176.png "skuzee")

![Participant](/html/@4AF0D5778CA8F669245BE7852AAAD971/rank_icons/5.png "Participant")
[skuzee](https://forums.autodesk.com/t5/user/viewprofilepage/user-id/3243401)

24921 Views, 14 Replies

‎08-31-2015
03:34 PM

* Mark as New
* Bookmark
* Subscribe
* Mute
* [Subscribe to RSS Feed](https://forums.autodesk.com/rss/message?board.id=area-b50&message.id=4031)
* [Permalink](/t5/maya-programming/guide-how-to-install-numpy-scipy-in-maya-windows-64-bit/m-p/5796722/highlight/true#M4031)
* [Print](/t5/forums/forumtopicprintpage/board-id/area-b50/message-id/4031/print-single-message/true/page/1)
* [Report](/t5/notifications/notifymoderatorpage/message-uid/5796722)

‎08-31-2015
03:34 PM

## [GUIDE] How to install numpy+scipy in Maya Windows 64 bit?

I've seen a lot of queries about getting scipy working in Maya (Windows 64 bit) with a few not 100% reproducible answers.

So after a long personal struggle with the problem, here's my solution which will hopefully end the madness for all Windows Maya users:

**TL;DR version**

[Click here to grab Maya 2014-2015-2016 tested versions of numpy ,scipy, numexpr and other useful pac...](https://drive.google.com/folderview?id=0BwsYd1k8t0lEfjJqV21yTnd2elVhNXEyTXhHclhxbDhvWVF5WWZUeVFISWViaFh1TzhrNTQ&usp=sharing)

unzip them somewhere relevant to PYTHONPATH. Congratulations! You can now use scipy in all it's glory!

**Long version**

What you need is a fully functional Python interpreter compiled with MSVC2010. [The steps for how to do that can be found here](http://p-nand-q.com/python/building-python-27-with-vs2010.html). Fortunately, the author not only explains the steps for how and why doing this is a good idea, but also provides pre-built binaries which is really nice of him. So go ahead and [download the 2.7.10 64bit build](http://p-nand-q.com/python/2015.07.12-Python2710-x64.7z) and unzip it somewhere (I put mine here: "C:\Python27"). You can then use PIP to install a properly packaged Python wheels which should play nice with mayapy.

[Pyth

... (原文过长，已截断)