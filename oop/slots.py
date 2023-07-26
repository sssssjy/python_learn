#!/usr/bin/env python3
#coding=utf-8 

from types import MethodType

class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s) #给实例绑定一个方法
s.set_age(32)
print(s.age)

# 一个实例绑定的方法不可以在另一个实例中访问
# 可以绑定在class上 使所有实例都能访问
def set_score(self, score):
    self.score = score

Student.set_score = set_score

# __slots__:限制实例能添加的属性

class Stu(object):
    __slots__ = ('name', 'age')

s1 = Stu()
s1.age = 3
s1.name = 'Gin'

# s1.score = 44 #报错