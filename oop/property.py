#!/usr/bin/env python3
#coding=utf-8 

class Student(object):
    def get_score(self):
        return self._score
    
    def set_score(self, value):
        if(not isinstance(value, int)):
            raise ValueError('score must be an interger')
        if(value < 0 or value > 100):
            raise ValueError('score must between 0 - 100')
        self._score = value

# @property: 把方法当做属性调用
# 把一个getter方法当做属性 只需要加上@property即可
# 同时创建另一个装饰器@score.setter 负责把一个setter方法变成属性赋值
class Student1(object):
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger')
        if value > 100 or value < 0:
            raise ValueError('value must between 0 - 100')
        
        self._score = value

# 定义只读属性
# temp属性未定义setter 为只读属性
class Student2(object):
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value

    @property
    def temp(self):
        return self._score - 60
    

class Screen(object):
    # __slots__ = ('width', 'height')
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger')
        self._width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height
    
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
