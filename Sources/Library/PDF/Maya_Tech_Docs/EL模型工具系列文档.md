---
tags: [pdf, Maya_Tech_Docs]
---

# 📄 EL模型工具系列文档.pdf

> **一句话总结**：EL 模型工具使用说明

## 🔗 本地文件
- [EL模型工具系列文档.pdf](file:///Y:/GGbommer/Lib/PDF/EL模型工具系列文档.pdf)
- **文件名称**：EL模型工具系列文档.pdf
- **资源类型**：pdf
- **归属分类**：Maya 技术文档
- **本地路径**：[[EL模型工具系列文档.pdf]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 PDF 提取内容

**前言/导读**:
Tool Pack 
Author: Erik Lehmann
Copyright (c) 2019 Erik Lehmann
Email: contact(at)eriklehmann.com
/ / /
Changelog:
EL_CheckerPattern:
        v1.0
⦁ 
check if your UVs are properly unfolded, oriented and equal in size
⦁ 
create, assign, remove and delete a UV shader 
⦁ 
custom 1k texture map
⦁ 
set UV texture tiling from 1-32k
EL_CompactRenamer:
        v1.0
⦁ 
rename objects in Maya
⦁ 
automatic numeration for multiple objects
⦁ 
add Prefixes 
⦁ 
add Suffixes
⦁ 
Search and Replace function
EL_Distribute:
        v1.0
⦁ 
Distribute overlapping objects based on their bounding box
⦁ 
Option to add spacing between the objects
EL_NthEdge:
        v1.0
⦁ 
select every nth edge in a loop, ring or border
- - - - - - - - - - - - - - - - - - - - - - - - - - - -
How to install:
1. Copy 
⦁ 
EL_CheckerPattern.py + UVCheckerPattern_1K.tga
⦁ 
EL_CompactRenamer.py
⦁ 
EL_Distribute.py
⦁ 
EL_NthEdge.py
to: 
⦁ 
Windows: \Users\<username>\Documents\maya\<mayaversion>\prefs\scripts
1

⦁ 
Linux: $HOME/maya/<mayaversion>/prefs/scripts
⦁ 
Mac: $HOME/Library/Preferences/Autodesk/maya/<mayaversion>/prefs/scripts
2. Launch / Restart Maya
3. In Maya, open a 'Python Tab' in the 'Script Editor' 
and execute each code block separately to launch the respective tool:
import EL_Distribute as ELDis
ELDis.MainClassElDistribute()
import EL_CheckerPattern as ELCP
ELCP.MainClassElCheckerPattern()
import EL_CompactRenamer as ELComRen
ELComRen.MainClassCompactRen()
import EL_NthEdge as ELNthE
ELNthE.MainClassElNthEdge()
2