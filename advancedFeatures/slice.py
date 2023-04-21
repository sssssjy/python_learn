#!/usr/bin/env python3
#coding=utf-8 

# 切片

list1 = [1, 2, 3, 4, 5]

print(list1[0:3])
# 若从第一个开始截取 可省略 0
print(list1[:3])

print(list1[1: 4])

# 倒数切片 最后一位是 -1
print(list1[-2:])
print(list1[-3:-1])

# 每x个 取1个
arr = list(range(100))
print(arr[::5])

# 前20个每2个取一个
print(arr[:20:2])

# 直接复制原数组
print(arr[:])

# tuple切片 返回的依然是tuple
print((0, 2, 4, 6, 8)[:4])

# 字符串切片
print("abcdefg"[:4])

def trim(s):
    if(len(s) == 0):
        return s
    if(s[0] != ' ' and s[-1] != ' '):
        return s
    if(s[0] == ' '):
        s = s[1:]
    if(s[-1] == ' '):
        s = s[:-1]
    return trim(s)

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
