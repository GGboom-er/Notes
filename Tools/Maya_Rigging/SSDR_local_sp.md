---
tags: [tool, Maya_Rigging]
---
# 🛠️ SSDR_local_sp
> **由 AI 深度扫描生成的本地脚本索引。**

- 📂 [SSDR_local_sp](file:///Y:/GGbommer/scripts/SSDR_local_sp)

## 💡 详细说明
### 🐍 代码结构与接口
**main.py**:
```text
SSDR_local_sp  –  原版功能 × Maya 2025 兼容
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
仅在必要处做 PySide6 / Qt6 / Python3.10+ 兼容修订，
业务逻辑、UI 控件名、信号槽绑定保持与旧脚本一致。
```
- **main.py**: `class MainWindow` `def maya_main_window()`, `def loadui()`, `def moveTime()`, `def tranningAnimation()`, `def getDagPath()`
