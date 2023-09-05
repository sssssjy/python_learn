#!/usr/bin/env python3
# coding=utf-8

# __str__ __repr__
from typing import Any


class Student(object):
    def __init__(self, name) -> None:
        self.__name = name

    # 自定义打印实例的输出内容 用户看到的字符串
    def __str__(self) -> str:
        return 'Student object name: %s' % self.__name

    # 返回程序开发者看到的字符串 用于调试服务
    def __repr__(self) -> str:
        return 'repr string %s' % self.__name


print(Student('Lisa'))

s = Student('Mike')
print(s)


# 通常 str 与 repr 内容相同
class Stu1(object):
    def __init__(self, name) -> None:
        self.__name = name

    def __str__(self) -> str:
        return 'stu1 string %s' % self.__name

    __repr__ = __str__


# __iter__ 用于for...in循环调用 类似list/tuple 返回迭代器对象
class Fib(object):
    def __init__(self) -> None:
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

# for i in Fib():
    # print(i)


# __getitem__ 读取元素
class Fib1(object):
    # 兼容切片 [1:3]
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib1()
print(f[4])
print(f[4: 10])


# __getattr__ 在没有找到属性的情况下调用
class Stu2(object):
    def __getattr__(self, key):
        if key == 'age':
            return lambda: 34


# 链式调用
class Chain(object):
    def __init__(self, path='') -> None:
        self.__path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))

    def __str__(self) -> str:
        return self.__path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


# __call__ 调用示例
# 一个对象是否能被调用 callable
class Stu3(object):
    def __init__(self, name) -> None:
        self.name = name

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('my name is %s' % self.name)


s1 = Stu3('namee3333')
s1()
print(callable(s1))


class Chain1(object):
    def __init__(self, path='') -> None:
        self.__path = path

    def __call__(self, path) -> Any:
        return Chain1('%s/%s' % (self.__path, path))

    def __getattr__(self, path):
        return Chain1('%s/%s' % (self.__path, path))

    def __str__(self) -> str:
        return self.__path

    __repr__ = __str__


print(Chain1().users('michael').repos)
