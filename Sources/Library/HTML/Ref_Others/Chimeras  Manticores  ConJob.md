---
tags: [html, Ref_Others]
---

# 🌐 Chimeras & Manticores – Con Job.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Chimeras & Manticores – Con Job.html](file:///Y:/GGbommer/Lib/Http/Chimeras%20&%20Manticores%20–%20Con Job.html)
- **文件名称**：Chimeras & Manticores – Con Job.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[Chimeras & Manticores – Con Job.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Chimeras & Manticores – Con Job

## Chimeras & Manticores

[![](https://theodox.github.io/theme/img/profile.png)](https://theodox.github.io)

# 

a blog about technical art, python, the games business, and obscurantism

# Con Job

Posted on Sat 04 April 2015 in [blog](https://theodox.github.io/category/blog.html)

If you do a lot of tools work in maya – particularly if you’re working one something that integrates with a whole studio toolset, instead of being a one-off script – you spend a lot of time restarting. I think I know every pixel of the last five Maya splash screens by heart at this point. A good knowledge of the python `[reload()](https://docs.python.org/2/library/functions.html#reload)` command can ease the pain a bit, but there are still a lot of times when you want to get in and out quickly and waiting for the GUI to spin up can be a real drag.

If this drives you nuts, `mayapy` — the python interpreter that comes with Maya — can be a huge time saver. There are a lot of cases where you can fire off a mayapy and run a few lines of code just to validate that things are working and you don’t need to watch as all the GUI widgets draw in. This is particularly handy if you do a lot of tools work or script development, but’s also a great environment for doing quickie batch work – opening a bunch of files to troll for out of date rigs, missing textures, and similar annoyances.  
All that said, the default mayapy experience is a bit too old-school if you’re running on Windows, where the python shell runs inside the horrendous `CMD` prompt, the same one that makes using DOS so unpleasant. If you’re used to a nice IDE like [PyCharm](https://www.jetbrains.com/pycharm/) or a swanky text editor like [Sublime](http://www.sublimetext.com/3), the ugly fonts, the monochrome dullness, and above all the antediluvian lack of cut and paste are pretty offputting.

However, it’s not too hard to put a much more pleasant face on mayapy and make it a really useful tool.

## Con Ed

[![](http://www.top10films.co.uk/img/conair_cage.jpg)](http://www.top10films.co.uk/img/conair_cage.jpg)

> obligatory “con” joke here.

The first thing to do is find a good *console program*. A console provides the window and display services for command-line programs; `CMD.exe` does the same thing, it just does it very *badly*. There are several good options depending on your taste (good roundup [here](http://www.nextofwindows.com/4-better-windows-console-tools-alternatives-to-windows-built-in-command-prompt/))). I’m going to walk through the setup for my favorite emulator, [ConEmu](http://conemu.github.io/), but the same ideas should adapt to the other emulators pretty simply.  
First, here’s a quick round up of what [ConEmu](http://conemu.github.io/) is going to be doing for us and mayapay:

#### Cut and paste

`Ctrl+C`, `Ctrl+V`. Worth the price of admission all by itself!

#### Customizable fonts

A killer feature for those of us with old, weak eyes and/or aspirations to style

#### Command history

If you’re testing out a bit of syntax, or doing something that repetitive but not worth really automating you’ll get a lot of value out of the command history: you can use the up and down arrows to scroll through your recently issued commands and repeat them. Especially when you’re testing a script over and over this takes the bite out of those two or three lines of setup you need to enter again and again.

#### Startup options

We’ll want to pass a few flags and instructions to mayapy every time.

#### Multiple consoles in one window

ConEmu allows you to run different shells in different tabs. This can be invaluable if you’re doing things like checking the contents of multiple folders, but it’s also a great way to compare the results of your maya scripts side-by-side in two different sessions

#### Transparency

A palliative for OSX envy.

## Setup basics

> Again, these instructions are for ConEmu – if you try this with a different console, add your experience in the comments for others!

ConEmu is a great little tool, and it’s free, but it is a bit… overeager?… in its efforts to let you control everything. The interface is a bit old school, so it’s worth walking through the setup process step by step.  
First you’ll want to download and install [ConEmu](http://conemu.github.io/) (the installation instructions are down at the botton of the linked page, and the setup is basically ‘unzip into a folder’).

Once you’ve got ConEmu up and running, you’ll want to open the settings dialog and select the *Tasks* option from the tree list at left. This will show you a dialog like this:

[![](http://3.bp.blogspot.com/-w0mbodm7rfY/VSAucMI2xPI/AAAAAAABLnI/0y0424YSh94/s1600/conemu_1.jpg)](http://3.bp.blogspot.com/-w0mbodm7rfY/VSAucMI2xPI/AAAAAAABLnI/0y0424YSh94/s1600/conemu_1.jpg)

> Like I said, old school.

For starters going to create a startup preset that launches mayapy. ConEmu calls these ‘tasks’. To create a new one, click that `+` botton under th

... (原文过长，已截断)