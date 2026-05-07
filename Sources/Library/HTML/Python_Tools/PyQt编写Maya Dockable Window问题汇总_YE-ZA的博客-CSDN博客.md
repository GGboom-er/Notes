---
tags: [html, Python_Tools]
---

# 🌐 PyQt编写Maya Dockable Window问题汇总_YE-ZA的博客-CSDN博客.html

> **一句话总结**：PySide/PyQt Dockable UI 汇总

## 🔗 本地文件
- [PyQt编写Maya Dockable Window问题汇总_YE-ZA的博客-CSDN博客.html](file:///Y:/GGbommer/Lib/Http/PyQt编写Maya%20Dockable%20Window问题汇总_YE-ZA的博客-CSDN博客.html)
- **文件名称**：PyQt编写Maya Dockable Window问题汇总_YE-ZA的博客-CSDN博客.html
- **资源类型**：html
- **归属分类**：Python_Tools
- **本地路径**：[[PyQt编写Maya Dockable Window问题汇总_YE-ZA的博客-CSDN博客.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

PyQt编写Maya Dockable Window问题汇总\_YE-ZA的博客-CSDN博客

# PyQt编写Maya Dockable Window问题汇总

![](https://csdnimg.cn/release/blogv2/dist/pc/img/original.png)

[YE-ZA](https://blog.csdn.net/VONGOLA10BOSS "YE-ZA")
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newCurrentTime2.png)
于 2021-09-02 21:47:40 发布
![](https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png)
600
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)
收藏

6

分类专栏：
[Maya](https://blog.csdn.net/vongola10boss/category_11331259.html)
[PyQt](https://blog.csdn.net/vongola10boss/category_11331262.html)
文章标签：
[maya](https://so.csdn.net/so/search/s.do?q=maya&t=all&o=vip&s=&l=&f=&viparticle=)
[python](https://so.csdn.net/so/search/s.do?q=python&t=all&o=vip&s=&l=&f=&viparticle=)
[pyqt](https://so.csdn.net/so/search/s.do?q=pyqt&t=all&o=vip&s=&l=&f=&viparticle=)

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/VONGOLA10BOSS/article/details/120057784>

版权

[![](https://img-blog.csdnimg.cn/20201014180756724.png?x-oss-process=image/resize,m_fixed,h_64,w_64)

Maya
同时被 2 个专栏收录![](https://csdnimg.cn/release/blogv2/dist/pc/img/newArrowDown1White.png)](https://blog.csdn.net/vongola10boss/category_11331259.html "Maya")

1 篇文章
0 订阅

订阅专栏

[![](https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64)

PyQt](https://blog.csdn.net/vongola10boss/category_11331262.html "PyQt")

1 篇文章
0 订阅

订阅专栏

最近在研究用PyQt写Maya插件的界面，遇到不少的疑难杂症，在这里汇总一下，便于日后查询。

  

# 与Maya界面融合

首先最主要的目标是想让PyQt写好的界面与Maya完美融合，不会在操作Maya界面的时候把我们自己的窗口压到后面，而网上传统的方法便是使用`OpenMayaUI`库以及`shiboken2`库中的`wrapInstance`方法，将我们的窗口parent到已经存在的Maya窗口中。

官网的Maya开发人员帮助中也给了以下代码示例：

```
from maya import OpenMayaUI as omui 

from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import *
from PySide2 import __version__
from shiboken2 import wrapInstance 

mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
mayaMainWindow= wrapInstance(long(mayaMainWindowPtr), QWidget) 

# WORKS: Widget is fine 
hello = QLabel("Hello, World", parent=mayaMainWindow) 
hello.setObjectName('MyLabel') 
hello.setWindowFlags(Qt.Window) # Make this widget a standalone window even though it is parented 
hello.show() 
hello = None # the "hello" widget is parented, so it will not be destroyed. 

# BROKEN: Widget is destroyed 
hello = QLabel("Hello, World", parent=None) 
hello.setObjectName('MyLabel') 
hello.show() 
hello = None # the "hello" widget is not parented, so it will be destroyed.
```

> 代码中对比了`parent = mayaMainWindow`和`parent = None`两种情况，后者在使用show()方法后窗口会由于Python的GC机制在创建后瞬间消失，但前者由于parent到了Maya的主窗口中，就会由Maya来维持其生命周期。另外，此时在操作Maya界面的时候，我们的窗口也会一直保持置顶不会被挡住。

  

# Dock窗口

为了让我们的窗口能够dock在Maya的UI中，网上常见的方法是结合上面的`wrapInstance`方法，再通过内置库的`cmds.workspaceControl`来实现。（*注：Maya2017之前的版本为* `cmds.dockControl`）

例如**Dhruv Govil**大神的Python For Maya: Artist Friendly Programming教程中的一个案例就是如此：

```
def getDock(name='LightingManagerDock'):
    # Delete existing window first
    deleteDock(name)
    
    ctrl = pm.workspaceControl(name,dockToMainWindow=('right',1),label="Lighting Manager")
    
    qtCtrl = omui.MQtUtil.findControl(ctrl)
    ptr = wrapInstance(long(qtCtrl),QtWidgets.QWidget)
    return ptr

def deleteDock(name='LightingManagerDock'):
    if pm.workspaceControl(name,query=True,exists=True) :
        pm.deleteUI(name)
```

> * 其中，大神这里用的是PyMel库`pm.`，也可替换成`cmds.`
> * 另外`omui.MQtUtil.findControl`方法的官方解释为：Auto-naming a widget so that it can be looked up as a string.

---

虽然以上方法可行，但根据教程还需要再额外添加多行代码才能实现dock的逻辑，比较麻烦，于是我又去调研了其他方案。

后来发现Maya提供了`maya.app.general.mayaMixin`模块，其中包含的类可以方便将基于PyQt创建的控件融合进Maya UI中，其中用于dock窗口的就是`MayaQWidgetDockableMixin`类。

官方示例：

```
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide.QtGui import QPushButton, QSizePolicy

class MyDockableButton(MayaQWidgetDockableMixin, QPushButton):
    def __init__(self, parent=None):
        super(MyDockableButton, self).__init__(parent=parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred )
        self.setText('Push Me')

# Create an instance of the button and display it.
button = MyDockableButton()
# Show the button as a non-dockable floating window.
button.show(dockable=False)
# A valid Maya control name has been automatically assigned to the button.
buttonName = button.objectName()
print('# ' + buttonName)
# MyDockableButton_368fe1d8-5bc3-4942-a1bf-597d1b5d3b83

# showRepr() can be used to display the current dockable settings.
print('# ' + button.showRepr())
# show(dockable=False, height=23, width=70, y=610, x=197, floating=True)

# Change it to a dockable floating window.
button.show(dockable=True)
print('# ' + button.showRepr())
# show(dockable=True, area='none', height=23, width=70, y=610, x=197, floating=True)
```

> * 在继承了`MayaQWidgetBaseMixin`类后，如果没有明确指定parent，则可以直接将我们的控件parent到main Maya window，无需再用`wr

... (原文过长，已截断)