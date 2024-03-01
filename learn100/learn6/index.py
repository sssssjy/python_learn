"""
函数与模块
"""
from random import randint


# 函数阶乘 math.factorial
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# m = int(input('请输入第一个数'))
# n = int(input('请输入第二个数'))
# print(fact(m)// fact(n) // fact(m - n))


# 函数的默认值
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        # randint 左闭又闭 range 左闭右开
        total += randint(1, 6)
    return total


def add_1(a=0, b=0, c=0):
    return a + b + c

# print(roll_dice())
# print(roll_dice(3))

# print(add_1())
# print(add_1(3))
# print(add_1(c=3))
# print(add_1(b=3, c=1, a=-1))


# 可变参数 args
def add_2(*args):
    total = 0
    for arg in args:
        total += arg
    return total

# print(add_2())
# print(add_2(1, 2))


# 实现计算求最大公约数和最小公倍数的函数。
def gcd(x, y):
    # 最大公约数
    (x, y) = (y, x) if y < x else (x, y)
    for i in range(x, 0, -1):
        if y % i == 0 and x % i == 0:
            return i


def lcm(x, y):
    # 最小公倍数
    return x * y // gcd(x, y)


# 实现判断一个数是不是回文数的函数。
def is_palindrome(num):
    # 判断是否是回文
    res = 0
    temp = num
    while temp > 0:
        res = temp % 10 + res * 10
        temp //= 10
    return res == num


# 实现判断一个数是不是素数的函数。
def is_prime(num):
    mid = num // 2 + 1
    res = 1
    for i in range(1, mid + 1):
        if num % i == 0:
            res = i
    return res == 1


# 写一个程序判断输入的正整数是不是回文素数。
def func_3(num):
    return is_prime(num) and is_palindrome(num)


print(func_3(223456))
print(func_3(34543))
print(func_3(123321))

"""
global 与 nonlocal
"""


# 全局作用域 global
def test():
    global a
    a = 200
    print(a)


# nonlocal
# 可以让最里面的函数使用最近的一个外函数已声明的变量，
# 将最里面的函数的局部变量设置和最近的一个外函数声明的变量为同一个变量（引用同一个内存地址）
# 拿不到global中的变量
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


if __name__ == '__main__':
    print('只有该文件被直接执行时会执行此if')
    a = 100
    test()
    print(a)
