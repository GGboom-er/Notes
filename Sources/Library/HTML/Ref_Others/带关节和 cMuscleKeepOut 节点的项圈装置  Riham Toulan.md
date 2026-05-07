---
tags: [html, Ref_Others]
---

# 🌐 带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan.html](file:///Y:/GGbommer/Lib/Http/带关节和%20cMuscleKeepOut%20节点的项圈装置%20—%20Riham%20Toulan.html)
- **文件名称**：带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan

菜单

# [里哈姆图兰](http://www.rihamtoulan.com/)

角色技术总监

# [带关节和 cMuscleKeepOut 节点的项圈装置](http://www.rihamtoulan.com/blog/2018/3/24/faking-collisions-with-joints-based-setup-8snd2)

2018 年 4 月 26 日

大家好，差不多一个月前，我发布了这个装备测试，用于我为我正在制作的角色制作的碰撞设置。

查看全尺寸

![neck_collision_512.gif](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524749144545-HRJIPT26ECUQRY85Z58H/neck_collision_512.gif)![颈部碰撞_512.gif](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/neck_collision_512.gif)

该装备是基于关节的，因此适用于游戏动画。我无法使用相同的资产，但出于本教程的目的，我创建了另一个资产。 

需要 Maya 和绑定的基本知识。这不是绑定和绑定练习教程，它专门用于介绍在 Maya 中使用 cMuscleKeepOut 节点的技术。因此，请随意使用它并使其符合您在装配过程中通常使用的任何惯例和命名约定。

我会将这篇文章分为 3 个主要部分。曲线设置、碰撞设置和关节设置。但在我们继续之前，这是钻机最终的样子。

---

## [您可以在Gumroad](https://gum.co/PhhXO)上以 5 美元的价格购买工作文件

[![buygum5.png](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1525526821197-M8Y5NYJ8OOZ0ZI55OA32/buygum5.png)![买口香糖5.png](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/buygum5.png)](https://gum.co/PhhXO)

---

查看全尺寸

![neck_collision_570.gif](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524327141303-0LWNXXOE25JDJTTO4Z1K/neck_collision_570.gif)![neck_collision_570.gif](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/neck_collision_570.gif)

### Kiel Figgins 友善地指出，在某些情况下默认情况下不会加载 MayaMuscle 插件，因此请确保在插件管理器中加载 MayaMuscle.mll 插件。

查看全尺寸

![Loading the MayaMuscle plugin.](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524841988410-8P79XUJ7I1TAVYNKSN71/plugin.jpg)![加载 MayaMuscle 插件。](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/plugin.jpg)

加载 MayaMuscle 插件。

---

# **曲线设置**

**1 -**创建一个具有 8 个跨度的 nurbs 圆并将其命名为“collar\_crv”。

查看全尺寸

![Creating a nurbs Curve.](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1522000100397-YEK7SRKRCEE8BA30AAAN/nurbsCurve_create.jpg)![创建 nurbs 曲线。](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/nurbsCurve_create.jpg)

创建 nurbs 曲线。

查看全尺寸

![Nurbs Circle options](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1522011831546-FJOPLOK12UEPMFO02TVU/cirxcleAbstract.jpg)![Nurbs 圆选项](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/cirxcleAbstract.jpg)

Nurbs 圆选项

**2 -**沿衣领内侧塑造曲线。曲线顶点是与我们的碰撞网格的接触点，因此请确保将它们放置在您希望碰撞发生的位置。

查看全尺寸

![Curve placement. The head is hidden for clarity purposes.](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1523297325347-TNQXUQ46BG78GKQES8A9/curvePlacement.jpg)![曲线放置。 为清楚起见，头部被隐藏。](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/curvePlacement.jpg)

曲线放置。为清楚起见，头部被隐藏。

**3 -**为“collar\_crv”的每个顶点创建一个集群。在绑定选项卡中，转到变形>集群。

查看全尺寸

![Creating clusters](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1523303647234-5KNV391BNY5BNHJC2LX3/clusters.jpg)![创建集群](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/clusters.jpg)

创建集群

**4 -**每个集群都需要一个偏移组。按**CTRL+G**创建空组的快捷方式。然后选择组和集群并转到**修改>匹配转换>匹配所有转换。**现在组已捕捉到集群，您可以通过选择 clusterHandle 和组并按**P**或转到**Edit>parent**将集群作为组的父级。

查看全尺寸

![cluster_groups.jpg](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1523304511951-FRV0PI322RK9MXY71SMH/cluster_groups.jpg)![cluster_groups.jpg](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/cluster_groups.jpg)

---

# 碰撞设置

**5 -**现在我们创建我们的碰撞网格。大多数时候我使用多边形基元作为碰撞形状，如圆柱体或球体，但在这种情况下，我将使用头部网格的静态副本并删除不需要与曲线碰撞的面。然后将碰撞网格作为颈部驱动器的父级。为了演示，我只是直接在联合下为它添加了父级。

在这种情况下，我选择使用头部的复制品，因为他的下巴非常突出，让它与衣领碰撞会很好。

查看全尺寸

![collision_mesh_titles.gif](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524777913859-Z6F7AS8EB0RYPROS6ZAF/collision_mesh_titles.gif)![碰撞网格标题.gif](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/collision_mesh_titles.gif)

**6 -**创建碰撞网格的最后一步是选择 collision\_head 并转到 Rigging>Deform>Muscle>Muscles/Bones>Convert Surface to Muscle/Bone。

查看全尺寸

![collisionCapsule.jpg](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524083033104-N1XZNWQ03PZTXEIKCZSG/collisionCapsule.jpg)![碰撞胶囊.jpg](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/collisionCapsule.jpg)

**7 -**选择所有集群手柄组并转到 Rigging>Deform>Muscle>Self/Multi Collsion>KeepOut 的 Rig selection

查看全尺寸

![keepOutNodes.jpg](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524324335825-9FEA5LM0IH3ME2ANZUZT/keepOutNodes.jpg)![keepOutNodes.jpg](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/keepOutNodes.jpg)

**8 -**如果您在大纲视图中展开集群组，您将看到在集群句柄顶部创建了两个转换。cMuscleKeepOut 和 cMuscleKeepOutDriven 组。cMuscleKeepOut 节点设置碰撞发生时 cMuscleKeepOutDriven 组移动的局部方向。

查看全尺寸

![keepOutNodes_outliner.jpg](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524325759685-QOCQPMRFZFYVE49MKC6A/keepOutNodes_outliner.jpg)![keepOutNodes_outliner.jpg](./带关节和 cMuscleKeepOut 节点的项圈装置 — Riham Toulan_files/keepOutNodes_outliner.jpg)

**9 -**在我们将碰撞网格连接到 keep out 节点之前，让我们设置 In Direction 值以避免我们的集群跳到错误的方向。  
选择右侧簇句柄的所有 keep out 节点，并将 In Direction X 设置为 -1，将 In Direction Y 设置为 -0.5。这样，当碰撞发生时，簇手柄向右移动的次数是向下移动的两倍

... (原文过长，已截断)