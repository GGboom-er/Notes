---
tags: [html, Ref_Others]
---

# 🌐 高效的 Maya 开发环境 - Rodolphe Vaillant 的主页.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [高效的 Maya 开发环境 - Rodolphe Vaillant 的主页.html](file:///Y:/GGbommer/Lib/Http/高效的%20Maya%20开发环境%20-%20Rodolphe%20Vaillant%20的主页.html)
- **文件名称**：高效的 Maya 开发环境 - Rodolphe Vaillant 的主页.html
- **资源类型**：html
- **归属分类**：参考与其它
- **本地路径**：[[高效的 Maya 开发环境 - Rodolphe Vaillant 的主页.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Efficient Maya development environment - Rodolphe Vaillant's homepage

|  |  |
| --- | --- |
| [Rodolphe Vaillant's homepage](/)Research, teaching and more... |  |

* [Bio](/page/home "About me")
* [Tutorials](/page/teaching "Site map / Table of content")
* [Links](/page/links "Bookmarks / pinterests")
* [Blog](/weblog/weblog "Somewhat cleaner articles")
* [Jumble](/weblog/jumble "Draft notes")

# [Efficient Maya development environment](/entry/108/efficient-maya-development-environment)

- 02/2020 - #[Maya](/category/maya)

![](/images/2020-03/maya_dev_env_banner_2.jpg)

How to setup your IDE so that clicking 'build' allows you to test and run your Maya plugin without extra steps or application restart.

To avoid copy/pasting plugin files it is best to tell Maya where to find the binary and scripts directly from your project folder.
You can add the following environment variables:

### Windows

```
MAYA_SHELF_PATH = C:\repo\trunk\plugin_name_maya\prefs\shelves/mayaxxxx
MAYA_SCRIPT_PATH = C:\repo\trunk\plugin_name_maya\scripts;C:\repo\trunk\libraries\toolbox_maya\mel
PYTHONPATH = C:\repo\trunk\plugin_name_maya\scripts
MAYA_PLUG_IN_PATH = C:\repo\trunk\plugin_name_maya\lib\mayaxxxx\release;C:\repo\trunk\plugin_name_maya\lib\mayaxxxx\debug
XBMLANGPATH = C:\repo\trunk\plugin_name_maya\prefs\icons
```

### Linux

```
MAYA_SHELF_PATH = $PLUGIN_MAYA_PATH/prefs/shelves/mayaxxxx
PLUGIN_MAYA_PATH = /home/user/repo/trunk/plugin_name_maya
MAYA_SCRIPT_PATH = $PLUGIN_MAYA_PATH/scripts;C:\repo\trunk\libraries\toolbox_maya\mel
PYTHONPATH = $MAYA_SCRIPT_PATH
MAYA_PLUG_IN_PATH = $PLUGIN_MAYA_PATH/lib/mayaxxxx/release:$PLUGIN_MAYA_PATH/lib/mayaxxxx/debug
XBMLANGPATH = $PLUGIN_MAYA_PATH/prefs/icons
```

Note 1 Instead of globally defining these variables in your OS,
  
you can instead define those in Maya.env  
(usually located around `C:/Users/your\_name/Documents/maya/2015-x64`)  
  
Note 2 `MAYA_SHELF_PATH` should always be defined first!  
  
Once this setup is completed you should be able to load the plugin using one of the methods below:

### Alternate method

You can use a python script to set the equivalent of `PYTHONPATH` and `MAYA_SCRIPT_PATH`.
All you need is to place a `userSetup.py`
(this script will get executed every time Maya starts)
file in:
  
  
`C:/Users/your_name/Documents/maya/2022/scripts/`
  
  
And simply put:

```
import sys
sys.path.insert(0, r"C:/some/path/scripts")
```

Maya will now also check into `C:/some/path/scripts` to find scripts.

# Loading / Unloading your plugin

### From Maya MEL command line

```
# loadPlugin plugin_name.mll
# loadPlugin plugin_name_debug.mll // for the plugin in debug mode
```

### From python cmds interface

```
from maya import cmds
cmds.loadPlugin("plugin.mll")
```

Alternatively if you haven't set PLUGIN\_MAYA\_PATH you can load plugins using an absolute path based on the location of your current python script:

```
cmds.loadPlugin(os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugin.mll")
```

### Through Maya GUI

`Window -> Settings/Preferences -> Plug-in Manager`

### Remotely!

It is possible to execute maya commands remotely (i.e from the Operating system command line).
This is really useful if you whish to automatically unload / build / reload the plugin without having to type or press anything in Maya!
In other words it is possible to re-build the plugin with a single click, and test is immediatly directly in Maya.
First you need to open a port in Maya with the Mel command:
  
  
`commandPort -n ":54321";`  
  
I recommend launching it automatically at each startup (through `userSetup.mel` in `maya\_user\_folder/scripts/userSetup.mel`)
Then execute the python script in a flow that look like this:

```
py ./project_name/scripts/remote_plugin_unload.py
make -j8
py ./project_name/scripts/remote_plugin_load_release.py
```

[Example of python scripts.](/images/codes/python_maya_utils.zip)
  
  
Obviously you need to install python to execute those scripts (or use the interpreter installed with Maya)

# Setup your IDE for C++ projects

It's worth noting it is usually pretty easy to setup your favorite IDE such as VS code (recommended), Qt creator, Eclipse etc.
to execute those three steps when pushing the "build button"!

### Visual Code

In 2022 this is my editor of choice for both C++ and Python.

Copy this `tasks.json` file in your local folder `.vscode/` in order to define a list of tasks/build steps.
`Terminal -> Run Task...` to choose which build to do (e.g. Maya 20xx release) or `ctrl+shift+b` to run the task set to be the default one:

yourProjectRootFolder/.vscode/tasks.json

```
{
  "version": "2.0.0",

  // We must run vcvars64.bat before running any build command 
  // so that environment variables are set correctly.
  "windows": {
    "options": {
        "shell": {
            "executable": "cmd.exe",
            "args": [
                "/d", 
                "/c", 
                "\"C:\\Program Files\\Microsoft Visual Studio\\2022\

... (原文过长，已截断)