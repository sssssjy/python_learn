#!/usr/bin/env python3
#coding=utf-8 

import logging
import pdb

#logging
logging.basicConfig(level=logging.ERROR) #debug info warning error
# 打印error 屏蔽其他类型的logging 
logging.info('info info info')
logging.warning('warnning warnning')
logging.error('error error')
logging.debug('debug debug debug')

# assert 断言 表达式应该为True 否则抛出AssertionError
# -O (大写字母O) 可以关闭断言 相当于pass
# /usr/local/bin/python3 -O /Users/shanjiaying/Documents/python/test/assert.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n
foo('0')


#pdb.set_trace() 
# p + 变量名 查看变量
# c 继续
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)