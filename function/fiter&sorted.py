#!/usr/bin/env python3
#coding=utf-8 

#filter(func, iterables)
# 接受一个函数 和 一个序列 将传入的函数一次作用于序列 根据返回结果True/False决定是否保留
# 返回一个序列

#保留奇数
def is_odd(x):
    return x % 2 == 1
print(list(filter(is_odd, [1, 3, 4,7,8,10])))

#删除多余空字符串
# strip: 删除字符串头尾指定字符 默认为空格或者换行符 只能删除头尾字符
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 计算素数：埃氏筛法
# 取序列的第一个数 把后续该数的倍数筛选掉 以此类推
def _odd_iter():
    n = 1
    while(True):
        n = n + 2
        yield n

# lambda 匿名函数 单行函数
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break

def is_palindrome(n):
    return n == int(str(n)[::-1])

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#sorted(list, key, reverse) 排序函数 key:自定义排序函数 reverse:倒序

#按绝对值排序
print(sorted([-1,-9,3,5,-3], key=abs))

l = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(l, key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

def by_score(t):
    return t[-1]

L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score, reverse=True)
print(L3)