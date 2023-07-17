#!/usr/bin/env python3
#coding=utf-8 

from collections.abc import Iterable, Iterator

# 可用for遍历 均为迭代
# 可迭代对象:list tuple dict等

# dict
dict1 = {'a': 3, 'c': 34, 'g': 'df', 'b': 'dfff'}
# 迭代key
for key in dict1:
    print(key, dict1[key])
# 迭代value
for value in dict1.values():
    print(value)
# 迭代 key value
for k, v in dict1.items():
    print(k, v)

# 迭代string
str = 'ABCdefg'
for i in str:
    print(i)

# 判断 是否可迭代 Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,4,6], Iterable))
print(isinstance(235, Iterable))

# enumerate 把list检索为key-value
for i,value in enumerate([1, 2, 'A', 'b']):
    print(i, value)

for x,y in [(1, 2), ('ab', 'c'), ('df', 34)]:
    print(x, y)

# Iterable对象：可以直接作用于for循环的对象
# Iterator对象：可以被next()调用并返回下一个值的对象

# Iterator对象表示一个数据流 可以被next()一直调用直到抛出StopIteration错误
# 可把他看作有序序列 但不能提前知道序列长度 具有惰性
# 只有在需要返回下一个数据时才会计算
isinstance((x for x in range(10)), Iterable) #True
isinstance((x for x in range(10)), Iterator) #True

isinstance([], Iterable) #True
isinstance([], Iterator) #False



def findMinAndMax(l):
    if(not isinstance(l, list)):
        raise TypeError('bad type')
    else:
        min = None
        max = None
        for i in l:
            if(min == None or min > i):
                min = i
            if(max == None or max < i):
                max = i
        return (min, max)
    
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

