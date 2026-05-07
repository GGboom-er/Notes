---
tags: [Core_Libraries, Maya_Rigging, tool]
tech_stack: [C++, Python]
---
# 🛠️ SeExpr
> **===================================================================**

- 📂 [SeExpr](file:///Y:/GGbommer/scripts/SeExpr)

## 💡 详细说明
===================================================================

  For info on using new v3 features and porting your code, see:

  http://wdas.github.io/SeExpr/doxygen/html/SeExpr_FAQ.html
  
===================================================================


# SeExpr - An embeddable expression evaluation engine


## Super impatient CMake building and installing guide

```bash
$ git clone https://github.com/wdas/SeExpr
$ cd SeExpr
$ mkdir build
$ cd build
$ cmake ../
$ make doc      # optional make documentation
$ make install
```

You can try the test application asciiGraph which is a simple
function grapher... e.g.
```bash
./asciiGraph "x^3-8*x"
```

## Getting started

Examining the demo applications in src/demo is a great way to see
some usage examples of the library. The basic strategy is to subclass
the Expression class and implement the methods that describe what
extra functions and variables your expression evaluation will need

Be sure to check out the doxygen pages for
