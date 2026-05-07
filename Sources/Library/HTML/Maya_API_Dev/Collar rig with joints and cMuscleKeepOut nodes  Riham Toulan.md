---
tags: [html, Maya_API_Dev]
---

# 🌐 Collar rig with joints and cMuscleKeepOut nodes — Riham Toulan.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Collar rig with joints and cMuscleKeepOut nodes — Riham Toulan.html](file:///Y:/GGbommer/Lib/Http/Collar%20rig%20with%20joints%20and%20cMuscleKeepOut%20nodes%20—%20Riham%20Toulan.html)
- **文件名称**：Collar rig with joints and cMuscleKeepOut nodes — Riham Toulan.html
- **资源类型**：html
- **归属分类**：Maya API 开发
- **本地路径**：[[Collar rig with joints and cMuscleKeepOut nodes — Riham Toulan.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Collar rig with joints and cMuscleKeepOut nodes — Riham Toulan

Menu

# [Riham Toulan](/)

Character Technical Director

# [Collar rig with joints and cMuscleKeepOut nodes](/blog/2018/3/24/faking-collisions-with-joints-based-setup-8snd2)

April 26, 2018

Hi guys, almost a month ago I posted this rig test for a collsion setup I made for a character I was working on.

View fullsize

![neck_collision_512.gif](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524749144545-HRJIPT26ECUQRY85Z58H/neck_collision_512.gif)![neck_collision_512.gif]()

The rig is joints based, therefore would be suitable for game animations. I couldn't use the same asset but I created another one for the purposes of this tutorial.

A basic knowledge of maya and rigging in is required. This is not a rigging and rigging practices tutorial, it is made specifically to cover the technique of using cMuscleKeepOut nodes in Maya. So feel free to take it and conform it to whatever practices and naming conventions you normally use in your rigging process.

I will break this post into 3 main sections. The curve setup, the collision setup and the joints setup. But before we proceed this is how the rig should look like in the end.

---

## You can purchase the work files for $5 on [Gumroad](https://gum.co/PhhXO)

[![buygum5.png](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1525526821197-M8Y5NYJ8OOZ0ZI55OA32/buygum5.png)![buygum5.png]()](https://gum.co/PhhXO)

---

View fullsize

![neck_collision_570.gif](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524327141303-0LWNXXOE25JDJTTO4Z1K/neck_collision_570.gif)![neck_collision_570.gif]()

### Kiel Figgins kindly pointed out that the MayaMuscle plugin is not loaded by default in some cases so make sure you load the MayaMuscle.mll plugin in the Plug-in Manager.

View fullsize

![Loading the MayaMuscle plugin.](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524841988410-8P79XUJ7I1TAVYNKSN71/plugin.jpg)![Loading the MayaMuscle plugin.]()

Loading the MayaMuscle plugin.

---

# **The Curve Setup**

**1 -** Create a nurbs circle with 8 spans and name it "collar\_crv".

View fullsize

![Creating a nurbs Curve.](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1522000100397-YEK7SRKRCEE8BA30AAAN/nurbsCurve_create.jpg)![Creating a nurbs Curve.]()

Creating a nurbs Curve.

View fullsize

![Nurbs Circle options](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1522011831546-FJOPLOK12UEPMFO02TVU/cirxcleAbstract.jpg)![Nurbs Circle options]()

Nurbs Circle options

**2 -** Shape the curve along th einside o the collar. The curve vertices are the points of contact with our collision mesh so make sure they are placed where you would want the collision to happen.

View fullsize

![Curve placement. The head is hidden for clarity purposes.](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1523297325347-TNQXUQ46BG78GKQES8A9/curvePlacement.jpg)![Curve placement. The head is hidden for clarity purposes.]()

Curve placement. The head is hidden for clarity purposes.

**3 -** Create a cluster for every vertix of the "collar\_crv". In the riggging tab go to Deform>Cluster.

View fullsize

![Creating clusters](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1523303647234-5KNV391BNY5BNHJC2LX3/clusters.jpg)![Creating clusters]()

Creating clusters

**4 -** We need an offset group for each cluster. Press **CTRL+G** the short cut for creating an empty group. Then select the group and the cluster and go to **Modify>Match Transformations>Match All Transforms.** Now the group is snapped to the cluster, you can parent the cluster to the group by selecting the clusterHandle and the group and press **P** or go to **Edit>parent**.

View fullsize

![cluster_groups.jpg](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1523304511951-FRV0PI322RK9MXY71SMH/cluster_groups.jpg)![cluster_groups.jpg]()

---

# The Collision Setup

**5 -** Now we create our collision mesh. Most of the time I use Polygon primitives as collision shapes like a cylinder or a sphere, but in this case I will use a static duplicate of the head mesh and delete the faces I don't need to collide with the curve. Then parent the collision mesh to the neck driver. For demonstration I just parented it under the joint directly.

I chose in this case to use a duplicate of the head because his chin is quite prominant and it would be nice to have it collide against the collar.

View fullsize

![collision_mesh_titles.gif](https://images.squarespace-cdn.com/content/v1/53e3e118e4b019d919160e6d/1524777913859-Z6F7AS8EB0RYPROS6ZAF/collision_mesh_titles.gif)![collision_mesh_titles.gif]()

**6 -**The last step for creatig our collision mesh is to selet the collision\_head and go to Rigging>Deform>Muscle>Muscles/Bones>Convert Surface to Muscle/Bone.

View fullsize

![collisionCapsule.jpg](h

... (原文过长，已截断)