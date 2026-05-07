---
tags: [pdf, Skinning_Algorithms]
---

# 📄 elasticSkinning.pdf

> **一句话总结**：Elastic Implicit Skinning（弹性蒙皮）

## 🔗 本地文件
- [elasticSkinning.pdf](file:///Y:/GGbommer/Lib/PDF/elasticSkinning.pdf)
- **文件名称**：elasticSkinning.pdf
- **资源类型**：pdf
- **归属分类**：蒙皮算法（学术论文）
- **本地路径**：[[elasticSkinning.pdf]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 PDF 提取内容

**前言/导读**:
Efﬁcient elasticity for character skinning with contact and collisions
Aleka McAdams1,3
Yongning Zhu2
Andrew Selle1
Mark Empey1
Rasmus Tamstorf1
Joseph Teran3,1
Eftychios Sifakis4,1
1 Walt Disney Animation Studios
2 PDI/DreamWorks
3 University of California, Los Angeles
4 University of Wisconsin, Madison
Figure 1: Our method takes a geometric internal skeleton (left) and a source surface mesh (not pictured) as input. Based on a hexahedral
lattice (center) it then simulates a deformed surface (right) obeying self-collision and volumetric elasticity. The example shown here has
106,567 cells and simulates at 5.5 seconds per frame. c⃝Disney Enterprises, Inc.
Abstract
We present a new algorithm for near-interactive simulation of skele-
ton driven, high resolution elasticity models. Our methodology is
used for soft tissue deformation in character animation. The al-
gorithm is based on a novel discretization of corotational elastic-
ity over a hexahedral lattice. Within this framework we enforce
positive deﬁniteness of the stiffness matrix to allow efﬁcient qua-
sistatics and dynamics. In addition, we present a multigrid method
that converges with very high efﬁciency. Our design targets perfor-
mance through parallelism using a fully vectorized and branch-free
SVD algorithm as well as a stable one-point quadrature scheme.
Since body collisions, self collisions and soft-constraints are nec-
essary for real-world examples, we present a simple framework for
enforcing them. The whole approach is demonstrated in an end-to-
end production-level character skinning system.
CR Categories:
I.6.8 [Simulation and Modeling]: Types of
Simulation—Animation
Keywords:
skinning, corotated elasticity, physics-based model-
ing, elastic deformations
Links:
DL
PDF
WEB
1
Introduction
Creating appealing characters is essential for feature animation.
One challenging aspect is the production of life-like deformations
for soft tissues comprising both humans and animals. In order to
provide the neces
... (截断)