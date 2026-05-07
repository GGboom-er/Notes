---
tags: [Core_Libraries, Maya_Rigging, tool]
tech_stack: [C++, Python]
---
# 🛠️ maya-math-nodes
> **Collection of math nodes for Autodesk Maya**

- 📂 [maya-math-nodes](file:///Y:/GGbommer/scripts/maya-math-nodes)

## 💡 详细说明
## Maya Math Nodes
Collection of math nodes for Autodesk Maya

#### Building
[![Build](https://github.com/serguei-k/maya-math-nodes/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/serguei-k/maya-math-nodes/actions/workflows/build.yml)
[![Documentation Status](https://readthedocs.org/projects/maya-math-nodes/badge/?version=latest)](https://maya-math-nodes.readthedocs.io/en/latest/?badge=latest)

To build the library on Windows, clone the repository and navigate to the cloned directory,
then run the following commands:

```
mkdir build
cd build
cmake ../. -G "Visual Studio 16 2019 Win64"
```

This will generate a Visual Studio solution you can use to build.

To build the library on OSX or Linux use the following commands:

```
mkdir build
cd build
cmake ../. -G "CodeBlocks - Unix Makefiles"
make
```

The build looks for Maya in the default installation directory for each platform, however you can always provide it with a custom path:

```
-DMAYA_LOCATION=/apps/auto
