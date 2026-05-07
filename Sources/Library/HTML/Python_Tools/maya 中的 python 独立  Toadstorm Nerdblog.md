---
tags: [html, Python_Tools]
---

# 🌐 maya 中的 python 独立 – Toadstorm Nerdblog.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [maya 中的 python 独立 – Toadstorm Nerdblog.html](file:///Y:/GGbommer/Lib/Http/maya%20中的%20python%20独立%20–%20Toadstorm%20Nerdblog.html)
- **文件名称**：maya 中的 python 独立 – Toadstorm Nerdblog.html
- **资源类型**：html
- **归属分类**：Python & 开发环境
- **本地路径**：[[maya 中的 python 独立 – Toadstorm Nerdblog.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

maya 中的 python 独立 – Toadstorm Nerdblog

# maya 中的 python 独立

#### 由[**toadstorm 发表**](https://www.toadstorm.com/blog/?author=1)于2012-02-22

我最近一直在研究一些以批处理模式打开 Maya 场景组的工具，对每个文件运行 Python 或 MEL 操作（例如，快速添加渲染层并将材质一次应用于一大组对象，或者获取场景中所有引用的名称），然后返回数据或保存文件。这种事情可以在通常的窗口式 Maya 界面中完成，但这很慢，意味着用户必须坐在那里看着 Maya 打开一堆文件、运行操作等等。如果在独立（“批处理”）模式下运行 Maya，一次对大量文件运行脚本会快得多。

还有其他关于如何让 Python 在独立模式下运行的信息更丰富的帖子（我[特别从这篇](http://www.chadvernon.com/blog/resources/python-scripting-for-maya-artists/python-in-maya/)文章中学到了很多），但其要点是您首先运行 /bin/mayapy.exe，然后初始化Maya Python 解释器通过调用以下函数：

|  |  |
| --- | --- |
| 1个  2个 | `import` `maya.standalone as standalone`  `standalone.initialize(name``=``'python'``)` |

一旦完成，您就可以像往常一样开始编写脚本，从那里开始`import maya.cmds as cmds`并从那里开始工作。有些命令在独立模式下不可用，尤其是与 UI 有关的命令。

无论如何，在编写一个旨在处理大量未排序的 Maya 文件的脚本时，我意识到在打开古老的、损坏的场景时崩溃将是一个常见的问题，所以我不能单独加载一个 Maya 实例从脚本模式并让它循环运行所有内容。我需要能够一次处理一个文件，然后在处理成功时返回一些有用的信息，或者让我知道 Maya 是否崩溃，这样我以后就可以避免该文件或至少标记它。

为此，我使用了 Python 的[子进程](http://docs.python.org/library/subprocess.html) 模块。同样，我不打算详细介绍该模块，它非常复杂，但我将给出一个快速示例，说明我在调用脚本时如何使用它从 Maya 进程返回信息来自 Maya（或任何其他程序，真的）。

假设我希望此脚本向多个场景添加一个新的渲染层，并将每个场景中的所有网格添加到该新层。首先，我将编写实际创建图层并分配对象的脚本。

|  |  |
| --- | --- |
| 1个  2个  3个  4个  5个  6个 | `import` `sys`  `import` `maya.standalone as std`  `std.initialize(name``=``'python'``)`  `import` `maya.cmds as cmds`  `filename` `=` `sys.argv[``1``]`  `layername` `=` `sys.argv[``2``]` |

`sys.argv[1]`和`sys.argv[2]`是将变量传递给外部脚本的简单方法。`sys.argv[n]`just 表示第 n 个命令行参数，`sys.argv[1]`运行脚本时的第一个命令行参数也是如此（在调用脚本名称之后，例如，通过运行 mayapy.exe yourScript.py）。当我们调用这个脚本时，我们将向它传递一个要打开的文件和一个要添加的图层名称。

|  |  |
| --- | --- |
| 1个  2个  3个  4个  5个  6个  7  8个  9  10  11  12  13  14  15  16  17  18 | `def` `addRenderLayer(filename,layername):`  `try``:`  `cmds.``file``(filename,o``=``1``,f``=``1``)`  `newLyr` `=` `cmds.createRenderLayer(n``=``layername,empty``=``1``,makeCurrent``=``1``)`  `meshes` `=` `cmds.ls(``type``=``'mesh'``)`  `xforms` `=` `[]`  `for` `i` `in` `meshes:`  `xf` `=` `cmds.listRelatives(i,p``=``1``)[``0``]`  `xforms.append(xf)`  `cmds.editRenderLayerMembers(layername,xforms)`  `cmds.``file``(s``=``1``,f``=``1``)`  `sys.stdout.write(newLyr)`  `return` `newLyr`  `except` `Exception, e:`  `sys.stderr.write(``str``(e))`  `sys.exit(``-``1``)`    `addRenderLayer(filename,layername)` |

在这里，我们基于“layername”参数创建一个空渲染层，然后我们获取场景中的所有网格。在大多数场景中，人们将*变换*添加 到渲染层，而不是它们各自的形状节点，因此我们将通过创建一个空列表“xforms”，然后循环遍历每个网格并找到它们的第一个相关变换节点（因此是`listTransforms(i,p=1)[0]`因为`listTransforms` 返回一个列表）并将其附加到“xforms”，然后将“xforms”添加到新的渲染层。然后我们只保存文件并返回层的名称（我只是喜欢为我的函数返回值）。

我们还将新层的名称写入`stdout`. 稍后我将对此进行更详细的介绍，但它可以让我们将信息发送回稍后调用此脚本的程序。还有一个异常处理程序，它将遇到的任何错误写入`stderr`流，并以代码 -1 退出，这是“此程序异常退出”的一种约定。

将此文件另存为 makeNewLayer.py，保存在默认脚本目录中的某处。

接下来，我们将制作我们从 Maya 运行的流程......

|  |  |
| --- | --- |
| 1个  2个  3个  4个  5个  6个  7  8个  9  10  11  12  13  14  15  16 | `import` `maya.cmds as cmds`  `import` `subprocess`  `# replace mayaPath with the path on your system to mayapy.exe`  `mayaPath` `=` `'c:/program files/autodesk/maya2011/bin/mayapy.exe'`  `# replace scriptPath with the path to the script you just saved`  `scriptPath` `=` `'c:/users/henry/desktop/addRenderLayer.py'`  `def` `massAddRenderLayer(filenames,layername):`  `for` `filename` `in` `filenames:`  `maya` `=` `subprocess.Popen(mayaPath``+``' '``+``scriptPath``+``' '``+``filename``+``' '``+``layername,stdout``=``subprocess.PIPE,stderr``=``subprocess.PIPE)`  `out,err` `=` `maya.communicate()`  `exitcode` `=` `maya.returncode`  `if` `str``(exitcode) !``=` `'0'``:`  `print``(err)`  `print` `'error opening file: %s'` `%` `(filename)`  `else``:`  `print` `'added new layer %s to %s'` `%` `(out,filename)` |

好的，这里发生了很多事情。该`subprocess.Popen`函数使用三个参数调用 mayapy.exe：首先是我们要运行的脚本 (makeNewLayer.py)，然后是脚本需要的两个参数（文件名和层名称），然后是输入流和输出流都设置为`subprocess.PIPE`. 我对 subprocess 模块的了解还不够深入，但基本上当你运行一个流程时，有三个“流”：输入、输出和错误流，通常称为`stdin`,`stdout` 和`stderr`。当您将输入和输出流设置为`subprocess.PIPE`when calling 时`Popen()`，您可以确定进程将接收您提供给它的任何输入流（我们在这里没有这样做；相反，我们使用`sys.argv` 上面显示的方法）并且还反馈它给出的任何输出。  
下一个过程`communicate()`返回两个变量：`stdout` 和`stderr`。我们可以使用它来调试或监控进度。通常在 Maya 脚本编辑器中，如果您的脚本因任何原因失败，您将从错误中获得某种（可能）有用的信息。但是，除非您正在侦听错误流，否则您不会知道子流程出了什么问题。  
`communicate()`做了一些其他很棒的事情。首先，也是最重要的，它会等待子进程完成，然后再继续您的脚本。这真的很重要，因为您肯定不希望这样的脚本继续运行，直到该过程完成。其次，它在`Popen()`对象上设置了一些变量，其中之一是`Popen.returncode`. 如果您曾经浏览过 Maya 渲染日志并注意到诸如“Maya 退出状态：210”或“Maya 退出状态：0”之类的行，这些数字就是退出代码。Status 0表示程序正常退出；任何其他退出代码都意味着出了问题。由于我希望在打开或编辑场景时出现问题时收到通知，因此我检查是否`Popen.returncode`有任何非零值，如果是，我打印出错误流并留下一条通知，说明出现问题。如果一切正常，我只想知道它是否有效，所以我打印一个字符串。因为我把输出层写到`sys.stdout`，当我读`stdout` 从子进程中，我得到了新创建的层的名称。我这样做是因为如果场景中的另一个节点与新层具有相同的名称，则该层可能不会完全具有我想要的名称！

现在，实际运行脚本。如果您要从 Maya 运行 massAddRenderLayer()，如示例中所示，您可以这样称呼它：

|  |  |
| --- | --- |
| 1个  2个  3个  4个  5个  6个 | `# define a list of filenames to iterate through`  `filenames` `=` `[``'file1'``,``'file2'``,``'file3'``]`  `renderLayerToAdd` `=` `'someNewLayer'`    `# run procedure, assuming you've already defined it`  `massAddRenderLayer(filenames, renderLayerToAdd)` |

随着我制作更复杂的应用程序，我越来越多地使用 subpro

... (原文过长，已截断)