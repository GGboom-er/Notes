---
tags: [html, Ref_Others]
---

# 🌐 Maya summary - Rodolphe Vaillant's homepage.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Maya summary - Rodolphe Vaillant's homepage.html](file:///Y:/GGbommer/Lib/Http/Maya%20summary%20-%20Rodolphe%20Vaillant's%20homepage.html)
- **文件名称**：Maya summary - Rodolphe Vaillant's homepage.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[Maya summary - Rodolphe Vaillant's homepage.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya summary - Rodolphe Vaillant's homepage

|  |  |
| --- | --- |
| [Rodolphe Vaillant's homepage](/)Research, teaching and more... |  |

* [Bio](/page/home "About me")
* [Tutorials](/page/teaching "Site map / Table of content")
* [Links](/page/links "Bookmarks / pinterests")
* [Blog](/weblog/weblog "Somewhat cleaner articles")
* [Jumble](/weblog/jumble "Draft notes")

# [Maya summary](/entry/63/maya-summary)

Shortcuts, MEL / python scripting, C++ API - 02/2015 - #[Maya](/category/maya)

![](/images/2020-07/maya_cheatsheet_banner.jpg)

Summary of elementary Maya feature.

# Resource

* [Introduction to Maya API (Chad Vernon)](https://www.chadvernon.com/maya-api-programming/)

# Shortcuts

List

### Camera

|  |  |
| --- | --- |
| alt + left click | Rotate |
| alt + middle click | Strafe / pan |
| alt + right click | Zoom |
| F | Focus on selection |

### Views

### Other

|  |  |
| --- | --- |
| S | Insert key frame |
|  |  |

  

# Architecture

Maya works on nodes. Nodes have attributes which we connect together using MEL or Python scripts.  
  
Maya GUI calls those script to setup the nodes.

# MEL script

MEL

## Manual

Bookmark the [MEL reference manual](https://help.autodesk.com/view/MAYAUL/2022/ENU/index.html?contextId=COMMANDS-INDEX) of whatever Maya version you are using.
Once you get an understanding of MEL scripting this is the go to page to find all MEL built-in commands.

## Useful resources

<http://ewertb.soundlinker.com/maya.php>

MEL syntax (quite good and concise):

<http://nccastaff.bournemouth.ac.uk/jmacey/OldWeb/RobTheBloke/www/>

## Syntax

Variables are always prefixed with '$' when declared and used:

```
int $myInt = 0;
string $helloString = "hello";
print( $helloString + " " + $myInt ); 
// outputs: 'hello 0'
```

Declaring arrays:

```
int $myArray[] = {1,3,9};
```

for loops (notice we don't declare the types):

```
for( $i=0, $j=0.0; $i<10; ++$i, $j+=0.75 ){
    print($j + ", "); 
}
// outputs: '0, 0.75, 1.5, 2.25, 3, 3.75, 4.5, 5.25, 6, 6.75,'
```

Iterate over array elements:

```
int $myArray[] = {1,3,9}; 
for($i = 0; $i < size($myArray); ++$i)
    print($myArray[$i] + ", "); 
// outputs: '1, 3, 9,'

// Alternatively:
for( $element in $myArray)  
    print($element + ", ");
```

MEL arrays are dynamic

```
int $myArray[] = {1,3,9}; 
$myArray[9] = -1;
for($i = 0; $i < size($myArray); ++$i)
    print($myArray[$i] + ", ");
// outputs: 1, 3, 9, 0, 0, 0, 0, 0, 0, -1,
```

## Array /multi attributes

Maya nodes contain attributes (access through 'plugs' in c++/python API). When an attribute holds an array we also call it a multi attribute or array attribute.

Multi attributes can be thought as a map (e.g. `map<unsigned (connection idx), Type (value)>`):

```
     attribute[3] (value) : [ elt1,  elt2,  elt3]
     Logical indices (key): {    0,     2,     9} // indices displayed in 'Node Editor'
     Physical indices     : {    0,     1,     2} // Always consecutive
```

Look up an attribute's connection and list the logical indices of the connection:

```
string $node_names[] = `listConnections ($source_node+".attribute_name")`;
// example output: {'node1', 'node2'}

int $connection_indices[] = `getAttr -multiIndices ($source_node+".attribute_name")`;
// example output: {0, 4}

// Loop through the nodes connected to the attribute '$source_node+".attribute_name[]"'
for( $i = 0; $i < size($node_names); ++$i) {    
    int $idx = $connection_indices[$i]; 
    string $name = $node_names[$i];   
}
```

How to describe an attribute / plug:

```
string $plug_name = "some_node_name.some_attr_name[index_atrr].some_compound_name"
```

Check connection at index:

Is a source {array} attribute currently connected to a node?   
This can be use to determine if an index of an array attribute is free and can be safely connected with `connectAttr()`.

```
string $con = `connectionInfo -sourceFromDestination ("some_node_name.some_attribute[index]")`;
if( size( $con ) == 0){ 
    /* Yea I'm free */ 
}
```

Find first available connection ([maya doc](https://download.autodesk.com/us/maya/2011help/Commands/getNextFreeMultiIndex.html)):

```
maya2014/scripts/AETemplates/getNextFreeMultiIndex.mel
source "getNextFreeMultiIndex.mel"
// N.B: no need to define index with [idx]
string $attribute_name = "some_node_name.some_attr_name";
// index from which we start looking up the array attribute.
int $start_idx = 0; 
getNextFreeMultiIndex(attribute_name, start_idx);
```

Remove element at index:

```
// This will remove the element with index 4 from the input of 
// the choice node as long as there are no incoming or outgoing 
// connections to the attribute. 
removeMultiInstance choice.input[4]; 
// This will remove the element with index 100 from the input of 
// the choice node, breaking any existing connections first.
removeMultiInstance -b true choice.input[100];
```

c.f maya2014/scripts/AETemplates/AEnewNonNumericMulti.mel and AEremoveMultiElement()

Get the size of the array attribute:

```
getAttr -s

... (原文过长，已截断)