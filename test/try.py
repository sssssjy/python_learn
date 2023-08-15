#!/usr/bin/env python3
# coding=utf-8 

import logging
from functools import reduce

try:
    print('try...')
    r = 10 / 0
    print('result % s' % r)
except ValueError as e:
    print('value error', e)
except ZeroDivisionError as e:
    print('error %s' % e)
else:
    print('no error')
finally:
    print('finally...')
print('END')

# python 的错误其实也是class  继承自BaseException
# 捕捉错误时 不仅捕捉该类错误 还将该类错误的子类错误一并捕捉
# try:
#     foo()
# except ValueError:
#     print('value err')
# except UnicodeError:
#     print('unicode err')


# try...except 可以跨越多层调用
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('error', e)
    else:
        print('no error')
    finally:
        print('finally')


main()


# logging 记录错误信息 打印错误信息后会继续执行
def main1():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main1()

print('END')


# 自定义错误 raise
class FooError(ValueError):
    pass


def foo1(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value %s' % s)
    return 10 / n


# foo1('0')


# raise 语句不带参数 将把错误向上抛出 让上层调用者接收
def bar1():
    try:
        foo('0')
    except ValueError:
        print('Value Error !!!')
        raise

# bar1()


def str2num(s):
    return float(s.strip())


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

# main()
