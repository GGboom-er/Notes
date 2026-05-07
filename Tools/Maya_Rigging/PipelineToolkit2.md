---
tags: [Maya_Rigging, Pipeline_General, tool]
tech_stack: [MEL, Python]
---
# 🛠️ PipelineToolkit2
> **`PipelineToolkit2` 是一套面向CG动画、VFX项目制作的综合型管线工具集。它通过高度模块化的目录结构与脚本组织，实现从资产管理、流程集成、自动化检查、渲染调度到常用艺术工具插件的全流程覆盖，支持Maya、Blender、Nuke、Photoshop等主流DCC软件，赋能团队日常生产协作提效与质量保证。**

- 📂 [PipelineToolkit2](file:///Y:/GGbommer/scripts/PipelineToolkit2)

## 💡 详细说明
# PipelineToolkit2 项目介绍

## 一、项目概述

`PipelineToolkit2` 是一套面向CG动画、VFX项目制作的综合型管线工具集。它通过高度模块化的目录结构与脚本组织，实现从资产管理、流程集成、自动化检查、渲染调度到常用艺术工具插件的全流程覆盖，支持Maya、Blender、Nuke、Photoshop等主流DCC软件，赋能团队日常生产协作提效与质量保证。

## 二、顶层目录结构说明

```
.
├── config/       # 配置文件，存放环境、流程、UI等参数设定
├── files/        # 主要为资产资源包（如CameraRigs/GeneralRigs等）
├── icons/        # 工具UI及功能按钮的icon美术资源
├── plug-ins/     # 外部插件与扩展（如SLiB材质库等）
├── scripts/
│   ├── mel/         # 各DCC的MEL脚本，分动画/灯光/建模/渲染等
│   ├── python/      # 主力pipeline脚本库，按功能深度细分模块
│   └── ...          # 其他辅助脚本或工程化工具
```

## 三、主要功能模块详解

> [提示] 子目录详细结构极为庞大，以下仅列举主干与特色功能板块，便于理解全局协同和代码定位。

- **python/core/**
  - pipeline核心工具、基类与通用函数，实现流程复用与底层集成。
- **python/pipeline/**
  - 流水线主干控制模块，负责生产业务流转、节点组织、数据驱动等。
- **python/library/** & **libraryItems/**
  - 资产（模型/贴图/道具等）库托管、检索、复用及团队共享机制。
- **python/tools/**
  - 生产环节专项工具集，涵盖：
    - animation、bake、playblast等动画批处理
    - lighting视觉检查/自动比对/资产批量处理
    - check品质自检、自动化清理、合规检测
    - 特殊定制工具（如gadget、generals、manager等）
    - 跨软件支持（blenderApp、photo
