---
tags: [Maya_Animation, Maya_Rigging, tool]
tech_stack: [C++, Python]
---
# 🛠️ adPose
> ****adPose** 是一个为专业角色绑定师（Rigger）和技术美术（Technical Artist）设计的高级姿态与BlendShape管理工具集。它以Autodesk Maya为核心平台，深度优化了角色姿态的创建、编辑和管理流程，并提供了强大的跨平台数据同步功能，支持将BlendShape数据无缝迁移至3ds Max、Unreal Engine和Unity。**

- 📂 [adPose](file:///Y:/GGbommer/scripts/adPose)

## 💡 详细说明
# adPose 工具集

## 1. 概述

**adPose** 是一个为专业角色绑定师（Rigger）和技术美术（Technical Artist）设计的高级姿态与BlendShape管理工具集。它以Autodesk Maya为核心平台，深度优化了角色姿态的创建、编辑和管理流程，并提供了强大的跨平台数据同步功能，支持将BlendShape数据无缝迁移至3ds Max、Unreal Engine和Unity。

该工具集的核心优势在于其高性能的C++插件和灵活的模块化架构，旨在解决现代角色工作流中常见的效率瓶颈和数据一致性问题。

## 2. 核心功能

- **强大的姿态库UI**:
  - 在Maya中提供了一个直观的图形界面，用于管理所有姿态（Pose Targets）。
  - 支持对姿态进行快速的**添加、编辑、镜像、复制和删除**操作。
  - 姿态被分为`Swing`（大范围运动）和`Twist`（扭转修复）两种类型，便于精细化管理。

- **高性能BlendShape节点操作**:
  - 内置一个名为 `bs_api` 的C++ Maya插件，用于加速BlendShape相关的计算。
  - 利用Intel TBB进行多线程处理，极大地提升了在高精度模型上进行顶点数据读写、镜像和反转��操作的性能。
  - 支持通过JSON格式对BlendShape数据进行**导入和导出**，便于数据备份和迁移。

- **跨平台工作流**:
  - **Maya -> 3ds Max**: 同步BlendShape数据，确保在两个DCC软件中形变效果一致。
  - **Maya -> Unreal Engine**: 提供`ad_pose_ue_bs_sdk`，将Maya中的姿态和表情直接与UE中的模型关联。
  - **Maya -> Unity**: 包含`LushDrive`等C#脚本，用于在Unity中驱动和加载由adPose创建的BlendShape数据。

- **灵活的命名配置**:
  - 通过`data/config.json`文件，用户可以自定义骨骼、控制器和左右侧的命名规则。
  - 工具能够自动识别和匹配不同项目中的命名规范，无需修改代码。

## 3. 模块结构

- **`adPose/`**: 项目主目录。
  - **`ma
