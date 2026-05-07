---
tags: [Maya_Rigging, Pipeline_General, tool]
tech_stack: [未知]
---
# 🛠️ maya_bifrost
> **Compounds for rigging**

- 📂 [maya_bifrost](file:///Y:/GGbommer/scripts/maya_bifrost)

## 💡 详细说明
# gkRig
Compounds for rigging

# Installation
Add the path to **gkRig\bifrost_lib_config.json** to the environment variable **BIFROST_LIB_CONFIG_FILES** in the Maya.env. Maya.env is normally located in the Documents\maya\20xx for Windows user.
For example, if you saved gkRig in C:\Autodesk\Bifrost\gkRig, you should add the following in the Maya.env. If you want to add multiple bifrost_lib_config.json, use **;** for separating each path.

`BIFROST_LIB_CONFIG_FILES = C:\Autodesk\Bifrost\gkRig\bifrost_lib_config.json`

# Compounds
## b_spline
This compound interpolates between the given control points(cvs) by a quadratic B-Spline curve, and outputs the interpolated position and the tangent.
### Namespace : gkRig::Motion
### Inputs

  - **cvs** (type: array\<Math::float3\>)<br>
    Control vertices used for interpolating by quadratic B-Spline. You need to have minimum 4 cvs.
  - **parameter** (type: float | array\<float\>)<br>
    0.0 to 1.0 value which determines the parametric position o
