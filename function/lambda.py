#!/usr/bin/env python3
#coding=utf-8 

# 匿名函数 lambda:只能有一个表达式 没有return

L1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L1)

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)