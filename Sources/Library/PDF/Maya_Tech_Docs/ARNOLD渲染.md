---
tags: [pdf, Maya_Tech_Docs]
---

# 📄 ARNOLD渲染.pdf

> **一句话总结**：Arnold 渲染器使用手册

## 🔗 本地文件
- [ARNOLD渲染.pdf](file:///Y:/GGbommer/Lib/PDF/ARNOLD渲染.pdf)
- **文件名称**：ARNOLD渲染.pdf
- **资源类型**：pdf
- **归属分类**：Maya 技术文档
- **本地路径**：[[ARNOLD渲染.pdf]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 PDF 提取内容

**前言/导读**:
基础
镜面
传输
地下的
外套
光泽
发光
薄膜
几何图形
不光滑的
AOV 
先进的
硬件纹理
金属各向异性：
必须使用UV集展好UV；
①　Rampfloat （使用UC集）先线性旋转→
rotation
②　Rampfloat径向旋转需先分色并反向→
anisotropy
③　粗糙度→（mask）colorcorrect（R）
→huess
拉丝金属不可添加Uv集名称；
④　Rampfloat+floattorgba→（P）
cellnoise→（map）bump2D（noaml）
⑤　划痕file→range→（mu）
colorcorrect，使用bump2D控制高度。