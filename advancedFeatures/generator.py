#!/usr/bin/env python3
# coding=utf-8

# 生成器
# 一边循环一边计算 保存算法

g1 = (x * x for x in range(10))
# print(g1)
# print(next(g1)) #0
# print(next(g1)) #1
# print(next(g1)) #4

# 上述next方法 几乎不使用 使用for循环
# for n in g1:
#     print(n)

# generator函数 yield


# fib函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# fib(10)


# 定义为generator
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, b + a
        n = n + 1
    return 'done'


print(fib1(4))

# 执行generator函数 会返回一个generator对象 执行多次会生成多个generator对象
# generator函数执行时 遇到yield会中断 等待下一次next()继续

g = fib1(6)

for n in g:
    print(n)

# 捕捉错误(暂时 不用记)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print('err', e.value)
        break


def triangles(maxLen):
    r, n = [1], 0
    while (n < maxLen):
        yield r
        r = [1] + [r[i] + r[i + 1] for i in range(0, len(r) - 1)] + [1]
        n = n + 1
    return 'done'


trianglesG = triangles(10)
for n in trianglesG:
    print(n)
