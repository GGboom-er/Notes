---
tags: [html, Dynamics_Simulation]
---

# 🌐 面向动画师的 Maya nCloth - Kiel Figgins.html

> **一句话总结**：nCloth 布料仿真入门

## 🔗 本地文件
- [面向动画师的 Maya nCloth - Kiel Figgins.html](file:///Y:/GGbommer/Lib/Http/面向动画师的%20Maya%20nCloth%20-%20Kiel%20Figgins.html)
- **文件名称**：面向动画师的 Maya nCloth - Kiel Figgins.html
- **资源类型**：html
- **归属分类**：Dynamics_Simulation
- **本地路径**：[[面向动画师的 Maya nCloth - Kiel Figgins.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya nCloth for Animators - Kiel Figgins

  
**Maya nCloth for Animators**
  
Kiel Figgins - [3dFiggins.com](http://www.3dfiggins.com)

---

  
  

[Maya nCloth for Animators - Tutorial](https://vimeo.com/497678662) from [Kiel Figgins](https://vimeo.com/kielfiggins) on [Vimeo](https://vimeo.com).

  
  
*Table of Contents*
  
- [Overview](#Overview)
  
- [Rigid Body Simulation / Intro to Simming and collisons](#Process)
  
- [Collisons](#AdvSetup)
  
- [Creating Rivets](#AdvSetup)
  
- [Cloth Simulations](#AdvSetup)
  
- [Jiggle Simulations](#AdvSetup)
  
- [Tips](#AdvSetup)
  
  
  
Rigs used in this tutoral are available at [3dFiggins.com/Store](https://www.3dfiggins.com/Store)
  
[![](https://www.3dfiggins.com/Store/Thumbs/kft_drakonia.jpg)](https://www.turbosquid.com/FullPreview/Index.cfm/ID/1646282?referral=kielfiggins)
[![](https://www.3dfiggins.com/Store/Thumbs/kft_troll.jpg)](https://www.turbosquid.com/FullPreview/Index.cfm/ID/1484965?referral=kielfiggins)
[![](https://www.3dfiggins.com/Store/Thumbs/kft_nora.jpg)](https://www.turbosquid.com/FullPreview/Index.cfm/ID/1557652?referral=kielfiggins)
  
  
  
  

---

**Overview**

---

  
Animating secondary elements by hand can be a tedious and time consuming part of animating a character, especially if those elements make up a large part of the character design, such as long hair, a cape or multiple straps. In an effort to reduce this time spent, I've been using ncloth as a base to get simulated motion baked back onto the rigs based off the characters performance. Outside of spending less time animating these extra bits, other benefits are: the performance can change and I can re sim, I can play with the sim settings for varying effects, I'm less hesitant to animate a character with a complex design. Lastly, simulation adds a certain amount of realism and natural noise or chaos to your animation. These subtle shifts, sways and three axis motion would be difficult at best to achieve by hand, though tutorials are available <http://spungella.blogspot.com/2019/08/body-mechanics-animating-cloth-by-kyle.html> by <https://twitter.com/kyle_kenworthy>.
  
  
But our goal is offloading some of that work, so with that in mind let's get started!
  
  
As mentioned above, simulation is about realism, so if your animation is very stylized or exaggerated, decent results may be harder to get. For instance, if your character is moving really fast or your heavily cheating your poses for camera, these will be revealed when you start simming.
  
  
Secondly, the goal of this write up is about getting the simmed motion back onto the existing control rig, not about doing sims for renders. This process suffers a loss in fidelity based on how the control rig is set up and what controls are available. This loss in detail would be facets like wrinkles and exact collision contacts. If the control rig doesn't have enough fidelity to get those bits, they will be lost. You will also likely need to spend a bit of time at the end cleaning up the results and fixing penetration or clipping issues.
  
  
Thirdly, there are certain elements that are less suited to nCloth and more suited for anim overlap. Elements like antennas, elf ears or other single FK chains that retain their shape/structure and jiggle/sway instead of drap down and react. There are tools out there to help create this dynamic overlap such as <https://www.highend3d.com/maya/script/dynamics-fk-joint-chains-for-maya> and <https://www.youtube.com/watch?v=-H9-cAAoOQc>
  
  
Lastly, this write up is about getting "some" results, not the "best" results, as quickly and painlessly as possible. Simulation is an entire department and the rabbit hole for getting better results is a long one. If you would like learn about simulations and ncloth there are many other resources online. For now, here are the major steps to getting working results.
  
  
There are three main types of sim setups:
  
  
1. Rigid Body: a sword dropping, debris, a decapitated head rolling
  
  
2. Cloth: loin, straps, skirts, jackets, flaps
  
  
3. Jiggles: belly, breasts, muscles
  
  
All of these use the same systems but the workflow is slightly different for each. We'll start with Rigid Body as it's the most straight forward and a good introduction to sim scene setups.
  
  
  
  
  
  

---

**Rigid Body Simulation / Intro to Simming and collisons**

---

  
For our bare bones example scene, do the following:
  
  
1. Create a new scene
  
2. Create a polyCube
  
3. Translate the cube up and rotate it off axis
  

![](Images/ss_00_cube.jpg)
  
*Initial Cube Setup*
  
4. Select the Dynamics dropdown (nDynamics dropdown in older Mayas)
  

![](Images/ss_01_dd.jpg)
  
*Dynamics Dropdown*
  
5. Select the cube
  
6. nMesh > Create nCloth
  
7. Hit Play in the timeline
  
  
And magically the cube drops uselessly through the floor! So let's refine this and explain what we're doing.
  
  
1. Open the Outliner and select nucleus1 and set the usePlane channe

... (原文过长，已截断)