#!/usr/bin/env python3
# coding=utf-8

' a test module '  # 文档注释 任何模块的第一个字符串都会被视为模块的文档注释 __doc__
__author__ = 'sjy'  # 作者名

import sys


def test():
    args = sys.argv
    if (len(args) == 1):
        print('args length 1')
    elif (len(args) == 2):
        print('args[1]: %s' % args[1])
    else:
        print('too many arguments')


# __name__:python内置属性 全局系统变量
# 若模块被导入 __name__为该文件的文件名
# 若模块被直接执行 __name__为__main__
# 用于鉴别程序入口 多用于测试代码 其他文件引用时不会执行
if __name__ == '__main__':
    test()


# 作用域：用_开头 不应该被直接引用
def _x():
    print('private function')
