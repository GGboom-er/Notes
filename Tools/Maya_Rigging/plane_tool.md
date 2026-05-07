---
tags: [Maya_Rigging, Pipeline_General, tool]
tech_stack: [MEL, PySide/PyQt, Python]
---
# 🛠️ plane_tool
> ****一个为CGI/DCC工作流设计的综合性工具集，旨在提升动画、绑定、建模、缓存以及与Unreal Engine交互的效率和质量。****

- 📂 [plane_tool](file:///Y:/GGbommer/scripts/plane_tool)

## 💡 详细说明
# Plane Tool Project (平面工具项目)

**一个为CGI/DCC工作流设计的综合性工具集，旨在提升动画、绑定、建模、缓存以及与Unreal Engine交互的效率和质量。**
(A comprehensive toolset designed for CGI/DCC workflows, aimed at enhancing efficiency and quality in animation, rigging, modeling, caching, and Unreal Engine interaction.)

## 核心功能模块 (Core Functional Modules)

### 1. 动画工具 (Animation Tools) - `aniTools/`
*   **引用管理 (Reference Management)**: 提供批处理引用、修改引用路径和修复引用名称的功能，确保大型场景中引用资产的稳定性和可管理性。
*   **关键帧优化 (Keyframe Optimization)**: 包含关键帧减面（`keyframeReduction`）和动画曲线平滑（`smoothAnimCurve`）工具，用于精简动画数据，提高播放性能和编辑效率。
*   **动画重定向 (Animation Retargeting)**: 支持动画在不同骨骼结构间的重定向，提高动画资产的复用性。

### 2. 绑定工具 (Rigging Tools) - `rigTools/`
*   **高级角色绑定系统 (Advanced Character Rigging System)**: `MHC/` 模块专注于DNA数据处理、BlendShape驱动、LOD管理和网格匹配，支持复杂角色绑定，实现高精度形变。
*   **蒙皮与权重管理 (Skinning & Weight Management)**: 提供快速蒙皮（`Quick_skin.py`）和蒙皮权重复制（`copySkinWeight/`）等功能，简化蒙皮流程，确保权重分配的准确性。
*   **骨骼与约束操作 (Joint & Constraint Operations)**: 包含重建骨骼层级、重建约束、关节转换等基础骨骼操作，以及属性集函数、通道盒颜色等辅助功能。
* 
