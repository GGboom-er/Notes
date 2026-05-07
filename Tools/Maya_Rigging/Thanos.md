---
tags: [Maya_Rigging, Pipeline_General, tool]
tech_stack: [Python]
---
# 🛠️ Thanos
> **A standalone tool shelf application that can send code to Maya, Blender, and Unreal Engine.**

- 📂 [Thanos](file:///Y:/GGbommer/scripts/Thanos)

## 💡 详细说明
# Thanos - Cross DCC Unified Tool Shelf

A standalone tool shelf application that can send code to Maya, Blender, and Unreal Engine.

## Features (Phase 1)

- Independent Windows application (PySide6)
- Connect to Maya via commandPort
- Send Python code for execution
- Receive execution results
- Configurable tool buttons via JSON

## Installation

### 1. Install Python Dependencies

```bash
cd Y:\GGbommer\scripts\Thanos
pip install -r requirements.txt
```

### 2. Setup Maya Server

Option A: Add to userSetup.py
```python
import sys
sys.path.insert(0, r"Y:\GGbommer\scripts\Thanos\dcc_plugins\maya")
import maya.cmds as cmds
cmds.evalDeferred("import thanos_server; thanos_server.start()")
```

Option B: Run manually in Maya Script Editor
```python
import sys
sys.path.insert(0, r"Y:\GGbommer\scripts\Thanos\dcc_plugins\maya")
import thanos_server
thanos_server.start()
```

### 3. Run Thanos

```bash
python Y:\GGbommer\scripts\Thanos\main.py
```

## Usage

1. Start Maya with Thanos server e
