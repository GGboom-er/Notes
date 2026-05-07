---
tags: [html, Maya_API_Dev]
---

# 🌐 Maya API Programming _ Chad Vernon.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Maya API Programming _ Chad Vernon.html](file:///Y:/GGbommer/Lib/Http/Maya%20API%20Programming%20_%20Chad%20Vernon.html)
- **文件名称**：Maya API Programming _ Chad Vernon.html
- **资源类型**：html
- **归属分类**：Maya API 开发
- **本地路径**：[[Maya API Programming _ Chad Vernon.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya API Programming | Chad Vernon

# Maya API Programming

Check out my Introduction to the Maya API video series at [CGCircuit](http://www.cgcircuit.com/course/introduction-to-the-maya-api?affid=ef44e69526a3d370b2fdcd141b5e0e2710ed9c1ed68109c0d58e39a516ec0cb16af1166111d27e654aca6abdfecc0a850cc048bbf30827c68fc655f3f465b707):

## Introduction

This workshop is geared towards individuals wanting to learn how to extend and customize Maya with the Maya API. Individuals should have existing C++ and/or Python experience as well as an intermediate to advanced level of knowledge of Maya. A good understanding of Object Oriented Programming (OOP) is extremely helpful as the Maya API makes heavy use of OOP. You will not learn everything about the Maya API from this workshop. The purpose of this workshop is not to make you expert Maya programmers, but to give you a solid foundation from which to further your Maya API studies.

The techniques and code included in this workflow may not be perfect or accepted by elite Maya API programmers as the best way to utilize the API. The code and knowledge presented here is based off of my experience in creating dozens of nodes, deformers, and tool sets using the Maya API in both C++ and Python in the production of animated and effects heavy feature films a large studios. If you think something is incorrect, let me know.  Maya API learning resources are limited so hopefully these notes will help you add to your tool set.

### What is the Maya API?

The Maya API is a C++/Python API that lets programmers and scripters access the internal libraries of Maya. With the Maya API, programmers can customize Maya with new technology and create tools to help integrate the software into a studios production pipeline. Tasks written with the Maya API execute several times faster than the same tasks written in MEL.

### What Can Be Implemented with the Maya API?

The Maya API is traditionally used to make plug-ins, which are dynamic libraries loaded by Maya at runtime. Plug-ins contain implementations of many different types of objects you want to add to Maya. When I refer to “objects” here, I am referring to objects in the Object Oriented Programming sense. The Maya API provides several base classes that programmers will inherit from and fill in the desired implementations. Some possible object types are:

* Rendering viewports.
* Texture baking engines.
* Commands
* Constraints
* Deformers
* Particle and fluid emitters
* Shaders
* IK solvers
* Dependency nodes
* OpenGL locators
* File exporters
* Tools

Starting with Maya 8.5, the Maya API became accessible via Python. With Python, not only can we make plug-ins as described above, but we can also access API commands in scripts, which adds a significant performance gain to existing toolsets.

### C++ vs. Python

Plug-ins can be made with both C++ and Python. So which one should you use? Both are useful but there are situations where one should be used over the other.

Anything complex or that works with larger data sets like deformers should probably be made with C++ for speeds sake. For simple nodes that are not performance critical, Python works fine. Anything dealing with OpenGL such as viewports and locators should be made with C++ as I have seen significant slowdowns with Python implementations.

Also, some API calls in Python are a total pain syntax-wise because the API expects a lot of C++ pointers and references, which is wrapped with a very cryptic module in Python (MScriptUtil) which is not documented very well.

I have used both C++ and Python when developing plug-ins. When I am writing a new node, I sometimes start with Python to work out algorithm details. Since Python isn’t compiled like C++, the iteration time is faster. There’s also less of a chance to crash Maya with array index and memory errors.

Most of the time, I stick with C++ just because that is what the end product is going to be. However, I use the API a lot with Python in scripts so it is still worth learning. All the API calls are the same; it is just a difference in syntax.

### Setting Up Your Development Environment

The first step in learning the API is setting up your build environment. The Maya API is packaged as a set of libraries that you will need to access. From the documentation, these libraries are:

* OpenMaya - Contains fundamental classes for defining nodes and commands and for assembling them into a plug-in.
* OpenMayaUI - Contains classes necessary for creating new user interface elements such as manipulators, contexts, and locators.
* OpenMayaAnim - Contains classes for animation, including deformers and inverse kinematics.
* OpenMayaFX - Contains classes for Autodesk Dynamics.
* OpenMayaRender - 包含用于执行渲染功能的类。

#### Python

如果您使用的是 Python，访问这些库就像将它们导入您的代码一样简单：

```
import maya.OpenMaya
import maya.OpenMayaUI
import maya.OpenMayaAnim
import maya.OpenMayaFX
import maya.OpenMayaRender
```

#### C++

我建议使用 CMake 帮助在 Windows、Linux 和 OSX 上创建构建环境。[您可以观看我创

... (原文过长，已截断)