---
tags: [html, Maya_API_Dev]
---

# 🌐 C++ Reference and Pointer Guide _ Tech Art Learning.html

> **一句话总结**：C++ 引用与指针（TechArtLearning）

## 🔗 本地文件
- [C++ Reference and Pointer Guide _ Tech Art Learning.html](file:///Y:/GGbommer/Lib/Http/C++%20Reference%20and%20Pointer%20Guide%20_%20Tech%20Art%20Learning.html)
- **文件名称**：C++ Reference and Pointer Guide _ Tech Art Learning.html
- **资源类型**：html
- **归属分类**：Maya_API_Dev
- **本地路径**：[[C++ Reference and Pointer Guide _ Tech Art Learning.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

C++ Reference and Pointer Guide | Tech Art Learning

[![](./C++ Reference and Pointer Guide _ Tech Art Learning_files/avatar.png)](https://github.com/leixingyu)

## Xingyu Lei

### Technical Artist

 California, US

Toggle navigation

### 

#### Featured Tools (**Free**)

[undefined](https://www.xingyulei.com/post/cpp-reference-pointer/undefined)

Forked from

undefined

undefined

undefined

[undefined](https://www.xingyulei.com/post/cpp-reference-pointer/undefined)

Forked from

undefined

undefined

undefined

[undefined](https://www.xingyulei.com/post/cpp-reference-pointer/undefined)

Forked from

undefined

undefined

undefined

[undefined](https://www.xingyulei.com/post/cpp-reference-pointer/undefined)

Forked from

undefined

undefined

undefined

### Categories

* [3d math](https://www.xingyulei.com/categories/3d-math/)4
* [graphics programming](https://www.xingyulei.com/categories/graphics-programming/)1
* [learning log](https://www.xingyulei.com/categories/learning-log/)7
* [maya communication](https://www.xingyulei.com/categories/maya-communication/)2
* [maya python api](https://www.xingyulei.com/categories/maya-python-api/)4
* [tech summary](https://www.xingyulei.com/categories/tech-summary/)15
* [unreal cinematic](https://www.xingyulei.com/categories/unreal-cinematic/)5

### Tag Cloud

[batch](https://www.xingyulei.com/tags/batch/) [c#](https://www.xingyulei.com/tags/c/) [c++](https://www.xingyulei.com/tags/c/) [command port](https://www.xingyulei.com/tags/command-port/) [general](https://www.xingyulei.com/tags/general/) [math](https://www.xingyulei.com/tags/math/) [maya](https://www.xingyulei.com/tags/maya/) [pipeline](https://www.xingyulei.com/tags/pipeline/) [pyqt](https://www.xingyulei.com/tags/pyqt/) [python](https://www.xingyulei.com/tags/python/) [rendering](https://www.xingyulei.com/tags/rendering/) [server](https://www.xingyulei.com/tags/server/) [socket](https://www.xingyulei.com/tags/socket/) [style](https://www.xingyulei.com/tags/style/) [template](https://www.xingyulei.com/tags/template/) [threading](https://www.xingyulei.com/tags/threading/) [unity](https://www.xingyulei.com/tags/unity/) [unreal](https://www.xingyulei.com/tags/unreal/) [windows](https://www.xingyulei.com/tags/windows/)

# C++ Reference and Pointer Guide

[2020-08-13](https://www.xingyulei.com/post/cpp-reference-pointer/)

[learning log](https://www.xingyulei.com/categories/learning-log/)

[c++](https://www.xingyulei.com/tags/c/)

## Basics

**De-referencing**

add \* before a pointer to expose the object’s value it’s pointing

* `varN`, varN’s value
* `ptrN`, varN’s address
* `*ptrN`, de-reference ptrN, varN’s value
* (`&ptrN`, ptrN’s address, which has little meaning)

**Symbol to access a member of a class or class object (instance)**

* `a->b`: **b** is the member of the object that pointer **a** refers to
* `a.b`: **b** is the member of the object, or the reference of an object **a**
* `a::b`: **b** is the member of the class, or namespace **a**

## Declaration

### Pointer Declaration

Syntax: `varType* varName`

Declaration

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` //declare a c++ pointer to an integer int* ptrx; ``` |

Initialization

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` // a pointer pointing to address of varN, varN type should be int int varN = 9; int* ptrN; ptrN = &varN; ``` |

short-hand:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` int* ptrN = &varN; ``` |

### Reference Declaration

Syntax: `varType& varName`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` int main() {     int& invalidRef;   // error: references must be initialized      int x = 5;     int& ref = x; // okay: reference to int is bound to int variable      return 0; } ``` |

When a reference is initialized with an object (or function), we say it is **bound** to that object (or function). The process by which such a reference is bound is called **reference binding**

references must be bound to a *modifiable variable*

## Function Pass Argument

> Both of these methods are prevented copying the variable, and capable of modifying the variable value that is passed in; if a variable is expensive to copy, e.g. struct, class

### By Reference

* Modify the variable, can’t pass in an un-modifiable variable like `const`

  Syntax `varType& varName`

  |  |  |
  | --- | --- |
  | ``` 1 2 3 4 ``` | ``` void printValue(int& y) {     std::cout << y << '\n'; } ``` |
* Prevent modifying the variable, while having the benefit of not making a copy

  Syntax `const varType& varName`

  |  |  |
  | --- | --- |
  | ``` 1 2 3 4 ``` | ``` void printValue(const int& y) {     std::cout << y << '\n'; } ``` |

### By Address (via pointer)

Syntax `varType* varName`, to access the variable, de-reference using `*varName`

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` void printByAddress(const std::string* ptr) // The function parameter is a pointer that holds the address of str {     std::cout << *ptr << '\n'; // print the value via the dereferenced

... (原文过长，已截断)