# 苍之彼方的四重奏解包

## 简介

Steam上的Aokana, Aokana Extra1 和 Aokana Extra2都可以通过该脚本解包。

## 具体过程

0. 提前安装 python环境、pythonet包 和 ImageMagick

1. 通过`dnspy`将`Assembly-Csharp.dll`的`namespace`修改为`Aokana`

2. 将该dll、所有的`.dat`文件和脚本文件`extract.py`放在同一个文件夹

3. 运行`python extract.py -d`，解包所有的`.dat`文件

4. 将`system/def/vcglist.csv`，所有的cg图片和脚本文件`extract.py`放在同一个文件夹

5. 运行`python extract.py -m`，合成所有的图片