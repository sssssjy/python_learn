#!/usr/bin/env python3
#coding=utf-8 

# dict 全称 dictionary,其他语言中称为Map，使用key-value
d = {'mick': 3,'lily': 34}
print(d['mick'])
d['meta'] = 123
print(d['meta'])

# 避免key不存在的问题
# 1、in 判断是否存在key值
print('meta' in d)
print('ddd' in d)
# 2、 get()方法 若key不存在 可以返回None或者指定值
print(d.get('ddd'))
print(d.get('ddd', -2))

# pop() 删除key
# 注意！ dict内部存放顺序与key的放入顺序没有关系
d.pop('meta')
print(d)

# list 与 dict 的对比

# list
# 查找和插入的时间随元素的增加而增加
# 占用空间小 浪费内存少

# dict
# 查找和插入速度极快，不会随key的增加而减慢
# 需要占用大量内存，内存浪费多 是一个空间换时间的方法
# dict的key必须是不可变对象 
# dict根据key通过hash算法来计算value位置 若每次计算结果不同 dict内部会混乱



# set key的集合 不能重复 必须是不可变对象
s = set([1,2,3,3,3])
print(s)
# add() 添加key
s.add('a')
print(s)
# 交集& 与 并集|
s1 = set([12,3,23])
s2 = set([12,55,235])
print(s1 & s2)
print(s1 | s2)

# 可变对象与不可变对象

# list 可变对象
list1 = ['a', 'c', 'b']
list1.sort()
print(list1) #['a', 'b', 'c']

# str 不可变对象
# replace 返回了一个新的str str1作为变量始终指向不变量'abc'
str1 = 'abc'
print(str1.replace('a', 'A')) #Abc 相当于 str2 = str1.replace('a', 'A')
str2 = str1.replace('a', 'A') #Abc
print(str1) #abc