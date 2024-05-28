# toy

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一些简单的小玩具. 自己生活常用的内容.

## System Requirements

- Python latest version (3.11)
- Win系统 (Linux系统未测试)
- [Quicker](https://getquicker.net/)
- 调整[杀毒软件](#my-time-aware)

## Usage and Guide

使用Quicker作为菜单和UI. 主要途径是PowerShell脚本来调用Python程序/脚本, 一般就仅此而已.

### 关于日志文件与隐私

这是一个简明的项目, 可能只是有了想法就随手写的, 所以没有考虑比如日志和隐私等具体实现, 也并没有对每一个程序检查他们的依赖库和初始文件等配置.

这个项目的目的是分享, 所以我会尝试尽量完善它, 使得它可以更加方便的使用.

Feel free to make a pull request or open an issue!

---

## Programs

简单解释关于程序, 以及记录它们的理念与想法.

### Record Rename By Time

获取音频文件的创建时间, 然后重命名文件. 一般用于录音文件, export example: `2024-05-27T23_19_49.m4a`.

例如录音笔录音文件, 或者来自Just Press Record之类的录音软件. 会妥善地自动识别处理重复的录音: 跳过时间和内容完全相同的音频文件, 如果内容不同则会添加后缀并继续执行.

需要ffmpeg, python3.x.

请自行安装ffmpeg并配置环境变量 - 建议使用powershell测试ffmpeg/ffprobe是否可用.

使用方法:

1. `python3 record_rename_by_time.py` : 默认读取同文件夹里名为`source`的文件夹, 将里面所有的内容拷贝到`renamed`文件夹, 并且重命名文件.
2. `python3 record_rename_by_time.py source_folder destination_folder` : 读取`source_folder`文件夹, 将里面所有的内容拷贝到`destination_folder`文件夹, 并且重命名文件.
3. 没给参数, 或者也没有`source`文件夹, 会有帮助提示的.

### My Time Aware

#### 警告

Bitdefender会误报, 会触发"Advanced Threat Defense". 请自行调整或者触发后restore受影响的文件 以便加入白名单

#### 简介与理念

原名`作息与时差.py`

我时常有作息不规律的情况, 或者说人总有偶尔不健康的时刻.

我的习惯与认知是, 不去强迫自己, 但是让自己清楚面对真实与事实.

我个人是觉得, 这是重要且必要的. 至于调整, 或许是自然而然的事情, 也可以是之后的具体行动.

对于健康的了解, 有的人就是晚睡晚起的类型, *有的人就是早睡早起的类型. 但是, 有的人却是不规律的, 也有的人是规律的, 但是不是自己想要的.*(自动补全了个绕口令哈哈)

总之, 一个人可以很晚或者过早得起床, 但是他醒了多久, 这个是值得关注的.

那么进一步, 我们假设一天是24小时(也有例外), 那么我们也可以继续假设日出而作 日落而息, 于是一般认知中的"标准人", 我们可以说他是8小时睡眠, 7点醒来, 23点睡着.

这是一个过于理想化的假设, 但是它是有意义的, 是个很好的提示与参考.

#### 使用

请配置Quicker或者其他工具, 通过PowerShell脚本调用本Python程序.

如果需要更新时间, 输入时间然后回车即可.

如果不需要, 只是查看, 直接回车即可关闭与退出了.

因为查看是更加频繁的, 所以更新时间的提示词我省略了.

---

### sc2map

消磨时间时喜欢打星际2, 但是有些地图和指挥官我不喜欢, 所以就花了几分钟写了这个简单的脚本.

### open_clipboard

学习并实践下[Docstring](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings) with sphinx, 初步实践pylint, 以及一些简单的操作.
读取剪贴板的文件或者文件夹路径, 然后通过资源管理器打开目标位置.

### base64_checker

检查base64编码的字符串是否和原始图片一致.
支持命令行参数, 也支持交互式输入.

---

## Reminders (个人的学习笔记)

py文件的命名规则: 一般使用纯小写, 但是如果是多个单词, 则使用下划线分割. 比如`my_clock.py`

### sphinx

- 安装: `pip install sphinx`, 然后`cd toy`
- 使用: `python -m sphinx.cmd.quickstart docs`来初始化一个文档目录, 生成的sphinx在`docs`目录下
- `python -m sphinx.ext.apidoc -f -o docs/sourc .` 来生成API文档
- 生成文档: `python -m sphinx -b html docs mydocs` 生成html文档, 也可以使用`make html`来生成(Linux)

## License

This project is licensed under the MIT License.
