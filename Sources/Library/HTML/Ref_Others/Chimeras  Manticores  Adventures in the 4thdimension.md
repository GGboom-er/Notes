---
tags: [html, Ref_Others]
---

# 🌐 Chimeras & Manticores – Adventures in the 4th dimension.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Chimeras & Manticores – Adventures in the 4th dimension.html](file:///Y:/GGbommer/Lib/Http/Chimeras%20&%20Manticores%20–%20Adventures%20in%20the%204th dimension.html)
- **文件名称**：Chimeras & Manticores – Adventures in the 4th dimension.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[Chimeras & Manticores – Adventures in the 4th dimension.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Chimeras & Manticores – Adventures in the 4th dimension

## Chimeras & Manticores

[![](https://theodox.github.io/theme/img/profile.png)](https://theodox.github.io)

# 

a blog about technical art, python, the games business, and obscurantism

# Adventures in the 4th dimension

Posted on Mon 15 December 2014 in [blog](https://theodox.github.io/category/blog.html)

In [our last discussion of 3d math](dot_matrix), we started to plumb the mysteries of the matrix. Along the way we discovered two important facts: First, that it’s possible to write an article about matrices with only the merest smidge of a Keanu Reeves mention and second (almost as important), that **matrices are just a convention for applying dot products in series.** We walked through the derivation of matrices for a series of dot products and shows how hat simple operation allows you to do rotations in two and three dimensions.

Naturally, any TA reading this will be knows there’s more. We all know that the matrices we’re most familiar with — the transform matrices that drive animation and modeling — do more than rotate. So this this time out we’re going talk about how **translation** — spatial offsets — can be packed into matrices. And we’re going to do it in a truly brain bending way. Sort of.

> > *If none of this sounds familiar, you may want to return to the [previous post in the series](dot_matrix) before continuing.*

After all of the time we’ve spent with dot products in this series, one thing we should remember is that dots are **additive** — if you dot two vectors, you sum up all of the products. “Additive” is a nice quality to have if we’re thinking about adding translations to our matrices It suggests that maybe we can use the additive-ness of dot products to teach our matrices how to do translations as well as rotations.

Multiplying a vector against a matrix, [you’ll recall](dot_matrix.html), is nothing more than stringing together a set of dot products between the vector and the columns of the matrix. So, putting together the fact that dots are additive and the fact that matrix multiplication uses dots, it seems logical that we can just stick our translation right onto the bottom of the matrix. By dropping it down at the end of the matrix columns, we’ll add it add it to our results. One important side effect that we’ll have to worry about is that this will break the pretty symmetry we noted last time whereby every matrix row is an axis in the matrix’s local coordinate system. However we’ll deal with that after we know it works.

To keep things simple, let’s start with a rotate matrix that doesn’t do any, you know, *rotating* — a matrix that works but leaves incoming data unchanged. That’ll make it easier to see when our translations kick in. The correct math moniker for this do-nothing matrix is an *identity* matrix (as in the otherwise-inexplicable `MakeIdentity()` command in Maya) and it’s just a set of rows that match the default XYZ axes:

| | |
|—-|—-|—-|   
1| 0| 0  
0| 1| 0  
0| 0| 1

I won’t bother with the math here, but if your work it out for yourself you’ll quickly see that dotting the columns of this matrix in turn against any vector returns the original vector unchanged.

Next, we’d like to add some extra information to this matrix to include a translation. Since we know our dots are going down the columns, if we tack on an extra row we should be getting a new value added to the output: hopefully, the translation we want. Adding an extra row for translation gives us a 4X3 matrix like this (with an example translation of `[1,2,3]` :

| | |
|—-|—-|—-|
1| 0| 0  
0| 1| 0  
0| 0| 1  
1| 2| 3

> *For future reference, matrices are usually described as ‘rows by columns’; in the last article we derived our matrix first as a 2X2 then as a 3X3 matrx. Most transformation matrices in 3d software are 4X4, for reasons that will become apparent shortly, but Max users will find this 4X3 format familiar — Maxscript makes extensive use of 4x3 matrices for object transforms.*

So now we’ve got a test matrix that should offset our initial value by `[1,2,3]`. However, we immediately run into a problem: as we try to multiply our vector against this matrix. The columns now have 4 items but our vector only has 3. How can we sum up? Dot products require that both vectors being dotted have the same number of products, as you can see here:

```
[1,1,1] dot [1,0,0,1] = (1 * 1) + (1 * 0) + (1 * 0) + (??? * 1)
```

To make this work, we are going to need to extend our vector to grab the translation values from the new matrix row. It needs to become a 4-dimensional vector. *The fourth dimension! Trippy! Cue [theremin music](https://www.youtube.com/watch?v=4wQsWL-lMJw)….*

We’ve actually dimension jumped before, while working through rotation matrices. We could borrow the same tactic we used in the last post when we moved from a 2-D matrix to a 3-D matrix by just taking on a zero to our vector. This seems like a natural idea, since we know that t

... (原文过长，已截断)