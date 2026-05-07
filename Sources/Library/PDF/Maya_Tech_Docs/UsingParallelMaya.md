---
tags: [pdf, Maya_Tech_Docs]
---

# 📄 UsingParallelMaya.pdf

> **一句话总结**：Maya 并行求值机制官方指南

## 🔗 本地文件
- [UsingParallelMaya.pdf](file:///Y:/GGbommer/Lib/PDF/UsingParallelMaya.pdf)
- **文件名称**：UsingParallelMaya.pdf
- **资源类型**：pdf
- **归属分类**：Maya 技术文档
- **本地路径**：[[UsingParallelMaya.pdf]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 PDF 提取内容

**文档目录**:
- Overview (p.5)
- Key Concepts (p.5)
- Supported Evaluation Modes (p.6)
- First Make it Right Then Make it Fast (p.7)
  - Evaluation Graph Correctness (p.7)
  - Thread Safety (p.8)
  - Safe Mode (p.10)
- Evaluation Graph Invalidation (p.11)
- Custom Evaluators (p.12)
  - GPU Override (p.13)
  - Dynamics Evaluator (p.15)
  - Reference Evaluator (p.17)
  - Invisibility Evaluator (p.18)
  - Frozen Evaluator (p.19)
    - The Frozen Attribute (p.19)
    - Operation (p.20)
    - Setting Options (p.21)
    - Limitations (p.22)
  - Other Evaluators (p.22)
  - Evaluator Conflicts (p.23)
- ... (余下目录省略)

**前言/导读**:
Using Parallel Maya
2018

Using Parallel Maya
Contents
Contents
Overview
4
Key Concepts
4
Supported EvaluaƟon Modes
5
First Make it Right Then Make it Fast
6
EvaluaƟon Graph Correctness
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
Thread Safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
Safe Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
EvaluaƟon Graph InvalidaƟon
10
Custom Evaluators
11
GPU Override . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
Dynamics Evaluator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
Reference Evaluator
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
Invisibility Evaluator
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
Frozen Evaluator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
The Frozen AƩribute
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
OperaƟon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
Seƫng OpƟons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
LimitaƟons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
Other Evaluators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
Evaluator Conﬂicts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
API Extensions
22
Parallel EvaluaƟon
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
Custom GPU Deformers
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
Custom Evaluator API . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
The Basics
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
2018
1