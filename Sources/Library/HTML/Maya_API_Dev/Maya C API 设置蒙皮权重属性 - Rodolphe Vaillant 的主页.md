---
tags: [html, Maya_API_Dev]
---

# 🌐 [Maya C++ API] 设置蒙皮权重属性 - Rodolphe Vaillant 的主页.html

> **一句话总结**：C++ API 操作蒙皮权重

## 🔗 本地文件
- [[Maya C++ API] 设置蒙皮权重属性 - Rodolphe Vaillant 的主页.html](file:///Y:/GGbommer/Lib/Http/[Maya C++ API] 设置蒙皮权重属性 - Rodolphe Vaillant 的主页.html)
- **文件名称**：[Maya C++ API] 设置蒙皮权重属性 - Rodolphe Vaillant 的主页.html
- **资源类型**：html
- **归属分类**：Maya_API_Dev
- **本地路径**：[[[Maya C++ API] 设置蒙皮权重属性 - Rodolphe Vaillant 的主页.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

[Maya C++ API] 设置蒙皮权重属性 - Rodolphe Vaillant 的主页

|  |  |
| --- | --- |
| [Rodolphe Vaillant 的主页](http://rodolphe-vaillant.fr/)研究、教学等... |  |

* [生物](http://rodolphe-vaillant.fr/page/home "关于我")
* [教程](http://rodolphe-vaillant.fr/page/teaching)
* [链接](http://rodolphe-vaillant.fr/page/links)
* [博客](http://rodolphe-vaillant.fr/weblog/weblog "我的东西")

# [[Maya C++ API] 设置蒙皮权重属性](http://rodolphe-vaillant.fr/entry/79/maya-c-api-set-skinning-weight-attributes)

用于设置平滑蒙皮权重的代码片段。- 03/2017 - #[玛雅人](http://rodolphe-vaillant.fr/category/maya)

![](./[Maya C++ API] 设置蒙皮权重属性 - Rodolphe Vaillant 的主页_files/set_skin_weights_banner.jpg)

一些 C++ Maya API 代码用于设置皮肤簇节点的皮肤权重（多属性）。

使用 Mplug 设置皮肤权重（多属性/数组属性）。中间速度

|  |
| --- |
| `void` `set_skinning_weights``(` |

|  |
| --- |
| `MObject` `skin_cluster_node,` |

|  |
| --- |
| `const` `std::vector``<` `std::map``<``int``/*joint id*/``,` `float``/*joint weight*/``> >& weights``)` |

|  |
| --- |
| `{` |

|  |
| --- |
| `MStatus` `status;` |

|  |
| --- |
| `MFnDependencyNode` `deformer_node``(``skin_cluster_node, &status``)``;` |

|  |
| --- |
| `mayaCheck``(``status``)``;` |

|  |
| --- |
| `MPlug` `weight_list_plug = deformer_node``.``findPlug``(``"weightList"``,` `true``, &status``)``;` |

|  |
| --- |
| `mayaCheck``(``status``)``;` |

|  |
| --- |
| `for``(` `unsigned` `i =` `0``; i < weight_list_plug``.``numElements``(``)``; i++` `)``// For each vertex` |

|  |
| --- |
| `{` |

|  |
| --- |
| `// weightList[i]` |

|  |
| --- |
| `MPlug` `ith_weights_plug = weight_list_plug``.``elementByPhysicalIndex``(` `i` `)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `// weightList[i].weight` |

|  |
| --- |
| `MPlug` `plug_weights = ith_weights_plug``.``child``(``0``)``;` `// access first compound child` |

|  |
| --- |
|  |

|  |
| --- |
| `// First reset values to zero:` |

|  |
| --- |
| `int` `nb_weights = plug_weights``.``numElements``(``)``;` |

|  |
| --- |
| `for``(` `int` `j =` `0``; j < nb_weights; j++` `)` `{` `// for each joint` |

|  |
| --- |
| `MPlug` `weight_plug = plug_weights``.``elementByPhysicalIndex``(` `j` `)``;` |

|  |
| --- |
| `// weightList[i].weight[j]` |

|  |
| --- |
| `mayaCheck``(` `weight_plug``.``setValue``(` `MObject``(``)` `)` `)``;` |

|  |
| --- |
| `}` |

|  |
| --- |
|  |

|  |
| --- |
| `for``(``const` `std::pair``<anim``::``bone``::``Id``,` `float``>& value : weights``[``i``]``)` `{` |

|  |
| --- |
| `MPlug` `weight_plug = plug_weights``.``elementByLogicalIndex``(` `value``.``first` `)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `// weightList[i].weight[value.second]` |

|  |
| --- |
| `mayaCheck``(` `weight_plug``.``setValue``(` `value``.``second` `)` `)``;` |

|  |
| --- |
| `}` |

|  |
| --- |
| `}` |

|  |
| --- |
| `}` |

设置多属性/数组属性的最快方法是通过 DAG 节点完成。（比 MPlugs 快 100 倍！）

|  |
| --- |
| `void` `set_skinning_weights``(` |

|  |
| --- |
| `const` `std::vector``<``std::map``<``int``/*joint id*/``,` `float``/*skin weight*/``> >& weights,` |

|  |
| --- |
| `MDataBlock``& block``)` |

|  |
| --- |
| `{` |

|  |
| --- |
| `MStatus` `status =` `MS``::``kSuccess;` |

|  |
| --- |
| `MArrayDataHandle` `array_hdl = block``.``outputArrayValue``(``_s_skin_weights``, &status``)``;` |

|  |
| --- |
| `mayaCheck``(``status``)``;` |

|  |
| --- |
| `for``(``unsigned` `i =` `0``; i < weights``.``size``(``)``; i++``)` |

|  |
| --- |
| `{` |

|  |
| --- |
| `mayaCheck``(` `array_hdl``.``jumpToArrayElement``(` `i` `)` `)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `// weightList[i]` |

|  |
| --- |
| `MDataHandle` `element_hdl = array_hdl``.``outputValue``(` `&status` `)``;` |

|  |
| --- |
| `mayaCheck``(``status``)``;` |

|  |
| --- |
| `// weightList[i].weight` |

|  |
| --- |
| `MDataHandle` `child = element_hdl``.``child``(` `_s_per_joint_weights` `)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `MArrayDataHandle` `weight_list_hdl``(``child, &status``)``;` |

|  |
| --- |
| `mayaCheck``(``status``)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `MArrayDataBuilder` `weight_list_builder = weight_list_hdl``.``builder``(``&status``)``;` |

|  |
| --- |
| `mayaCheck``(``status``)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `unsigned` `handle_count = weight_list_hdl``.``elementCount``(``&status``)``;` |

|  |
| --- |
| `mayaCheck``(``status``)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `unsigned` `builder_count = weight_list_builder``.``elementCount``(``&status``)``;` |

|  |
| --- |
| `mayaCheck``(``status``)``;` |

|  |
| --- |
| `mayaAssert``(` `builder_count == handle_count``)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `std::map``<``int``/*influence obj id / joint id*/``,` `float``> map = weights``[``i``]``;` |

|  |
| --- |
|  |

|  |
| --- |
| `std::vector` `to_remove;` |

|  |
| --- |
| `to_remove``.``reserve``(` `map``.``size``(``)` `)``;` |

|  |
| --- |
|  |

|  |
| --- |
| `// Scan array, update existing element, remove unsused ones` |

|  |
| --- |
| `for``(``unsigned` `j =` `0``; j < handle_count; ++j``)` |

|  |
| --- |
| `{` |

|  |
| --- |
| `// weightList[i].weight[j]` |

| 

... (原文过长，已截断)