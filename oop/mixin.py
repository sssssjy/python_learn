#!/usr/bin/env python3
#coding=utf-8 

# 多重继承

from socketserver import ForkingMixIn, TCPServer, ThreadingMixIn, UDPServer


class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 大类2
class Runnable(object):
    pass

class Flyable(object):
    pass

# 各种动物

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# Mixin 继承多个类

# 多进程tcp服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 多进程udp服务
class MYUDPServer(UDPServer, ThreadingMixIn):
    pass
