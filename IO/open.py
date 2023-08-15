#!/usr/bin/env python3
#coding=utf-8 

# open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# open
# r 读取 若不存在 抛出 IOError
# f = open('/Users/shanjiaying/Documents/text.txt', 'r')
# read 一次性读取所有文件 用str对象表示
# print(f.read())

# 读取完文件后必须关闭
# f.close()

# 文件读写时 可能会发生IOError 需要保证一定能关闭
# try:
#     f = open('/Users/shanjiaying/Documents/text.txt', 'r')
#     print(f.read())
# finally:
#     f.close()

# with语句简化
# with open('/Users/shanjiaying/Documents/text.txt', 'r') as f:
#     print(f.read())
    
# read:直接使用read()将一次性读取所有文件内容
# read(size): 读取size个字节的内容
# readline(): 读取一行
# readlines(): 读取全部内容 并将内容以list形式返回

# with open('/Users/shanjiaying/Documents/text.txt', 'r') as f:
    # for line in f.readlines():
        # print(line.strip())

# file-like Object: 返回有read()方法

# 二进制：open 第二个参数rb
# with open('/Users/shanjiaying/Documents/text.txt', 'rb') as f:
    # print(f.read())

# 字符编码：open encoding参数
# with open('/Users/shanjiaying/Documents/text.txt', 'r', encoding='gbk') as f:
    # print(f.read())

# 忽略错误 errors='ignore'
# with open('/Users/shanjiaying/Documents/text.txt', 'r', encoding='gbk', errors='ignore') as f:
    # print(f.read())

# 写文件：open参数 w / wb 写文本或二进制
# 可以反复使用write写入内容 需要使用f.close()
# 操作系统可能不会立刻把write内容写入文件 只有close方法执行才能保证写入
# 否则可能只写入部分
# 不覆盖原本内容：a
with open('/Users/shanjiaying/Documents/pythonwrite.txt', 'x') as f:
    f.write('hello python')

with open('/Users/shanjiaying/Documents/pythonwrite.txt', 'a') as f:
    f.write('hello python second')

'''
    r : 读取(默认)
    w : 覆盖写入
    x : 创建文件并写入, 如果文件存在会报错
    a : 在尾部添加
    b : 字节模式
    t : 文本模式（默认）
    + : 读写模式
'''