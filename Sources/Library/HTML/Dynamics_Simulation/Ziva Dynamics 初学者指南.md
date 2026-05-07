---
tags: [html, Dynamics_Simulation]
---

# 🌐 Ziva Dynamics 初学者指南.html

> **一句话总结**：Ziva 官方入门教程（中文）

## 🔗 本地文件
- [Ziva Dynamics 初学者指南.html](file:///Y:/GGbommer/Lib/Http/Ziva%20Dynamics%20初学者指南.html)
- **文件名称**：Ziva Dynamics 初学者指南.html
- **资源类型**：html
- **归属分类**：Dynamics_Simulation
- **本地路径**：[[Ziva Dynamics 初学者指南.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

A Beginners Guide to Ziva Dynamics

![](https://www.facebook.com/tr?id=735981606527756&ev=PageView&noscript=1)

Search

![A Beginners Guide to Ziva Dynamics](/content/images/size/w1000/2020/07/Hero.jpg)

[Learning](/tag/learning/)

# A Beginners Guide to Ziva Dynamics

Create a new Maya scene, import the alembic cache of the skeleton and the muscles simulated, and the fat mesh.

* [![Benjamin Makki](/content/images/size/w100/2020/08/SHF_0572.jpg)](/author/benjamin/)

#### [Benjamin Makki](/author/benjamin/)

Aug 2, 2020
• 12 min read

Round of applause for our sponsors

This is a great article for anybody wanting to take their characters to the next level with sophisticated muscle sims. This same muscle system were used in movies like The Lion King.  Benjamin Makki give us a step by step on how he used [Ziva Dynamics](https://zivadynamics.com/?ref=discover-the-rookies) on a personal project to simulate the muscles, fat, and skin of a cat.

---

## Getting your model ready for Ziva

If you're not interested by the modelling part you can download one of the [free assets](https://zivadynamics.com/promos/free?ref=discover-the-rookies) Ziva provides on their website. In my case I did the modelling of the asset myself.

I started to sculpt the skeleton in [Zbrush](https://pixologic.com/?ref=discover-the-rookies). The topology of the bones is not that important, just keep it low poly for the export to [Maya](https://www.autodesk.com/?ref=discover-the-rookies). No need to do any complex handmade retopology, the ZRemesher does the job. Don’t forget to unfold the UVs, you will need it later in Ziva, but again you don't need anything complexe. I unfolded them in [Zbrush](https://pixologic.com/?ref=discover-the-rookies) with the Unwrap tool, and then organised them in 4 UV sets in [Maya](https://www.autodesk.com/?ref=discover-the-rookies) to keep it clean.

![](https://discover.therookies.co/content/images/2020/07/Skeleton_Inline.jpg)

Now let’s do the muscles, it might be the most demanding part of the modelling. You want to have as little interpenetrations between the muscles as possible. Otherwise it might cause abnormal behaviour at the simulation stage. If you find out about some interpenetrations when you are already doing the simulation, that’s okay. You will still be able to go back to [Zbrush](https://pixologic.com/?ref=discover-the-rookies), do some retakes, then re-export your meshes to [Maya](https://www.autodesk.com/?ref=discover-the-rookies) and pick up your simulation where you left off.

> *One thing you have to care about is that you need to have your neutral pose like 10 frames before the animation begins.*

It’s a non-destructive workflow so don’t be afraid to do some mistakes. You will want the muscles edge flow to go in the same direction as the muscle movements. (Like for the bones, ZRemesher might also be enough to get this done). This will help you to get a nice simulation with fewer polygons.

Speaking of polygons, you need to know that the more polys you have on your simulated meshes, the more folds you will be able to get. That said, you don’t really need folds on muscles so you might be able to get the result you are looking for by keeping them quite lowpoly. The only muscle i exported with a higher polycount is the External Oblique so it can be moulded around the rib cage.

For the UVs I did the same thing as I did for the bones.

![](https://discover.therookies.co/content/images/2020/07/Muscles_Inline.jpg)

Done with the muscles, we can start the fat layer. This layer must cover all your muscles. Here is a small tip I found to have the base of the fat mesh : Duplicate all the muscles, merge them into one subtool, Dynamesh to make it a single mesh.

Then you can mask the outside of this mesh and extract it to create the fat subtool. Now you just need to do an extrude on the whole mesh to create the thickness and you have the basic shape of your fat layer. (You can delete the dynameshed muscles at this point). The topology isn’t really important again, ZRemesher will do the job well.

When you will export the fat mesh to [Maya](https://www.autodesk.com/?ref=discover-the-rookies) it needs to be quite highpoly to get folds when running the simulation, mine is about 140.000 faces. For the UVs I advise you to cut the inner side from the outside because at some point later in [Maya](https://www.autodesk.com/?ref=discover-the-rookies) you will need to select the inside vertices of this mesh, so you will be able to select them through the UVs.

![](https://discover.therookies.co/content/images/2020/07/Fat_Inline.jpg)

The next step is sculpting the skin, when the sculpt is done you will need to retopologize it by hand so it can be rigged and animated. Then you can unfold the UVs. Like the fat mesh, you need to export a highpoly to get folds, mine is about 300.000 faces.

![](https://discover.therookies.co/content/images/2020/07/Skin_Inline.jpg)

## Rigging and animation

At this point I asked my fr

... (原文过长，已截断)