"""
字符串和常用数据结构
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
str.find(): 从字符串中查找子串的位置 找不到位置时返回-1
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

list1.insert(2, 88)
print(list1)
list2.extend([3, 4])
list2 += [2, 43]
print(list2)
list2.remove(3)
list2.pop(4)
list2.pop(len(list2) - 1)
print(list2)
list3 = [1, 2, 1]
list3.remove(1)  # 移除找到的第一个
print(list3)

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
