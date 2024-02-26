"""
使用type对类型进行检查
type()
"""

a = 1
b = '1'
c = True
d = 1 + 5j
e = 3.5323

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'bool'>
print(type(d))  # <class 'complex'>
print(type(e))  # <class 'float'>

"""
类型转换函数
int(): 转换为int
str(): 转换为str
float(): 转换为浮点数
chr(): 整数类型转换为该编码对应的字符串(一个字符)
ord(): 字符串(一个字符)转换为对应的编码
"""

# 类型转换
print(str(a))  # '1'
print(int(b))  # 1
print(int(c))  # 1
print(int(False))  # 0
print(chr(83))  # S
print(ord('单'))  # 21333
