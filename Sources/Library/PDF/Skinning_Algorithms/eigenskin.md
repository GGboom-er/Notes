---
tags: [pdf, Skinning_Algorithms]
---

# 📄 eigenskin.pdf

> **一句话总结**：EigenSkin 基于PCA的实时蒙皮

## 🔗 本地文件
- [eigenskin.pdf](file:///Y:/GGbommer/Lib/PDF/eigenskin.pdf)
- **文件名称**：eigenskin.pdf
- **资源类型**：pdf
- **归属分类**：蒙皮算法（学术论文）
- **本地路径**：[[eigenskin.pdf]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 PDF 提取内容

**前言/导读**:
EigenSkin: Real Time Large Deformation Character Skinning in Hardware
Paul G. Kry, Doug L. James, and Dinesh K. Pai
University of British Columbia
{pgkry|djames|pai}@cs.ubc.ca
a) FEM simulated pose
b) SSD only
c) EigenSkin
d) Real time hardware simulation
Figure 1: Comparison of EigenSkin and Skeletal-Subspace Deformation for an extreme pose not in the training data. Note signiﬁcant dif-
ferences in the thumb between a) the new pose computed from our ﬁnite element hand model, b) skeletal-subspace deformation
only, and c) EigenSkin with one eigendisplacements and one normal correction per support. Figure d) shows our EigenSkin
hand example being animated using a CyberGlove. The hand model shown here consists of 55,904 triangles and is drawn using
display lists with a GeForce3 vertex program.
Abstract
We present a technique which allows subtle nonlinear quasi-static
deformations of articulated characters to be compactly approxi-
mated by data-dependent eigenbases which are optimized for real
time rendering on commodity graphics hardware.
The method
extends the common Skeletal-Subspace Deformation (SSD) tech-
nique to provide efﬁcient approximations of the complex deforma-
tion behaviours exhibited in simulated, measured, and artist-drawn
characters. Instead of storing displacements for key poses (which
may be numerous), we precompute principal components of the de-
formation inﬂuences for individual kinematic joints, and so con-
struct error-optimal eigenbases describing each joint’s deformation
subspace. Pose-dependent deformations are then expressed in terms
of these reduced eigenbases, allowing precomputed coefﬁcients of
the eigenbasis to be interpolated at run time. Vertex program hard-
ware can then efﬁciently render nonlinear skin deformations using
a small number of eigendisplacements stored in graphics hardware.
We refer to the ﬁnal resulting character skinning construct as the
model’s EigenSkin. Animation results are presented for a very large
nonlinear ﬁnite
... (截断)