#!/usr/bin/env python3
#coding=utf-8 

import os
#列表生成器

#range 快速生成list
list1 = list(range(1, 11))
print(list1)

#生成 [1*1, 2*2, ..., 10*10] list
list2 = [x * x for x in range(1, 11)]
print(list2)

#筛选偶数
# 此时 if为筛选条件 不能添加else
list3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list3)
# if...else
list6 = [x if x % 2 == 0 else -x for x in range(2, 8)]
print(list6)

#循环使用 实现全排列
list4 = [m + n for m in 'ABC' for n in 'XYZ']
print(list4)

#列出当前目录下所有文件和目录名
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

#字符串小写
list5 = ['Hello', 'My', 'Friend']
print([x.lower() for x in list5])


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str) ]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')