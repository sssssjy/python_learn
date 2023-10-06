#!/usr/bin/env python3
# coding=utf-8

# 字符编码

# ASCII 1个字节
# 8bit = 1byte 1个字节能最大代表 255
# ASCII码 由美国人发明 仅有127个字符（数字、英文、符号）

# Unicode 通常为2个字节
# 由于其他语言也要编想要编入ASCII 各个国家有了不同的编码 例如中国为GB3212
# 为了解决不同国家的编码不同问题 由Unicode统一
# 通常为2个字节 个别生僻字符使用4个字节
# 例如 A: ASCII中编码为 01000001 Unicode中编码为 00000000 01000001

# UTF-8 可变长度编码
# 若使用Unicode编码 会造成资源浪费 因此诞生UTF-8编码
# 英文通常为1个字节 中文通常为3个字节 生僻字符可能为4-6个字节

# 在计算机内存中 统一使用Unicode编码
# 保存至硬盘或传输时 使用UTF-8编码

# ord() 获取字符的整数表示
print(ord('A'))
print(ord('中'))

# chr() 将编码转为字符
print(chr(54))
print(chr(10023))

# python中 字符串类型为str 在内存中以Unicode编码表示
# 若要传输或者保存至硬盘 需要转为bytes
# Python 对bytes类型的数据用 b'' 或者 b"" 表示

a = 'ABC'  # str
b = b'ABC'  # bytes 每个字符占用1个字节

# encode 编码转换
print('ABC'.encode('ascii'))  # b'ABC'
print('中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii')) #报错 ASCII码中没有中文

# decode 字节流转换编码
print(b"ABC".decode('ascii'))  # ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文
# 若decode中有无法解析的字符 会报错 使用 errors='ingore' 忽略
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# len 计算str字符数 计算bytes字节数
print(len('ABC'))  # 3
print(len('中文'))  # 2

print(len(b'ABC'))  # 3
print(len('中文'.encode('utf-8')))  # 6

# 格式化 %
# %d 整数 %f 浮点数 %s 字符串 %x 16进制数
print('hello, %s' % 'world')
print('Hi, this is %s, you have %d dollars' % ('Anna', 35.32))
print('%.2f' % 23.2555)
print('%2d-%02d' % (3, 1))
# 转义
print('aa%%34')

# 格式化 format
print('this is {0}, his grade is {1:.2f}'.format('selina', 3))

# 格式化 f-string
r = 3
d = 5
print(f'the area is {r}, the length is {d:.2f}')

a1 = 72
a2 = 85
print(f'last year {a1}, this year {a2}, percent: {(a2 - a1)/a1 * 100:2.1f}%')