---
tags: [Maya_Rigging, Pipeline_General, tool]
tech_stack: [Python]
---
# 🛠️ dayu_path
> **[![Build Status](https://travis-ci.org/phenom-films/dayu_path.svg?branch=master)](https://travis-ci.org/phenom-films/dayu_path)**

- 📂 [dayu_path](file:///Y:/GGbommer/scripts/dayu_path)

## 💡 详细说明
# dayu_path

[![Build Status](https://travis-ci.org/phenom-films/dayu_path.svg?branch=master)](https://travis-ci.org/phenom-films/dayu_path)

针对影视行业的文件路径处理类。比起传统的os.path 有着下面的优点：

* 将文件路径作为对象处理
* 更好的针对影视行业文件优化。可以快速得到frame count、version 等字段
* 扫描文件自动拼合序列帧，并且可以识别丢帧
* 更快捷的文件序列帧格式转换。支持%0?d、####、$F? 的三种形式
* 序列批量改名、移动、拷贝（帧数自动重排）
* 支持用户自行对DayuPath 添加更多的方法、属性

# 如何安装
```bash
pip install -U dayu-path
```

# 简单用法说明

```python
from dayu_path import DayuPath

# 初始化
disk_path = DayuPath('/some/v0001/A001C001_170922_E4FB.1001.exr')

# 查询父级目录
assert disk_path.parent == '/some/v0001'

# 拼接子文件夹、子文件
assert disk_path.parent.child('child', 'new_file.txt') == '/some/v0001/child/new_file.txt'

# 获得文件名、文件扩展名、文件主干部分
assert disk_path.name == 'A001C001_170922_E4FB.1001.exr'
assert disk_path.ext == '.exr'
assert disk_path.stem == 'A001C001_170922_E4FB.1001'

# 扫描当前目录下的所有文件夹、文件
print disk_path.parent.listdir()

# 遍历当前文件夹下所有深度的文件夹、文件
for single_file in disk_path.parent.walk():
    print single_file

# 快速获得相应的versio
