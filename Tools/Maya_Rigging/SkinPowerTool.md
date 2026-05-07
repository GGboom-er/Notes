---
tags: [tool, Maya_Rigging]
---
# 🛠️ SkinPowerTool
> **[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)**

- 📂 [SkinPowerTool](file:///Y:/GGbommer/scripts/SkinPowerTool)

## 💡 详细说明
# SkinPowerTool
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)

![Image of SkinPowerTool Interface](img/001.jpg)


As a replacement tool for the SkinMagic plugin for Maya versions prior to 2022, it has been rewritten using Python 3.



## Improvements and Differences Compared to Skin Magic

- All operations are based on Maya's vertex editing mode.
- Supports Maya versions 2023 and above.
(Maya 2022 can still use Skin Magic with Python 2)
- Object-oriented design, scripts are categorized by functionality.
- Integrated UI, reducing the need to open additional windows, and providing a .ui file for easy modification.
- Simplified UI, eliminating buttons that are rarely used in practice.
- Smooth algorithm now uses Maya's default functions.
- Provides functionality to remove trailing decimal places.

## Installation

```python
import sys

modules_path = r"D:\\your\\path\\SkinPowerTool"
sys.path.a
