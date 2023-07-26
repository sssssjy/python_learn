#!/usr/bin/env python3
#coding=utf-8 

# 闭包：内部函数引用外部函数的变量
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
    
f1, f2, f3 = count()
print(f1(), f2(), f3()) #9 9 9

def count1():
    fs = []
    for i in range(1, 4):
        def f(j):
            return lambda : j * j
        fs.append(f(i))
    return fs

f1, f2, f3 = count1()
print(f1(), f2(), f3()) #1 4 9


# nonlocal 在闭包内部赋值外部变量 需要声明 否则报错
def inc():
    x = 0
    def fn():
        # return x + 1 #仅读取 不报错

        #必须声明 否则报错
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f())

def createCounter():
    count = 0
    def counter():
        nonlocal count
        count = count + 1
        return count
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')