---
tags: [html, Maya_API_Dev]
---

# 🌐 Maya开发实践课（二） - Vanny Yuan's Blog.html

> **一句话总结**：Vanny Yuan 博客：实战开发

## 🔗 本地文件
- [Maya开发实践课（二） - Vanny Yuan's Blog.html](file:///Y:/GGbommer/Lib/Http/Maya开发实践课（二）%20-%20Vanny%20Yuan's%20Blog.html)
- **文件名称**：Maya开发实践课（二） - Vanny Yuan's Blog.html
- **资源类型**：html
- **归属分类**：Maya_API_Dev
- **本地路径**：[[Maya开发实践课（二） - Vanny Yuan's Blog.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya开发实践课（二） - Vanny Yuan's Blog

Maya开发实践课（二） 🍒

2020年11月2日 下午

2.5k 字

35 次

# Maya开发实践课（二）

## L15 走进 PyMEL 编程

### 什么是PyMel

[![](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L15_1.png)](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L15_1.png)

### 了解PyNode

[![](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L15_2.png)](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L15_2.png)

### pynode转化

```
node = pm.PyNode('pSphere1')

# ! 查询方法
dir(node)

# ! 查询属性
dir(node.attr())Copy
```

### 连接属性

```
import maya.cmds as cmds
import pymel.core as pm
ball = pm.PyNode('ball')
ball_tx = ball.attr('tx')

box = pm.PyNode('pCube1')
box_tx = box.attr('tx')

ball_tx >> box.txCopy
```

### 断开连接

```
ball_tx //  box_txCopy
```

### 使用API方法

```
ball = pm.PyNode('ball)
baii.__apiobject__()Copy
```

### 练习

使用PyMEl实现原来融合节点的连接。

```
import pymel.core as pm

lam_A = pm.createNode('lambert')
lam_B = pm.createNode('lambert')
lam_C = pm.createNode('lambert')
bc = pm.createNode('blendColors')

lam_A.outColor >> bc.color1
lam_B.outColor >> bc.color2
bc.output.connect(lam_C.color)Copy
```

## L16 为 Maya 安装第三方 Python 包

1. 拷贝安装
2. pip安装
3. 编译安装

### 练习

给Maya安装yaml模块和numpy模块。

**Numpy**

官方文档

<https://numpy.org/install/#python-numpy-install-guide>

简介

<https://www.runoob.com/numpy/numpy-tutorial.html>

python安装

python -m pip install numpy

maya安装

1. 下载wheel  
   <https://pypi.tuna.tsinghua.edu.cn/simple/numpy/>
2. 安装  
   mayapy -m pip install C:\Users\Administrator\Desktop\numpy-1.14.0rc1-cp27-none-win\_amd64.whl

**yaml**

python安装

python -m pip install pyyaml

maya安装

1. 下载wheel  
   <https://pypi.tuna.tsinghua.edu.cn/simple/pyyml/>
2. 安装  
   mayapy -m pip install C:\Users\Administrator\Desktop\pyyml-0.0.2-py2.py3-none-any.whl

## L17 自定义 Maya 环境变量

### 为什么自定义软件环境

1. 统一管理
2. 快速部署
3. 方便切换

  环境变量的用户变量会覆盖系统变量。

### cmd设置环境变量

```
set MAYA_DISABLE_CLIC_IPM=1Copy
```

### python设置环境变量

1. 查询

   ```
   os.environCopy
   ```
2. 设置

   ```
   _env = os.environ.copy()
   _env['XXX_ENV'] = 'hello'
   import subprocess
   subprocess.Popen("C:/Program Files/Autodesk/Maya2017/bin/maya.exe",env=_env)Copy
   ```

### 常用环境变量

[![](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L17_1.png)](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L17_1.png)

### 练习

使用Yaml编写一个环境配置文件，读取里面内容使用subprocess启动软件。

写入yaml

```
import os
import yaml

yaml_str = """
name: yaml_env
date: 20200716
version: ['maya2018','maya2019']
"""

yaml_data = yaml.load(yaml_str, Loader=yaml.SafeLoader)

with open('D:/td_tech/yaml_test/yaml_write.yaml', 'w') as f:
        yaml.dump(yaml_data, f)Copy
```

启动软件

```
import os
import yaml
import subprocess

with open('D:/td_tech/yaml_test/yaml_write.yaml', 'r+') as f:
        data = yaml.load(f, Loader=yaml.Loader)

_env = os.environ.copy()

for (key,value) in data.items():
        _env[key] = str(value)

subprocess.Popen("C:/Program Files/Autodesk/Maya2018/bin/maya.exe",env=_env)Copy
```

[![](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L17_2.png)](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L17_2.png)

## L18 Maya API 基本类型介绍

### Maya API基本结构

[![](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L18_1.png)](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L18_1.png)

### API语言支持

[![](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L18_2.png)](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L18_2.png)

1. API编译的插件后缀：

   Linux：.so

   Windows: .mll

   Mac OS X：.bundle

   通用性插件：.py
2. API内置库：

   OpenMaya 基本的操作工具类

   OpenMayaUI 界面工具类

   OpenMayaAnim 动画工具类

   OpenMayaFX 特效工具类

   OpenMayaRender 渲染工具类
3. API命名规则

M classes - 基本的数据类型

MFn - Function 函数工具类型

MIt - Iterator 迭代器类型

MPx - 代理类型，拓展Maya功能需要继承的类

### DependencyNode、 DagNode

DependencyNode：Maya最基本的节点类型

DagNode：Maya带有层级的节点类型

DagNode由DependencyNode继承而来，DagNode有层级关系继承。

### MObject

[![](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L18_3.png)](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L18_3.png)

### 查询API帮助文档 API1.0

MObject() 相当于python的**init**()，可以用于实例化对象

静态方法static Mobject：在没有实例化节点之前就能使用

析构函数~Mobject()：变量在销毁的时候执行的操作

### 通过Pymel创建Mobject

```
import maya.OpenMaya as OpenMaya
import pymel.core as pm

ball_node = pm.PyNode('pSphere1')
ball_api_node = ball_node.__apimobject__()

# 通过pymel转化的MObject已经有了对象
print ball_api_node.isNull() # True
# 通过OpenMaya直接创建的MObject是空的
print OpenMaya.MObject().isNull() # False

# 查询api类型
print ball_api_node.apiType() # 110
print ball_api_node.apiTypeStr() # kTransform
ballshape_api_node = pm.PyNode('pSphereShape1').__apimobject__()
print ballshape_api_node.apiType() # 296
print ballshape_api_node.apiTypeStr() # kMesh

# 使用 == != 判断两个物体是否相等
print ball_api_node == ballshape_api_node # False
# 使用 = 直接赋值
ballshape_api_node = ball_api_node
print ballshape_api_node.apiTypeStr()Copy
```

### DagPath

[![](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L18_4.png)](./Maya开发实践课（二） - Vanny Yuan's Blog_files/L18_4.png)

```
# 创建一个空的MDagPath
ball_dag_path = OpenMaya.MDagPath()
# 建立DagPath联系
OpenMaya.MDagPath.getAPathTo(ball_api_node,ball_dag_path)
# 获取DagPath名字
print ball_dag_path.fullPathName() # |pSphere1
print ball_da

... (原文过长，已截断)