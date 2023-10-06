#!/usr/bin/env python3
# coding=utf-8

import functools
import time
import types


# 函数是一个对象 函数对象可赋值给变量 通过变量可以调用函数
def now():
    print('2023-07-18')


f = now
f()

# __name__：函数名称
print(now.__name__, f.__name__)


# 装饰器decorator：函数运行期间动态增加功能的方式
# 本质：返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print('func.name = ', func.__name__)
        print('call %s()' % func.__name__)
        func(*args, **kw)
    return wrapper

# F1 = log(str)
# F1(2343.2323)


@log
def print_now():
    print('2023-07-18')


print_now()


# decorator 本身传入参数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('text %s, %s()' % (text, func.__name__))
            func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def print_now_second():
    print('2023-07-18')


print_now_second()
print(print_now_second.__name__)  # wrapper 不正确


# 完整decorator示例
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        # do what you want do before func
        print('before func run')
        res = func(*args, **kw)
        print('after func run')
        return res
    return wrapper


# 完整 带参数 decorator示例
def logWithParams(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s() text %s' % (func.__name__, text))
            return func(*args, **kw)
        return wrapper
    return decorator


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        res = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return res
    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def log(n):
    if (not isinstance(n, types.FunctionType)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s()' % func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        def wrapper(*args, **kw):
            print('%s()' % (n.__name__))
            n(*args, **kw)
        return wrapper


@log
def f1():
    pass


@log('execute')
def f2():
    pass


f1()
f2()
