#!/usr/bin/env python3
#coding=utf-8 

from typing import Any


class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % k)
    
    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value

# 执行注释中的代码
if __name__ == '__main__':
    import doctest
    doctest.testmod()