import sys
import os
import time
import random
"""
字符串和常用数据结构
列表 元组 集合 字典
"""

s1 = 'str1'
s2 = "str2"
s3 = """
    str3
    str3
"""

# 使用\可进行转义
s4 = '\'str4\n\r\t\\'
# 使用十六进制或六进制代表字符
s5 = '\x61\141'
# unicode编码
s6 = '\u9a86'

# 使用r \将不代表转义
s7 = r'\390'

"""
使用 + 拼接字符串
使用 * 重复字符串
in / not in 进行成员运算 判断一个字符串中是否含有目标字符串
[] / [:] 提取某个字符 或 字符串切片(左闭右开)
"""
ss1 = 'hello ' * 3
print(ss1)
ss2 = ss1 + 'world'
print(ss2)
print('ll' in ss2)
print('s' not in ss1)
print(ss2[4])
print(ss2[0:2])

ss3 = 'abcdefg1234567'
print(ss3[1:3])
print(ss3[3:])  # 从第3个索引开始往后
print(ss3[:4])  # 从第0个索引到第4个索引（不包括第4个索引）
print(ss3[2::2])  # 从第2个索引开始 每2个取一个 直到最后
print(ss3[::3])  # 从第0个索引开始 每3个取一个 直到最后
print(ss3[-10:-3])  # 从第-10个索引到第-3个索引（不包括第-3个索引）
print(ss3[-3:-1])  # 从第-3个索引到第-1个索引（不包括第-1个索引）
print(ss3[::-1])  # 倒序输出

"""
字符串处理方法
len(str): 获取字符串长度
str.capitalize(): 获取字符串首字母大写的copy
str.title(): 获取字符串每个单词首字母大写的copy
str.upper(): 获取字符串每个字母大写的copy
str.find(): 从字符串中查找子串第一次的位置 找不到位置时返回-1
str.rfind(): 从字符串中查找子串最后出现的位置 找不到位置时返回-1
str.index(): 与find类似 但找不到时会报错 ValueError: xxx not found
str.startswith(): 检查str是否以子串开头
str.endswith(): 检查str是否以子串结尾
str.center(length, char): 将字符串以指定长度居中 并在两侧填充指定字符(仅1个)
str.rjust(50, char): 将字符串以指定长度靠右放置，并在左侧填充指定字符
str.isdigit(): 检查字符串是否由数字构成
str.isalpha(): 检查字符串是否由字母组成
str.isalnum(): 检查字符串是否由字母和数字组成
str.strip(): 获得字符串去除两侧空格之后的copy
"""
ss4 = 'do you wanna go out with me?'
print(len(ss4))
print(ss4.capitalize())
print(ss4.title())
print(ss4.upper())
print(ss4.find('ou'))
print(ss4.find('ddd'))
print(ss4.index('ou'))
# print(ss4.index('aadsa'))
print(ss4.startswith('s'))
print(ss4.endswith('me'))

print(ss4.center(50, '*'))
print(ss4.rjust(50, '*'))

ss5 = 'abcdefg1234567'
print(ss5.isdigit())
print(ss5.isalpha())
print(ss5.isalnum())
ss6 = '   dddd   '
print(ss6.strip())

"""
列表 list 结构化非标量类型

* 列表内容重复
len(list): 列表长度
for...in: 循环遍历
enumerate: 配合for...in可同时遍历下标和元素

list.append(item): 添加元素
list.insert(index, item): 插入元素 在目标下标插入元素

list.extend(list1) 合并列表
list += list1 合并列表(与extend相同)

list.remove(item): 删除元素
list.pop(index): 指定位置删除元素
list.clear(): 清空列表
list.sorted(list, reverse, key): 列表排序 返回排序后的数组 不改变原数组
    reverse: 是否逆序
    key: 根据key(方法)排序, 默认字母表顺序
"""
list1 = [1, 3, 4, 5, 6]
list2 = ['aa', 'bb'] * 3
print(list2)
# 下标 索引运算
print(list1[1])
print(list1[-1])
# print(list1[100])  # IndexError: list index out of range
for item in list1:
    print(item)

for index, item in enumerate(list1):
    print(index, item)

list1.append(23)
list1.insert(2, 88)
print(list1)
list2.extend([3, 4])
list2 += [2, 43]
print(list2)
if 2 in list2:
    list2.remove(2)

# 指定位置删除元素
list2.pop(4)
list2.pop(len(list2) - 1)
print(list2)
list3 = [1, 2, 1]
list3.remove(1)  # 移除找到的第一个
print(list3)
list3.clear()

# 列表的切片
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

fruits2 = fruits[3:5]
print(fruits2)
# 使用[:]可直接复制数组
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-4: -1]
print(fruits4)
# 倒转顺序copy
fruits5 = fruits[::-1]
print(fruits5)

# 列表排序 sorted
list11 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list12 = sorted(list11)
list13 = sorted(list11, reverse=True)
list14 = sorted(list11, key=len)  # 按字符串长度排序
print('--------')
print(list12, list13, list14)

