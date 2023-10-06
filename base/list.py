#!/usr/bin/env python3
# coding=utf-8 

# list
list = [1, 2, 3]
print(len(list))
print(list[-2])

# append 往尾部添加
list.append(4)

# insert 插入
list.insert(1, 5)

# pop 删除 可制定删除索引i
list.pop()
list.pop(3)

# 替换
list[2] = 45
print(list)

# tuple 元组 与list类似 一旦初始化便不能修改
tupleList = (1, 4, 3)
# 定义空元组
tupleEmpty = ()
# 定义一个元素
tupleSingle = (2,)
