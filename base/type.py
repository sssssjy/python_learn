#!/usr/bin/env python3
#coding=utf-8 

# 整数
# 过大可以用_分割
print(100_000_000)
# 16进制
print(0xa23b2)

# 浮点数
# 过大过小可用科学计数法
# 没有大小限制 但超出一定范围会表示为inf(无限大)
print(12.76e10)
print(-153.3e8)

# 字符串
print('helllllllllo \' "string" \' \" ')
# 转义
print('\r aaa \n ccc')
# 不转义 r''
print(r'\t\d\n')
# 多行内容 '''    '''
print('''line1
 line2
 line3''')

print(r''' first line
second line\d\t\n
third line''')

# boolean True False
# 可用 and not or 运算
print(True and True)
print(False or True)
print(not 2 < 4)

age = input('please enter your age:');
if int(age) > 18:
    print('adult')
else:
    print('teenager')


# 空值 None

# 变量 命名规则 大小写英文 + _ + 数字 组合而成，开头不可以是数字

# 常量 通常用全大写的变量名表示 (习惯用法 本质还是变量)

# 除法
print(10 / 3) #输出浮点数
print(10 // 3) #地板除 输出整数
print(10 % 3) #余数 输出整数