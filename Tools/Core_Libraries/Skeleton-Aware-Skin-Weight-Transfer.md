---
tags: [Core_Libraries, Maya_Rigging, tool]
tech_stack: [C++]
---
# 🛠️ Skeleton-Aware-Skin-Weight-Transfer
> **> **Authors**: [Ziyuan Cao](https://github.com/Ziyuan-Cao), [Tomohiko Mukai](https://github.com/TomohikoMukai)**

- 📂 [Skeleton-Aware-Skin-Weight-Transfer](file:///Y:/GGbommer/scripts/Skeleton-Aware-Skin-Weight-Transfer)

## 💡 详细说明
# Skeleton-Aware Skin Weight Transfer for Helper Joint Rigs

> **Authors**: [Ziyuan Cao](https://github.com/Ziyuan-Cao), [Tomohiko Mukai](https://github.com/TomohikoMukai)
>
> **Affiliations**: Tokyo Metropolitan University

[[Video]](https://www.youtube.com/watch?v=LyW50RFzJOs&feature=youtu.be)

**Abstract**

We propose a method to transfer skin weights and helper joints from a reference model to other targets. Our approach uses two types of spatial proximity to find the correspondence between the target vertex and reference mesh regions. The proposed method first generates a guide weight map to establish a relationship between the skin vertices and skeletal joints using a standard skinning technique. The correspondence between the reference and target skins is established using vertex-to-bone projection and bone-to-skin ray-casting using the guide weights. This method enables fully automated and smooth transfer of skin weight between human-like characters bound to helper joint rigs.

