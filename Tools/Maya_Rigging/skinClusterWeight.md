---
tags: [tool, Maya_Rigging]
---
# 🛠️ skinClusterWeight
> **SkinCluster权重导入/导出工具，支持Maya 2018-2025所有版本。**

- 📂 [skinClusterWeight](file:///Y:/GGbommer/scripts/skinClusterWeight)

## 💡 详细说明
# SkinClusterWeight 工具 - Python 2/3 兼容版

## 简介
SkinCluster权重导入/导出工具，支持Maya 2018-2025所有版本。

## 版本
**v3.0** - Python 2/3 兼容版本

## 支持的Maya版本
- Maya 2018 - 2019 (Python 2.7)
- Maya 2020 - 2021 (Python 2.7 / 3.7)
- Maya 2022 (Python 3.7)
- Maya 2023 (Python 3.9)
- Maya 2024 (Python 3.10)
- Maya 2025 (Python 3.11)

## 功能特性
- ✅ 导出/导入 Mesh 皮肤权重
- ✅ 导出/导入 NurbsCurve 皮肤权重
- ✅ 导出/导入 NurbsSurface 皮肤权重
- ✅ 导出/导入 Lattice 皮肤权重
- ✅ 批量导出/导入权重
- ✅ 权重分割（左右对称）
- ✅ 重置绑定姿势
- ✅ 选择影响骨骼

## 安装方法

### 1. 复制文件
将整个 `skinClusterWeight` 文件夹复制到Maya scripts目录：

**Windows:**
```
C:\Users\<你的用户名>\Documents\maya\scripts\
```

**Mac:**
```
~/Library/Preferences/Autodesk/maya/scripts/
```

**Linux:**
```
~/maya/scripts/
```

### 2. 启动工具
在Maya的Python脚本编辑器中执行：
```python
import rig_ch.skinClusterWeight as skWt
skWt.win()
```

### 3. 创建工具架按钮（可选）
将上面的代码添加到Maya工具架按钮中，方便快速访问。

## 使用说明

### 导出权重
1. 选择要导出的模型或顶点
2. 点击 "Export SkinWeight" 按钮
3. 选择保存路径和文件名
4. 权重将保存为 `.w` 文件

### 导入权重
1. 选择要导入权重的模型
2. 点击 "Import SkinWeight" 按钮
3. 选择之前
