---
tags: [tool, Maya_Rigging]
---
# 🛠️ riganything_maya_tool_v2
> **基于 RigAnything (SIGGRAPH TOG 2025) 的 Maya 自动骨骼绑定工具。**

- 📂 [riganything_maya_tool_v2](file:///Y:/GGbommer/scripts/riganything_maya_tool_v2)

## 💡 详细说明
# RigAnything for Maya 2025

基于 RigAnything (SIGGRAPH TOG 2025) 的 Maya 自动骨骼绑定工具。

## 架构

```
Maya 2025 UI  ─→  导出 OBJ  ─→  RigAnything 推理  ─→  解析 NPZ  ─→  Maya 创建骨骼+蒙皮
```

## 安装

```bash
cd riganything_maya_tool
python install.py
```

## 使用

Maya Script Editor 中执行:
```python
import riganything_maya.ui.main_window as rui; rui.show()
```

