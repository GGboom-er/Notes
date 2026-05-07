---
tags: [Maya_Animation, Maya_Rigging, tool]
tech_stack: [MEL, Python]
---
# 🛠️ mayakeyframereduction
> **Keyframe Reduction for Maya using least-squares method.**

- 📂 [mayakeyframereduction](file:///Y:/GGbommer/scripts/mayakeyframereduction)

## 💡 详细说明
# Added support for Maya 2023
# maya-keyframe-reduction
Keyframe Reduction for Maya using least-squares method.

<p align="center"><img src="docs/_images/keyframeReductionExample.gif?raw=true"></p>

## Installation
* Extract the content of the .rar file anywhere on disk.
* Drag the keyframeReduction.mel file in Maya to permanently install the script.

## Usage
A button on the MiscTools shelf will be created that will allow easy access to
the ui, this way the user doesn't need to worry about any of the code. If user
wishes to not use the shelf button the following commands can be used.

The ui responds to the current selection where it finds all of the suitable
animation curves for reduction. You will be able to filter the animation
curves based on the plug it is connected to. This will make it easier to
target exactly the curves you want to reduce.

After an animation curve is reduced the reduction percentage will be printed
to the console. This can give you an idea if you would like t
