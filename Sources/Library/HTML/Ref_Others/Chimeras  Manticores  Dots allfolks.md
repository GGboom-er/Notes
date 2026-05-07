---
tags: [html, Ref_Others]
---

# 🌐 Chimeras & Manticores – Dot’s all, folks.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Chimeras & Manticores – Dot’s all, folks.html](file:///Y:/GGbommer/Lib/Http/Chimeras%20&%20Manticores%20–%20Dot’s%20all, folks.html)
- **文件名称**：Chimeras & Manticores – Dot’s all, folks.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[Chimeras & Manticores – Dot’s all, folks.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Chimeras & Manticores – Dot’s all, folks

## Chimeras & Manticores

[![](https://theodox.github.io/theme/img/profile.png)](https://theodox.github.io)

# 

a blog about technical art, python, the games business, and obscurantism

# Dot’s all, folks

Posted on Sat 29 November 2014 in [blog](https://theodox.github.io/category/blog.html)

Last time out I went on (probably a bit too long) on the virtues of the dot product - the operation which takes two lists of numbers and multiplies them to create a single product. The highlight of the whole thing was the *cosine dot product* - the handy fact that the dot product of two normalized vectors is the cosine of the angle between them.

Now that the theory is out of the way, it’s time to highlight some of the zillions of applications for this handy little operation.

> If none of this sounds familiar you might want to [revisit the first post in the series](bagels_and_coffee.html) before continuing.

The dot product is incredibly useful for a TA for two reasons. First, dots allow you to *convert between geometric measures and angles* without the need for matrices or complex formulae. Second, dots provide an efficient way to *project one vector on to another*, allowing you to measure distances and quantities relative to an arbitrary axis or vector - a great tool for anything from color conversions in a pixel shader to measuring motion in a complex rig.  
Before getting down to cases, a quick reminder of one important side fact we pointed out last time. A cosine dot product can only tell you *how different* the angle between two vectors is - **not** what rotations would transform one vector into the other. If you try out this example you’ll see that the dot of `[1,0,0]` against both `[.5, .866, 0]` and `[.5, -.866, 0]` is .5, which (if you remember your sines and cosines) means the relative angle is 30 degrees. However one of those two vectors is clockwise from `[1,0,0]` and the other is counter-clockwise from it. The dot, by itself, can’t tell you which one is which. *Don’t forget that bit!*

> As I mentioned in the last article, the math for dots is trivially simple. Maxscript [includes vector math functions](http://www.scriptspot.com/bobo/mel2mxs/arithmetic.htm) by default, as does MEL, but vanilla maya.cmds does not. If you want to experiment with examples mentioned here in Maya python, you can import `pymel.core.datataypes` and use the `Vector`. I’ve also put a [simple vector module up on Github](https://github.com/theodox/vector) that works in `Maya.cmds`. I’ll be using that for these examples but translating between MXS, Pymel, and cmds should be a no-brainer.

## Rigging

One of the most common tasks in rigging is wrangling information into the correct frame of reference.This is particularly tough when dealing with angular data, since angles are often presented in the form of Euler angles whose numeric values can vary unpredictably and which are therefore hard to use in expressions or code. Here are a few examples of how dot’s can help riggers get angular information while avoiding the Euler blues

#### The Bends

Dot’s are an excellent way to measure the extension of a limb, without relying on an Euler value which might be affected by local axis orientations, joint orients, or rotated local axes. Here’s an example that gets a reliable value for the extension of an arm (note: this is vanilla maya, you could do it more succintly with Pymel but it’s a better illustration to do it from scratch)

```
shoulder_pos = cmds.xform('r_shoulder', t=True, w=True)  
elbow_pos = cmds.xform('r_elbow', t=True, w=True)  
wrist_pos = cmds.xform('r_wrist', t=True, w=True)

bicep_vector = (Vector3(*elbow_pos) - Vector3(*shoulder_pos)).normalized()  
forearm_vector = (Vector3(*wrist_pos) - Vector3(*elbow_pos)).normalized()  
elbow_bend = Vector3.dot(bicep_vector, forearm_vector)
```

then `arm_extension` will be 1 at full extension and 0 when the arm is bent back completely on itself (*ouch!*). You can map use this extension value to drive muscle deformations, blendshapes, or other behaviors without worrying about th underlying Euler values or converting from angles to linear ranges.

#### Leaning In

It’s often useful to have a general idea what a character’s whole body is doing, rather than focusing entirely on individual joint positions and orientations. For example, you might want to have rig behaviors turn on when a character is ‘upright’ and off when it it is ‘prone’, or vice-versa. Figuring out the gross orientation is often hard because there are so many bones cooperating to produce the visual effect – and because different animators may use different controls in different ways: animator A may prefer to put all of the big rotations onto a center-of-gravity control while animator B does everything on the pelvis.

Dots are great for extracting pose info from the world space position of key bones instead of trying to intuit them from rotation values. For example:

```
head_pos 

... (原文过长，已截断)