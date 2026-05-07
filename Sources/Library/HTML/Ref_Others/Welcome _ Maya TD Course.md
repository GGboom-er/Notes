---
tags: [html, Ref_Others]
---

# 🌐 Welcome _ Maya TD Course.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Welcome _ Maya TD Course.html](file:///Y:/GGbommer/Lib/Http/Welcome%20_%20Maya%20TD%20Course.html)
- **文件名称**：Welcome _ Maya TD Course.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[Welcome _ Maya TD Course.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Welcome | Maya TD Course

# [Maya TD Course](https://serguei-k.github.io/mayatd/)

# Welcome

This brief course is designed for the current CG industry professionals who would like to expand their technical understanding of Autodesk Maya software, and learn how best to utilize its advanced features to build efficient and robust CG pipelines.

### Contents

* [Architecture](#architecture)
  + [DG & DAG](#dg--dag)
    - [Nodes & Attributes](#nodes--attributes)
    - [Transforms](#transforms)
    - [Shapes](#shapes)
    - [DAG Path](#dag-path)
    - [Instancing](#instancing)
    - [Tracking Relationships](#tracking-relationships)
  + [Geometry & Deformation](#geometry--deformation)
    - [Object Space](#object-space)
    - [GroupParts & GroupId](#groupparts--groupid)
    - [Original Shape](#original-shape)
    - [Tweak Deformer](#tweak-Deformer)
  + [Asset Management](#asset-management)
    - [File Referencing](#file-referencing)
    - [Reference Edits](#reference-edits)
    - [Construction History](#construction-history)
    - [Namespaces](#namespaces)
    - [Versioning](#versioning)
  + [Alembic](#alembic)
    - [Maya Alembic](#maya-alembic-plugins)
    - [GPU Cache](#gpu-cache)

## Architecture

The architecture section covers the fundamentals of the Maya data model and some of its core features. It is by no means going to be an exhaustive reference, but it should provide a keen understanding of Maya mechanics that will allow you to design better solutions and troubleshoot problems.

### DG & DAG

The vast majority of all user interactions with Maya happens through the manipulation of either the DG or DAG. The DAG and DG are two seperate systems and serve different purposes.

**DG** (Dependency Graph) is really at the heart of Maya, it takes part in modeling, animation, and simulation. The purpose of the DG is to take some input from the user, such as numeric values or geometry, perform some work with this data, and output a new result to the user. The DG can be visualized in the *Node Editor* or the *Hypergraph (Connections mode)*.

#### Nodes & Attributes

At its core, all the work is performed by individual, self-contained nodes. Each node defines a series of attributes to accept input data and output the work product. These nodes can be connected together through their attributes, therefore constituting the dependency graph.

> You can create cyclic connections between nodes in the DG (ex. constraints) as long as there is no direct *affects* relationship between the connected attributes (or DAG side effects).

The attributes defined by the node represent a kind of an interface for the node to the rest of the graph. Maya supports attributes of various types, such as simple numeric attributes for integers and floats. In addition, complex attributes are supported and can hold data such as string, numeric arrays, and geometry.

In many cases it is useful to treat a group of related attributes as a single entity (ex. color or translation), for this purpose Maya provides a concept of *Compound Attributes*. A compound attribute behaves as a parent container to any number of child attributes of arbitrary type. Two compound attributes that have identically defined children can be safely connected together in the DG.

Any attribute can also be defined as an array, in which case it can hold an arbitrary number of child elements of the **same** type. Each array element, visualized by square brackets in the GUI, can be independently set or connected via a sparse index (note that array indexing is 0 based).

> Note that Maya documentation recommends that array plugs should **not** be connected together.

Additionally, attributes have several other properties that control their behavior, such as keyable and locked.

> You will frequently see a reference to attribute *plugs* in Maya documentation and API usage. You can think of an attribute as a description or template defined for a node type, while a plug is an actual physical entity for the attribute on a specific instance of that node.

**DAG** (Direct Acyclic Graph) is essentially the object hierarchy, it builds on top of DG and provides a way to describe the parent-child relationships. You can visualize the DAG in the *Outliner* or *Hypergraph (Hierarchy mode)*. This DAG relationship can further be modified using the *Parent* or *Group* commands.

> You can traverse the DAG hierarchy using the arrow keys, up-down to navigate the parent-child relationship, and left-right to navigate the siblings

Practically speaking there are two types of objects that are involved in defining the DAG hierarchy, a **Transform** node and a **Shape** node.

#### Transforms

A transform node defines a transformation in space. The transformation can be modified by setting the values of translation, rotation and scale attributes. A transform node can have any number of children and at most a single parent.

> You can visualize the transformation in the Viewport by turning on *Display->T

... (原文过长，已截断)