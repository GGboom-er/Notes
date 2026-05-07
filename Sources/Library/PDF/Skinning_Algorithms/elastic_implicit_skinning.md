---
tags: [pdf, Skinning_Algorithms]
---

# 📄 elastic_implicit_skinning.pdf

> **一句话总结**：弹性隐式蒙皮（改进版）

## 🔗 本地文件
- [elastic_implicit_skinning.pdf](file:///Y:/GGbommer/Lib/PDF/elastic_implicit_skinning.pdf)
- **文件名称**：elastic_implicit_skinning.pdf
- **资源类型**：pdf
- **归属分类**：蒙皮算法（学术论文）
- **本地路径**：[[elastic_implicit_skinning.pdf]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 PDF 提取内容

**前言/导读**:
Robust Iso-Surface Tracking for Interactive Character Skinning
Rodolphe Vaillant1,2, Ga¨el Guennebaud3, Lo¨ıc Barthe1, Brian Wyvill2, Marie-Paule Cani4
1IRIT - Universit´e de Toulouse, 2 University of Victoria, 3Inria - Univ. Bordeaux - IOGS - CNRS,
4 LJK univ. Grenoble-Alpes - Inria
(a)
(b)
(c)
(d)
(e)
Figure 1: (a) The Jeff model in rest pose. Its shoulders are rotated and skinned with (b) implicit skinning (by Vaillant et al. [2013]) which
locally deforms the mesh according to some preset weights and (c) our new technique which automatically produces a plausible skin elasticity
(notice how the belly button stretches). On the right, the Dana’s knee is bent with an extreme rotation angle. (d) Implicit Skinning fails to
handle deep self-intersections while (e) our technique allows large bending angles and the self-intersection at the knee is handled correctly.
Abstract
We present a novel approach to interactive character skinning,
which is robust to extreme character movements, handles skin con-
tacts and produces the effect of skin elasticity (sliding). Our ap-
proach builds on the idea of implicit skinning in which the character
is approximated by a 3D scalar ﬁeld and mesh-vertices are appro-
priately re-projected. Instead of being bound by an initial skinning
solution used to initialize the shape at each time step, we use the
skin mesh to directly track iso-surfaces of the ﬁeld over time. Tech-
nical problems are two-fold: ﬁrstly, all contact surfaces generated
between skin parts should be captured as iso-surfaces of the implicit
ﬁeld; secondly, the tracking method should capture elastic skin ef-
fects when the joints bend, and as the character returns to its rest
shape, so the skin must follow. Our solutions include: new com-
position operators enabling blending effects and local self-contact
between implicit surfaces, as well as a tangential relaxation scheme
derived from the as-rigid-as possible energy to solve the tracking
problem.
CR Categories:
I.3.7 [Compu
... (截断)