---
tags: [Core_Libraries, Maya_Rigging, tool]
tech_stack: [C++]
---
# 🛠️ dem-bones
> **<img align="left" width="60" height="60" src="logo/DemBones.png">**

- 📂 [dem-bones](file:///Y:/GGbommer/scripts/dem-bones)

## 💡 详细说明
<img align="left" width="60" height="60" src="logo/DemBones.png">

# Dem Bones
[![BSD3 Clause](https://img.shields.io/badge/license-BSD3_Clause-blue.svg)](LICENSE.md)
[![Version](https://img.shields.io/badge/version-1.2.1-green.svg)](VERSION.md)

This repository contains an implementation of [Smooth Skinning Decomposition with Rigid Bones](http://binh.graphics/papers/2012sa-ssdr/), 
an automated algorithm to extract the *Linear Blend Skinning* (LBS) with bone transformations from a set of example meshes. 
*Skinning Decomposition* can be used in various tasks:
- converting any animated mesh sequence, e.g. geometry cache, to LBS, which can be replayed in popular game engines,
- solving skinning weights from shapes and skeleton poses, e.g. converting blendshapes to LBS,
- solving bone transformations for a mesh animation given skinning weights.

This project is named after "The Skeleton Dance" by Super Simple Songs.

## Contents
- `include/DemBones`: C++ header-only core library using [Ei
