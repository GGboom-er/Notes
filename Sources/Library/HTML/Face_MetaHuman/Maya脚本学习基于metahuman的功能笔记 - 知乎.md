---
tags: [html, Face_MetaHuman]
---

# 🌐 【Maya脚本学习】基于metahuman的功能笔记 - 知乎.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [【Maya脚本学习】基于metahuman的功能笔记 - 知乎.html](file:///Y:/GGbommer/Lib/Http/【Maya脚本学习】基于metahuman的功能笔记%20-%20知乎.html)
- **文件名称**：【Maya脚本学习】基于metahuman的功能笔记 - 知乎.html
- **资源类型**：html
- **归属分类**：面部 & MetaHuman
- **本地路径**：[[【Maya脚本学习】基于metahuman的功能笔记 - 知乎.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

【Maya脚本学习】基于metahuman的功能笔记 - 知乎[![](https://zhuanlan.zhihu.com/p/408074041)](javascript:void(0))

切换模式

写文章

登录/注册

![【Maya脚本学习】基于metahuman的功能笔记](./【Maya脚本学习】基于metahuman的功能笔记 - 知乎_files/v2-ed52b1fb6ba384af0b8bab9d31739c3b_720w.jpg)

# 【Maya脚本学习】基于metahuman的功能笔记

[![Axxzls](./【Maya脚本学习】基于metahuman的功能笔记 - 知乎_files/v2-17ce4ecaec507d8cc8fdc63842e295e9_l.jpg)](https://www.zhihu.com/people/ai-xue-xi-kan-shi-jie)

[Axxzls](https://www.zhihu.com/people/ai-xue-xi-kan-shi-jie)

小研究生

11 人赞同了该文章

具体的命令使用方法参考官方帮助文档（2020版）：

[Help​help.autodesk.com/view/MAYAUL/2020/CHS/](https://link.zhihu.com/?target=https%3A//help.autodesk.com/view/MAYAUL/2020/CHS/)

1. 打开二进制文件

```
import maya.cmds as cmds
cmds.file(
            file_path,
            f=True,
            options="v=0;",
            ignoreVersion=True,
            typ="mayaBinary",
            o=True,
         )
```

2.寻找特定类型的节点

```
import maya.cmds as cmds
rbf_node = ""
for node in history:
    if cmds.nodeType(node) == "****":  # **** 为节点类型
       rbf_node = node
```

对于Maya中的节点类型总结，可参看本人的另一篇文章：

[Axxzls：【maya脚本学习】节点类型总结6 赞同 · 2 评论文章![](./【Maya脚本学习】基于metahuman的功能笔记 - 知乎_files/v2-ed52b1fb6ba384af0b8bab9d31739c3b_r.jpg)](https://zhuanlan.zhihu.com/p/408243384)

例如对于节点‘embedded Node RL4’，需要将其输出属性bsOutputs与目标blendshape连接，可调用代码

```
import maya.cmds as cmds
cmds.connectAttr(
                rfb_node + ".bsOutputs[" + str(i) + "]",
                blendShape_targets[i],
                f=True,
                )
```

3.选择一个组层级里的几何体

* 使用dag标签，可以选择是第几层级
* 在maya里一个组其实就是一个变换（transform）类型的节点，即maya**大纲视图显示的模型名称都是变换类型节点**
* 通过type标签过滤mesh获取到的只是模型的形状（shape）节点，需要使用listRelatives命令来获取shape所在的变换名称，即大纲视图中的模型名称

```
import maya.cmds as cmds

#通过dag标签获取所有子物体，l标签开启节点全路径名称，通过type来过滤mesh物体
sn = cmds.ls(sl=1,dag=1,l=1,type=['mesh']) 

#获取dag的父级模型名称
def get_parent_from_dag(self, dag):
    return cmds.listRelatives(dag, p=True)

#通过transform名称获取子节点的形状(shape)
def get_shapes_from_transform(self, transform):
    return cmds.listRelatives(transform, s=True)

#列出skeleton_root下的所有模型名称，注意孙节点排列在子节点上面
cmds.listRelatives(skeleton_root, ad=True)
#列出skeleton_root下的所有路径名称，注意孙节点排列在子节点上面
cmds.listRelatives(skeleton_root, ad=True，f=True）
```

4.设置定位器并与模型的某部分绑定

```
import maya.cmds as cmds

#与变换节点建立关系
# cmds.spaceLocator将定位器放在变换节点的位置处，cmds.parentConstraint将其与模型建立父子关系
#即 locator保持与transform一样的位置（position）和旋转（rotation）
def locators_from_transforms(self, transforms):
        locators = []
        for transform in transforms:
            locator = cmds.spaceLocator(name=transform + "_loc")[0]
            cmds.delete(cmds.parentConstraint(transform, locator, mo=False))
            locators.append(locator)
        return locators

#与模型的顶点建立联系
#得到顶点世界坐标 > 将定位器放置在某mesh的某个顶点位置处 > 设置定位器的坐标值与顶点的世界坐标一致
 def locator_from_vertex(self, geometry, vertex):
        vertex_world_space_position = cmds.xform(
            geometry + ".vtx[" + str(vertex) + "]",
            query=True,
            translation=True,
            worldSpace=True,
        )
        vertex_locator = cmds.spaceLocator(
            name=geometry + "_" + str(vertex) + "_loc"
        )[0]
        cmds.setAttr(
            vertex_locator + ".translateX", vertex_world_space_position[0]
        )
        cmds.setAttr(
            vertex_locator + ".translateY", vertex_world_space_position[1]
        )
        cmds.setAttr(
            vertex_locator + ".translateZ", vertex_world_space_position[2]
        )
        return vertex_locator

#与边缘建立联系
#在选中的边缘曲线上建立簇变形器>建立簇变形器与标记点的父子关系，传递参数后删去父子关系
#>将标记点绑定在边缘上>删掉中间过渡的簇变形器
 def locator_from_edge_loop(self, geometry, edge):
        cmds.polySelect(geometry, el=edge)
        cluster = cmds.cluster(name=geometry + str(edge) + "_cluster")
        locator = cmds.spaceLocator(name=geometry + str(edge) + "_locator")[0]
        cmds.delete(cmds.parentConstraint(cluster, locator, mo=False))
        cmds.delete(cluster)
        return locator
```

5.与骨骼簇（skinCluster）相关

将**关节（joints）或骨骼（skeleton）**和**几何（geometry）**通过骨骼簇节点绑定。每个几何面上点可以由任意数量的关节影响，各关节的影响程度通过权重表征。权重可用skinPercent命令进行修改。

```
import maya.cmds as cmds

#创建骨骼簇
#tsb标签设置几何将只与选定的关节绑定
def create_skinCluster(self, joints, geometry):
        skinCluster = cmds.skinCluster(
            joints, geometry, tsb=True, name=geometry + "_skinCluster"
        )
        return skinCluster

#从几何中得到骨骼簇
def get_skinCluster_from_geometry(self, geometry):
        history = cmds.listHistory(geometry)
        for node in history:
            if cmds.nodeType(node) == "skinCluster":
                return node

#从骨骼簇得到起作用的关节名称
#在quary模式下，influence标签控制返回起作用的关节或骨骼
def get_joints_from_skinCluster(self, skinCluster):
        joints = cmds.skinCluster(skinCluster, query=True, influence=True)
        return joints

#从骨骼簇得到几何名称
def get_geometry_from_skinCluster(self, skinCluster):
        return self.get_parent_from_dag(
            cmds.ls(cmds.listHistory(skinCluster, f=True), type="mesh")[0]
        )

#通过贴图坐标，将一个几何的骨骼簇的权重复制（非镜像）到另一个几何上
#surfaceAssociation标签控制权重迁移的方法，有“closestPoint", "rayCast", o

... (原文过长，已截断)