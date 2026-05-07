---
tags: [pdf, Skinning_Algorithms]
---

# 📄 preprint.pdf

> **一句话总结**：蒙皮预印本论文

## 🔗 本地文件
- [preprint.pdf](file:///Y:/GGbommer/Lib/PDF/preprint.pdf)
- **文件名称**：preprint.pdf
- **资源类型**：pdf
- **归属分类**：蒙皮算法（学术论文）
- **本地路径**：[[preprint.pdf]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 PDF 提取内容

**文档目录**:
- Abstract (p.1)
- 1 Introduction (p.2)
- 2 Related Work (p.2)
- 3 Method (p.2)
  - 3.1 Closest Point Matching (p.2)
  - 3.2 Skinning Weights Inpainting (p.3)
  - 3.3 Implementation (p.3)
  - 3.4 Artist-Control (p.3)
- 4 Results (p.3)
- 5 Limitations and Future Work (p.4)
- 6 Conclusion (p.4)
- References (p.4)

**前言/导读**:
Robust Skin Weights Transfer via Weight Inpainting
Rinat Abdrashitov
Epic Games
Canada
rinat.abdrashitov@epicgames.com
Kim Raichstat
Epic Games
USA
kim.raichstat@epicgames.com
Jared Monsen
Epic Games
USA
jared.monsen@epicgames.com
David Hill
Epic Games
USA
david.hill@epicgames.com
b
a
d
g
f
e
c
baseline
our method
Figure 1: Skin weights are transferred from a rigged body to a t-shirt and pants (a). Current production methods fail to produce
ready-to-use assets (b). Upon closer inspection, areas around the armpits (c), the crotch, and lower legs (d) are skinned incorrectly.
In contrast, our method (e) does not suffer from the same issues (f, g). 3D models are the property of Epic Games, Inc., used
with permission.
ABSTRACT
We present a new method for the robust transfer of skin weights
from a source mesh to a target mesh with significantly different
geometric shapes. Rigging garments is a typical application of skin
weight transfer where weights are copied from a source body mesh
to avoid tedious weight painting from scratch. However, existing
techniques struggle with non-skin-tight garments and require ad-
ditional manual weight painting. We introduce a fully automatic
two-stage skin weight transfer process. First, an initial transfer
is performed by copying weights from the source mesh only for
those vertices on the target mesh where we have high confidence
in obtaining the ground truth weights from the source. Then, we
SA Technical Communications ’23, December 12–15, 2023, Sydney, NSW, Australia
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
This is the author’s version of the work. It is posted here for your personal use. Not
for redistribution. The definitive Version of Record was published in SIGGRAPH Asia
2023 Technical Communications (SA Technical Communications ’23), December 12–15,
2023, Sydney, NSW, Australia, https://doi.org/10.1145/3610543.3626180.
automatically compute weights for all other vertices by interpolat-
ing 
... (截断)