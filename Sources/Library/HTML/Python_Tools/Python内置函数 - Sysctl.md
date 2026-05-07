---
tags: [html, Python_Tools]
---

# 🌐 Python内置函数 - Sysctl.html

> **一句话总结**：全内置函数详解（Sysctl）

## 🔗 本地文件
- [Python内置函数 - Sysctl.html](file:///Y:/GGbommer/Lib/Http/Python内置函数%20-%20Sysctl.html)
- **文件名称**：Python内置函数 - Sysctl.html
- **资源类型**：html
- **归属分类**：Python_Tools
- **本地路径**：[[Python内置函数 - Sysctl.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Python内置函数 - Sysctl

[所有文章](/posts/)  [标签](/tags/)  [分类](/categories/)  [笔记](/categories/note/)  [关于](/about/)

[取消](javascript:void(0);)

[所有文章](/posts/)[标签](/tags/)[分类](/categories/)[笔记](/categories/note/)[关于](/about/)

## 目录

# Python内置函数

[xieth](/ "Author") 收录于 [Programming](/categories/programming/)

2017-05-30  约 7461 字 
 预计阅读 15 分钟

目录

## 数学运算

* abs：绝对值

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` def abs(*args, **kwargs): # real signature unknown     """ Return the absolute value of the argument. """     pass ``` |

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` >>>abs(-4) 4 ``` |

* divmod：返回两个数值的商和余数

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` def divmod(x, y): # known case of builtins.divmod     """ Return the tuple (x//y, x%y).  Invariant: div*y + mod == x. """     return (0, 0) ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` >>>divmod(7,2) (3, 1) >>>divmod(7,1.5) (4.0, 1.0) ``` |

* max：返回可迭代对象中的元素中的最大值或者所有参数的最大值

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 ``` | ``` def max(*args, key=None): # known special case of max     """     max(iterable, *[, default=obj, key=func]) -> value     max(arg1, arg2, *args, *[, key=func]) -> value      With a single iterable argument, return its biggest item. The     default keyword-only argument specifies an object to return if     the provided iterable is empty.     With two or more arguments, return the largest argument.     """     pass ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` >>> max(1,2,3) # 传入3个参数 取3个中较大者 3 >>> max('1234') # 传入1个可迭代对象，取其最大元素值 '4' >>> max(-1,0) # 数值默认去数值较大者 0 >>> max(-1,0,key = abs) # 传入了求绝对值函数，则参数都会进行求绝对值后再取较大者 -1 ``` |

* min：返回可迭代对象中的元素中的最小值或者所有参数的最小值

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 ``` | ``` def min(*args, key=None): # known special case of min     """     min(iterable, *[, default=obj, key=func]) -> value     min(arg1, arg2, *args, *[, key=func]) -> value      With a single iterable argument, return its smallest item. The     default keyword-only argument specifies an object to return if     the provided iterable is empty.     With two or more arguments, return the smallest argument.     """     pass     """ Return the absolute value of the argument. """     pass ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` >>> min(1,2,3) # 传入3个参数 取3个中较小者 1 >>> min('1234') # 传入1个可迭代对象，取其最小元素值 '1' >>> min(-1,-2) # 数值默认去数值较小者 -2 >>> min(-1,-2,key = abs)  # 传入了求绝对值函数，则参数都会进行求绝对值后再取较小者 -1 ``` |

* pow：返回两个数值的幂运算值或其与指定整数的模值

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` def pow(*args, **kwargs): # real signature unknown     """     Equivalent to x**y (with two arguments) or x**y % z (with three arguments)      Some types, such as ints, are able to use a more efficient algorithm when     invoked using the three argument form.     """     pass ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` >>> pow(2,3) >>> 8 >>> >>> pow(2,3,5) >>> 3 ``` |

* round：对浮点数四舍五入

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` def round(number, ndigits=None): # real signature unknown; restored from __doc__     """     round(number[, ndigits]) -> number          Round a number to a given precision in decimal digits (default 0 digits).     This returns an int when called with one argument, otherwise the     same type as the number. ndigits may be negative.     """     return 0 ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` >>>round(4.33) 4 >>>>round(1.44443326,4) 1.4444 ``` |

* sum：对元素类型是数值的可迭代对象中的每个元素求和

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` def sum(*args, **kwargs): # real signature unknown     """     Return the sum of a 'start' value (default: 0) plus an iterable of numbers      When the iterable is empty, return the start value.     This function is intended specifically for use with numeric values and may     reject non-numeric types.     """     pass ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` >>> sum((1,2,3,4))  # 传入可迭代对象 10 >>> sum((1.5,2.5,3.5,4.5))  # 元素类型必须是数值型 12.0 >>> sum((1,2,3,4),-10) 0 ``` |

## 类型转换

* bool：根据传入的参数的逻辑值创建一个新的布尔值

|  |  |
| --- | --- |
| ``` 1 2 ``` | ```     def __init__(self, x): # real signature unknown; restored from __doc__         pass ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` >>> bool() #未传入参数 False >>> bool(0) #数值0、空序列等值为False False >>> bool(1) True ``` |

* int：根据传入的参数创建一个新的整数

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 ``` | ```         def __init__(self, x, base=10): # known special case of int.__init__         """         int(x=0) -> integer         int(x, base=10) -> integer          Convert a number or string to an integer, or return 0 if no arguments         are given.  If x is a number, return x.__int__().  For floating point         numbers, this truncates towards zero.          If x is not a number or if base is given, then x must be a string,         bytes, or bytearray instance representing an integer literal in the     

... (原文过长，已截断)