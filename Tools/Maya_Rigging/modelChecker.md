---
tags: [Maya_Rigging, Pipeline_General, tool]
tech_stack: [Python]
---
# 🛠️ modelChecker
> **<h1 align="center">modelChecker</h1>**

- 📂 [modelChecker](file:///Y:/GGbommer/scripts/modelChecker)

## 💡 详细说明
<h1 align="center">modelChecker</h1>

modelChecker is a python plug-in written for Autodesk Maya to sanity check digital polygon models. It is unopinionated, provides concise reporting, and lets you select your error nodes easily.

![modelChecker](./modelChecker.png)

## Install

Download the [modelChecker.zip](https://github.com/JakobJK/modelChecker/archive/main.zip) and place the modelChecker folder in your Maya scripts directory and create a python shelf button with the following code:

```python
from modelChecker import modelChecker_UI

modelChecker_UI.UI.show_UI()
```

## Usage

There are three ways to run the checks.

1. If you have objects selected, the checks will run on the current selection. Select objects in object mode. (component mode won't work).
2. On a hierarchy by declaring a root node in the UI.
3. The checks will run on the entire scene if nothing is selected and the root node field is left empty.

## Authors

- [**Jakob Kousholt**](https://www.linkedin.com/in/jakobj
