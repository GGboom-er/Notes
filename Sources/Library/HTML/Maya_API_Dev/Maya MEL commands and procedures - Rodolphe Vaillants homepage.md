---
tags: [html, Maya_API_Dev]
---

# 🌐 Maya MEL commands and procedures - Rodolphe Vaillant's homepage.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Maya MEL commands and procedures - Rodolphe Vaillant's homepage.html](file:///Y:/GGbommer/Lib/Http/Maya%20MEL%20commands%20and%20procedures%20-%20Rodolphe%20Vaillant's%20homepage.html)
- **文件名称**：Maya MEL commands and procedures - Rodolphe Vaillant's homepage.html
- **资源类型**：html
- **归属分类**：Maya API 开发
- **本地路径**：[[Maya MEL commands and procedures - Rodolphe Vaillant's homepage.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Maya MEL commands and procedures - Rodolphe Vaillant's homepage

|  |  |
| --- | --- |
| [Rodolphe Vaillant's homepage](/)Research, teaching and more... |  |

* [Bio](/page/home "About me")
* [Tutorials](/page/teaching "Site map / Table of content")
* [Links](/page/links "Bookmarks / pinterests")
* [Blog](/weblog/weblog "Somewhat cleaner articles")
* [Jumble](/weblog/jumble "Draft notes")

# [Maya MEL commands and procedures](/entry/76/maya-mel-commands-and-procedures)

A listing of MEL commands and procedures that were hard to find. - 10/2016 - #[Maya](/category/maya)

![](/images/2017-03/mel_script_window.png)

How to find the MEL command Maya runs when you click a menu or button? Sometimes Maya doesn't explicitly display the MEL command that is executed when you click on a GUI element.

Here are a few tips:

* In the script editor go to `History` and enable `Echo All Commands`.
* Try and look in `Window` -> `Settings/Preferences` -> `Hotkey Editor` (The hot key editor contains a long list to MEL shortcuts!)
* The hard way: go to [[scripts]] and look for the menu names directly into Maya's code. You can use a grep command or open every script file into your favorite IDE (Vim, QtCreator, Visual Studio..)

Here is some procedures I had to look up by myself:

# Mesh Display

In Maya GUI: `Mesh Display` -> `Toggle Display Colors Attributes`   
 MEL equivalent: `toggleShadeMode();`

# Modify

In Maya GUI: `Modify` -> `Paint Attributes Tool`   
MEL equivalent: `ArtPaintAttrTool();`

## Modify -> Evaluate Nodes

In Maya GUI: `Modify` -> `Evaluate Nodes` -> `Evaluate All`  
MEL equivalent: `EnableAll();`

In Maya GUI: `Modify` -> `Evaluate Nodes` -> `Ignore All`  
MEL equivalent: `DisableAll();`

---

In Maya GUI: `Modify` -> `Evaluate Nodes` -> `IK Solvers`  
MEL equivalent: `setState iksolver true/false;`

[![Rss](/images/rss.svg)](/index.php?feed=rss)
[![Paypal donation](/images/paypal_donate_button.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=blog%40rodolphe-vaillant.fr&item_name=Thank+you+%3AD¤cy_code=USD&source=url&lc=EN&country=US)

No comments

Please enable Javascript (and reload this page) to add any comments.

Name

Email
 (optional field, I won't disclose or spam but it's necessary to notify you if I respond to your comment)

All html tags except <b> and <i> will be removed from your comment. You can make links by just typing the url or mail-address.

Anti-spam question:  
**√4 + 40 = ?**

Criticism comes effortlessly. Art is always hard.
  
(Fr: La critique est aisée et l'art est difficile)
  
 -- Destouches

![](/pivotx/scheduler.php)