'''
一个围绕base64编码的小工具，用于检查base64和原始图片的差异
已知base64图片可能来自于:
1. 原始代码
2. 本地markdown
3. 其他, 但本工具应该保持精简所以应不支持
原始图片预计来自于:
1. 文件路径
此外, 这个工具的支持应该是支持传入参数的, 也就是说应该是一个命令行工具.
同时也支持交互式的使用.
所以有三种使用/格式:
base64checker.py -b base64(file address) -i image(file address)
'''

import base64
import os
import sys
import argparse