"""
生成式和生成器
"""
f1 = [x for x in range(1, 10)]
f2 = [x + y for x in 'abcd' for y in '124343']

# 生成式[]和生成器{} yield对比
# 生成式 在定义变量时内部元素已经生成 占用内存较大
f3 = [x ** 2 for x in range(1, 100)]
print(sys.getsizeof(f3))
print(f3)

# 生成器 在定义时内部元素未生成 占用内存小
# 在需要使用时需要通过内部运算得到数据 花费额外时间
f4 = (x ** 2 for x in range(1, 100))
print(sys.getsizeof(f4))
print(f4)
for val in f4:
    print(val)


# 定义生成器语法 yield: 讲普通函数改为生成器函数
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

"""
元组: 与列表类似 容器数据类型
用一个变量存储多个数据
元组内部元素不可修改

元组转换为数组: list()
数组转换为元组: tuple()

元组vs数组
数组内部内容可改,元组不可改
如果内部元素不变,优先使用元组
元组在创建时间和占用空间上都优于数组
sys.getsizeof(): 检查占用内存大小
ipython %timeit: 获取代码执行耗费时间
"""
t = ('a', 123, '元组', True)
# 获取元组中的元素
print(t[2])
# 遍历元组
for member in t:
    print(member)
# 将元组转换为数组
t_list = list(t)
print(t_list)
# 数组转换为元组
t_list1 = tuple(t_list)
print(t_list1)

print(f'元组大小{sys.getsizeof(t)}')
print(f'数组大小{sys.getsizeof(t_list)}')

"""
集合
创建集合 set(): 元素不重复

set.add(T): 在尾部添加元素
set.remove(T): 删除指定元素 若不存在会报错
set.discard(T): 删除指定元素 若不存在不会报错
set.update(列表|元组|字典): 添加多个元素
set.pop(): 随机删除一个元素 该方法会对set内部元素无序排列 并删除左边第一个元素
set.clear(): 清空元素

交集 &
并集 |
差集 -
两个集合不重合部分 ^
判断子集或超集 >= <= > <
"""
# 创建集合
set1 = {1, 3, 4, 5, 7}
print(set1)
print('length of set1', len(set1))
# 构造器方法创建
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 4, 5))
print(set2, set3)
# 推导式语法
set4 = {x for x in range(0, 100) if x % 3 == 0 and x % 7 == 0}
print(set4)

set1.add(9)
set1.remove(1)
if 4 in set1:
    set1.remove(4)
set1.discard(444)

print(set1 & set2)
print(set1 | set2)
print(set1 ^ set2)
print(set1 <= set2)

"""
字典:
生成方式:
    键值对 dict()
    zip():将两个序列压成字典
    推导式语法

遍历字典:
    for key in dict:

获取值: dict.get(key, 默认值)
删除元素: dict.popitem() dict.pop()
清空字典: dict.clear()
"""
dict1 = {'a': 1, 'b': 2}
dict2 = dict(one=1, two=2)
dict3 = dict(zip(['a', 'b', 'c'], '123'))
dict4 = {x: x**2 for x in range(1, 11)}
print(dict1, dict2, dict3, dict4)

for key in dict4:
    print(f'{key}, {dict4[key]}')

# 更新元素
dict1['a'] = 3
dict2.update(one=4)

print(dict1.get('a', 44))


# 在屏幕上展示跑马灯文字
def func1():
    str1 = '我是测试跑马灯的文字'
    count = 0
    while count < 10:
        # 清除输出
        os.system('clear')
        print(str1)
        str1 = str1[1:] + str1[0]
        count += 1
        time.sleep(0.2)


# func1()
# 随机生成指定长度str
def func2(char_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_char_len = len(all_chars)
    code = ''
    for i in range(0, char_len):
        random_num = random.randint(0, all_char_len - 1)
        code += all_chars[random_num]
    return code


random_code = func2(5)
print(random_code)


# 返回文件后缀名
def get_file_suffix(filename):
    pos = filename.rfind('.')
    if pos == -1:
        print('invalid filename')
        return ''
    return filename[pos:]


print(get_file_suffix('dfadsa.txt'))


# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def func4(_list):
    if len(_list) < 2:
        print('数组元素不够')
        return
    m1, m2 = (_list[0], _list[1]) if _list[0] < _list[1] else (_list[1], _list[0])
    for i in range(2, len(_list)):
        if _list[i] > m2:
            m1 = m2
            m2 = _list[i]
        elif _list[i] > m1:
            m1 = _list[i]
    return m1, m2


print(func4([1, 3, 4, 62, 1, 3, 51, 0, 9, 12, 34, 21, 5, 74]))


# 练习5：计算指定的年月日是这一年的第几天。
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    # is_leap_year(year)返回true 1 false 0
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for i in range(month - 1):
        total += days_of_month[i]
    return total + day


print(which_day(1998, 10, 13))
print(which_day(2024, 1, 4))
print(which_day(2024, 3, 28))


# 练习6：打印杨辉三角。
def func5(line):
    pass
