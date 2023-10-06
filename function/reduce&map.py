#!/usr/bin/env python3
# coding=utf-8

from functools import reduce
from math import pow

# 高阶函数

# 变量可以指向函数
f = abs
print(f(-10))

# 函数名可以是变量
# abs = -1
# abs(-10) #报错


# 高阶函数：参数为函数
def add(x, y, f):
    return f(x) + f(y)


print(add(10, -4, abs))


# map(func, iterables)
# 将传入的函数作用于iterable的每个元素中 并将结果作为Iterator返回
def f(x):
    return x * x


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = map(f, L)
print(list(r))
print(list(map(str, L)))


# reduce(func, iterables)
# 把传入的函数作用于一个序列上
# 该函数必须接受两个参数
# reduce把结果继续和序列的下一个元素做累积计算
# 序列求和
def calSum(x, y):
    return x + y


print(reduce(calSum, L))


def add1(x, y):
    return 10 * x + y


print(reduce(add1, L))


# map + reduce
def fn(x, y):
    return x * 10 + y


def str2num(s):
    return int(s)


print(reduce(fn, map(str2num, '123444')))


# 首字母大写 其余小写
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 求积
def cal1(x, y):
    return x * y


def prod(L):
    return reduce(cal1, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# str2float
def func1(x, y):
    return x * 10 + y


def func2(x):
    config = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    if x in config:
        return config[x]
    return x


def str2float(s):
    n = list(map(func2, s))
    dotIndex = n.index('.')
    sum1 = reduce(func1, n[:dotIndex])
    sum2 = reduce(func1, n[dotIndex + 1:])
    return sum1 + sum2 * pow(10, (dotIndex - len(n) + 1))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
