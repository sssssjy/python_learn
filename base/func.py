#!/usr/bin/env python3
#coding=utf-8 

# abs 绝对值函数
# max 返回最大值函数
# int float str bool 类型转换函数
# hex 16进制转换函数
import math

a = 123
print(str(hex(a)))

# 函数
# 使用 def 定义函数
# def 函数名(参数):
#     return 返回值
# 若没有返回值 默认返回None

def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


# 空函数 pass 通常用于占位符 等想好之后补充
def passFunc():
    pass

def passFunc1(x):
    if x > 10:
        pass

# 参数检查 isinstance()
def my_abs1(x):
    if not isinstance(x, (float, int)):
        raise TypeError('bad type')
    elif x > 0:
        return x
    else:
        return -x
    
# my_abs1('dd')

# 返回多个值 返回值为tuple
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(23, 12, 5, 30)
r = move(23, 23, 4, -30)
print(x, y)
print(r)

def quadratic(a, b, c):
    if not isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        raise TypeError('a, b, c must all be type int or float')
    elif b**2 - 4 * a * c < 0:
        print('次方程无解')
    else:
        temp1 = b**2 - 4 * a * c
        x1 = (-b + math.sqrt(temp1)) / (2 * a)
        x2 = (-b - math.sqrt(temp1)) / (2 * a)
        return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


#=============================================================
# 位置参数 与 默认参数
def power(x: int, n = 2):
    return x ** n

print(power(3, 4))

# 重要！ 默认参数必须是不变对象
def listFunc(list = []):
    list.append('End')
    return list

# 若调用 listFunc()多次 将会返回同一个list 造成错误
# python在函数定义阶段时便已经计算完成了list的值 [], list 指向了 []
print(listFunc()) #['End']
print(listFunc()) #['End', 'End']
print(listFunc()) #['End', 'End', 'End']

# 正确方式
# 在编程中尽量使用不变对象
def listFunc1(list = None):
    if list == None:
        list = []
    list.append('End')
    return list

print(listFunc1()) #['End']
print(listFunc1()) #['End']
print(listFunc1()) #['End']

# 可变参数 *
# 内部接收到tuple 可以传递0-任意个参数
def calc(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number ** 2
    
    return sum

list1 = [1, 2, 3]
print(calc( 1, 2, 3))
print(calc(*list1)) # 将list或tuple的元素作为可变参数传入函数

# 关键字参数 ** 
# 传入0-任意个含参数名的参数 在函数内部组装为dict
def person(name, age, **others):
    print('name:',name, 'age:', age, 'others,', others)

person('lina', 34, city = 'admi')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'add', 'job': 'dd'}
# **dict 为dict的一份拷贝 不改变原dict
person('acd', 34, **extra)

# 命名关键字参数 *后的参数为命名关键字参数
# 只接受定义的关键字
# 必须传入参数名
def person1(name, age, *, city, gender):
    print(name, age, city, gender)

# 若已存在可变参数 则不需要 *
def person2(name, age, *other, city = 'me', gender):
    print(name, age, other, city, gender)

person1('lisa', 14, city = 'los', gender = 'm')
person2('rose', 2, 3, 4, 4, city = 'lc', gender= 'a')

# 参数组合 必选参数 默认参数 可变参数 命名关键字参数 关键字参数 
def f1(a, b = 3, *, name, **others):
    print(a, b, name, others)

def f2(a, b = 4, *numbers, age, **others):
    print(a, b, numbers, age, others)

f1(23, name = 'name', age = 'age')
f1( 1, 2, name = 3, age = 'age')

f2(43, 23, 45, 34, 34, age = '33', city = '33dd')
f2( 334, *[1, 2, 3], age = '34', city = 'dd')

def mul(*numbers):
    if len(numbers) == 0:
        raise TypeError('至少输入一个数字')
    else:
        sum = 1;
        for number in numbers:
            if(not isinstance(number, (int, float))):
                raise TypeError('请输入int 或 float')
            else:
                sum = sum * number
        
        return sum

print(mul(1,2,3,4,5))
# print(mul(1,'2',3,4,5))
# print(mul())

print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

# 小结
# 默认参数一定要用不可变对象
# *args是可变参数，接受一个tuple
# **kw是关键字参数，接受一个dict

# 可变参数可以直接传入 func(1,2,3) 也可组装为list或tuple再传入 func(*(1,2,3))
# 关键字参数可以直接诶传入 func(a = 3, b = 2) 也可组装为dict再传入 func(**{'a': 2, 'b': 4})
# *args **kw 习惯用法
# 定义命名参数时 若没有可变参数 需要加上 * 分隔

#=============================================================
# 递归函数

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)
    
print(fact(3))
# print(fact(1000)) #内存溢出

# 解决调用递归栈溢出 尾递归
# 尾递归：在函数返回时 调用函数本身 return不能包含表达式
# 无论调用多少次 只占用1个栈

def fact1(n):
    return fact_inner(n, 1)

def fact_inner(num1, num2):
    if num1 == 1:
        return num2
    else:
        return fact_inner(num1 - 1, num2 * num1)
    
print(fact1(5))

def move(n, a, b, c):
    if(n == 1):
        print(a, '---->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '---->', c)
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')