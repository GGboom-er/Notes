---
tags: [html, Ref_Others]
---

# 🌐 【Maya脚本学习】常见节点总结 - 知乎.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [【Maya脚本学习】常见节点总结 - 知乎.html](file:///Y:/GGbommer/Lib/Http/【Maya脚本学习】常见节点总结%20-%20知乎.html)
- **文件名称**：【Maya脚本学习】常见节点总结 - 知乎.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[【Maya脚本学习】常见节点总结 - 知乎.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

【Maya脚本学习】常见节点总结 - 知乎[![](https://zhuanlan.zhihu.com/p/408380205)](javascript:void(0))

切换模式

写文章

登录/注册

![【Maya脚本学习】常见节点总结](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-ed52b1fb6ba384af0b8bab9d31739c3b_720w.jpg)

# 【Maya脚本学习】常见节点总结

[![Axxzls](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-17ce4ecaec507d8cc8fdc63842e295e9_l.jpg)](https://www.zhihu.com/people/ai-xue-xi-kan-shi-jie)

[Axxzls](https://www.zhihu.com/people/ai-xue-xi-kan-shi-jie)

小研究生

4 人赞同了该文章

1.簇（cluster）

属于**变形器（deformer)**，通过**控制模型上的一个或者多个点**，修改权重，从而通过控制簇变形器的移动旋转缩放来影响模型的局部变化。

2.骨骼簇（skinCluster）

属于**变形器(deformer)**，常用来平滑皮肤，功能等同“刷权重”。通过**控制关节(joint)或变换节点（transform）**，修改权重，来改变几何的形态。

3.父约束（parentConstraint）

属于**动画（animation）**，可**移动旋转缩放**对象，输入可以是一系列target，包含属性：平移（targetTranslate）, 旋转（targetRotate）, 缩放（targetScale）, 旋转中心（targetRotatePivot）, 旋转缩放（targetRotateTranslate）, 父级矩阵（targetParentMatrix）, 旋转方向（targetRotateOrder）, 旋转偏移量（targetOffsetRotate）, 平移偏移量（targetOffsetTranslate）, 权重（ targetWeight）。可连接一系列模型，输出连接对象唯一。

4.方向约束（orientConstraint）

属于**动画（animation）**，可**旋转**对象，输入也可是一系列target,包含属性：旋转（targetRotate）, 旋转方向（targetRotateOrder）, 父级矩阵（targetParentMatrix）, 权重（targetWeight）。可连接一系列模型，输出连接对象唯一。

5.缩放约束（scaleConstraint）

属于**动画（animation）**，可**缩放**对象，输入也可是一系列target,包含属性：缩放（targetScale）, 父级矩阵（targetParentMatrix）, 权重（targetWeight）。可连接一系列模型，输出连接对象唯一。

6.多边形球体（polySphere）

属于**几何（geometry）**，根据给定的半径和不同方向的网格划分数来创建球体。如果球体的纹理属性（标签texture）开启，还会相应创建UV坐标。

7.表情基（blendShape）

属于**变形器（deformer)**，将给定的一组形状转换为一组表情基附加相应权重。

讲解变形器比较好的文档：（侵权请联系，马上删）

[二、Maya变形器 - 百度文库​wenku.baidu.com/view/a553d5a2cd84b9d528ea81c758f5f61fb6362865.html![](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-ad13d24911f1a8554a67d5ab0360cd1c_120x160.jpg)](https://link.zhihu.com/?target=https%3A//wenku.baidu.com/view/a553d5a2cd84b9d528ea81c758f5f61fb6362865.html)

8.表面渲染器（surfaceShader）

属于**渲染器（shader）/表面（surface）/工具（utility）**，可**直接控制**模型的颜色（color）, 透明度（transparency）及 材料的粗糙度（matte opacity）。控制时并未进行任何渲染计算，而是直接将模型的某属性与节点的颜色等输出属性连接，如若将模型的平移属性与节点的颜色输出连接，则移动模型，其颜色会发生变化。

9.渲染引擎（shadingEngine）/渲染集（shading group）

**父级为模型集（objectSet)**，将渲染器与几何连接，输出三种渲染方式：面渲染（surface shading）、体渲染（volume shading）和替换式渲染（displacement shading）

10.接近度固定“针”（proximityPin）

属于**几何（geometry）**，形状类似针，用于跟踪曲面上点的位置，是**2020版Maya**新加入的节点，“针”的位置取自输入表面上最近的点，返回该点的坐标值。

11. UV固定“针”（uvPin ）

同属**几何（geometry）**，形状似针，从指定的 UV 坐标中得到"针"的位置。

12.加减平均（plusMinusAverage）

属于**通用工具（utility>general）**，对于不同维的数据有Input/Output 1D/2D/3D的区别，对输入数据进行加法、或减法、或求平均、或无操作。

13.变换曲线（animCurve）

属于**动画（animation）**，根据输入输出的不同类型，又可下分为不同的节点参见图1

![](https://pic1.zhimg.com/v2-cf74407fe633febba407eefc27107250_b.jpg)

![](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-cf74407fe633febba407eefc27107250_720w.webp)

图1

14.单位换算（unitConversion）

属于**工具（Utility）下的尺寸（scalar）**。保证该节点两端的同一数值等价，即源端单位中下的“1”等价于连接端单位下的“1”。举例：若transform1.translateX和transform2.rotateX相连，translateX的单位cm，rotateX的单位角度，则1cm对应1度。连接完成后，若translateX输出100cm，则rotateX跟着改变100度，即使此时再改变translateX的单位为m，输出值1(m)，rotateX仍改变100度。

15.加权叠加（blendWeighted）

属于**数学（math）**，对输入求加权和。

output = input(0) \* weight(0) + input(1) \* weight(1) + ...

编辑于 2021-10-17 17:35

[Autodesk Maya](https://www.zhihu.com/topic/19601585)

[节点](https://www.zhihu.com/topic/20035573)

[Python](https://www.zhihu.com/topic/19552832)

​赞同 4​​6 条评论

​分享

​喜欢​收藏​申请转载

​

写下你的评论...

6 条评论

默认

最新

[![就这样吧](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-4de2b7f513899f8a5da0ba927faf7e57_l.jpg)](https://www.zhihu.com/people/f82f3485b035a97f4da9fce2dba28ce6)

[就这样吧](https://www.zhihu.com/people/f82f3485b035a97f4da9fce2dba28ce6)

只有第一个簇懂了，后面的做什么会接触

2022-12-22

​赞

[![Axxzls](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-17ce4ecaec507d8cc8fdc63842e295e9_l(1).jpg)](https://www.zhihu.com/people/5844f30efc5c6aff450f399cd36040ff)

[Axxzls](https://www.zhihu.com/people/5844f30efc5c6aff450f399cd36040ff)

作者

做骨骼绑定，面部驱动啥的

2022-12-22

​赞

[![春日](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-d8ae31100dbee45755b75ee8b91b3965_l.jpg)](https://www.zhihu.com/people/a237df18b3355c868328ce78f2c72e34)

[春日](https://www.zhihu.com/people/a237df18b3355c868328ce78f2c72e34)

写的挺好 我一边看也一遍基于你这个在学习

2021-10-02

​赞

[![Axxzls](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-17ce4ecaec507d8cc8fdc63842e295e9_l(1).jpg)](https://www.zhihu.com/people/5844f30efc5c6aff450f399cd36040ff)

[Axxzls](https://www.zhihu.com/people/5844f30efc5c6aff450f399cd36040ff)

作者

![[惊喜]](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-3846906ea3ded1fabbf1a98c891527fb.png)![[惊喜]](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-3846906ea3ded1fabbf1a98c891527fb.png)![[大笑]](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-3ac403672728e5e91f5b2d3c095e415a.png)

2021-10-04

​赞

[![苏格兰肠](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-abed1a8c04700ba7d72b45195223e0ff_l.jpg)](https://www.zhihu.com/people/63fb13d4dae39b5751d00a0e73823b4e)

[苏格兰肠](https://www.zhihu.com/people/63fb13d4dae39b5751d00a0e73823b4e)

楼主的基础概念的总结精简到位![[大笑]](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-3ac403672728e5e91f5b2d3c095e415a.png)![[大笑]](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-3ac403672728e5e91f5b2d3c095e415a.png)，忘记了就翻一下

2021-09-14

​赞

[![Axxzls](./【Maya脚本学习】常见节点总结 - 知乎_files/v2-17ce4ecaec507d8cc8fdc63842e2

... (原文过长，已截断)