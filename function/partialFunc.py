#!/usr/bin/env python3
#coding=utf-8 

import functools
# 偏函数 functools.partial:把某些函数的参数设置默认值 

# 给int函数设置默认参数 2进制
# 可接受 函数对象 *args **kw 三个参数
int2 = functools.partial(int, base = 2)

# 相当于传入int('0101010', {base = 2})
print(int2('0101010'))

max2 = functools.partial(max, 10)
#将10 传入args中 相当于 max(10, 6, 7)
print(max2(6, 7))