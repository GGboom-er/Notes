---
tags: [html, Ref_Others]
---

# 🌐 Maya_ look up array attribute connections - Rodolphe Vaillant's homepage.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Maya_ look up array attribute connections - Rodolphe Vaillant's homepage.html](file:///Y:/GGbommer/Lib/Http/Maya_%20look%20up%20array%20attribute%20connections%20-%20Rodolphe%20Vaillant's%20homepage.html)
- **文件名称**：Maya_ look up array attribute connections - Rodolphe Vaillant's homepage.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[Maya_ look up array attribute connections - Rodolphe Vaillant's homepage.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya: look up array attribute connections - Rodolphe Vaillant's homepage

|  |  |
| --- | --- |
| [Rodolphe Vaillant's homepage](/)Research, teaching and more... |  |

* [Bio](/page/home "About me")
* [Tutorials](/page/teaching "Site map / Table of content")
* [Links](/page/links "Bookmarks / pinterests")
* [Blog](/weblog/weblog "Somewhat cleaner articles")
* [Jumble](/weblog/jumble "Draft notes")

# [Maya: look up array attribute connections](/entry/136/maya-lookup-array-attribute-connections)

Maya list / lookup multi attribute connections in MEL & Python - 01/2022 - #[Maya](/category/maya)

![](/images/2022-01/maya_listconnections_banner.jpg)

# MEL

Consider this node and connections to the array (multi) attribute `.matrix`:

![](/images/2022-01/skin_cluster_matrix_connections.jpg)

MEL command to list every DG nodes connected to a multi attribute (a.k.a array attribute):

```
string $joint_names[] = `listConnections ($skincluster+".matrix")`;
// example output: {'joint1', 'joint2'}
```

Now here is how to list the "logical" indices of an array attribute that are connected to a node:

```
int $joint_indices[] = `getAttr -multiIndices ($skincluster+".matrix")`;
// example output: {0, 2}
```

Note: you may recall that array attributes can be sparse, for instance:

```
    array_attribute[2] : [ joint1,  joint2]
    Logical indices    : {      0,       2} 
    Physical indices   : {      0,       1}
```

## Summary

This is how to transfer the connections of a multi (i.e. array) attribute from one Maya node to another:

```
string $joint_names[] = `listConnections ($source_skincluster+".matrix")`;
int $joint_indices[] = `getAttr -multiIndices ($source_skincluster+".matrix")`;

// Loop through the nodes connected to the attribute '$source_skincluster+".matrix[]"'
for( $i = 0; $i < size($joint_indices); ++$i) {    
    int $idx = $joint_indices[$i]; 
    string $name = $joint_names[$i];   
    // Reconnect joints to another skin cluster while preserving the original indices of the joints:
    connectAttr ($name+".worldMatrix[0]") ($destination_skincluster+".matrix["+$idx+"]")
}
```

# Python 2.0 API

The above MEL code translates as follows:

```
from maya.api.OpenMaya import *

# get_MObject() and get_MPlug() are utilities I define below
obj = get_MObject("skinCluster1")
plug = get_MPlug(obj, "matrix")
for i in range(plug.numElements()):
    plug_element = plug.elementByPhysicalIndex(i)
    print( "name: " + plug_element.name() )
    print( "logical index: " + str(plug_element.logicalIndex()) )
    print( "physical index: " + str(i) )
    print( "" )
```

Output:

```
# name: skinCluster1.matrix[0]
# logical index: 0
# physical index: 0
#
# name: skinCluster1.matrix[2]
# logical index: 2
# physical index: 1
```

get\_MObject() & get\_MPlug() definitions

```
from maya.api.OpenMaya import *

def get_MObject(node_name):
    if isinstance(node_name, MObject):
        return node_name

    if isinstance(node_name, MDagPath):
        return node_name.node()

    slist = MSelectionList()
    try:
        slist.add(node_name)
    except RuntimeError:
        assert False, 'The node: "'+node_name+'" could not be found.'

    matches = slist.length()
    assert (matches == 1), 'Multiple nodes found for the same name: '+node_name

    obj = slist.getDependNode(0)
    return obj
# -----------------

def get_MPlug(obj, attribute):
    if not isinstance(obj, MObject):
        assert False, "expected MObject"
    dep = MFnDependencyNode(obj)
    plug = MPlug()
    try:
        plug = dep.findPlug( attribute, True)
    except RuntimeError:
        assert False, 'The attribute: "'+attribute+'" could not be found.'
          
    assert (not plug.isNull), 'The attribute: "'+attribute+'" could not be found.'
    return plug
# -----------------
```

[![Rss](/images/rss.svg)](/index.php?feed=rss)
[![Paypal donation](/images/paypal_donate_button.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=blog%40rodolphe-vaillant.fr&item_name=Thank+you+%3AD¤cy_code=USD&source=url&lc=EN&country=US)

No comments

Please enable Javascript (and reload this page) to add any comments.

Name

Email
 (optional field, I won't disclose or spam but it's necessary to notify you if I respond to your comment)

All html tags except <b> and <i> will be removed from your comment. You can make links by just typing the url or mail-address.

Anti-spam question:  
**√4 + 40 = ?**

You could live a better life, if you had a better mind and a better body.

![](/pivotx/scheduler.php)