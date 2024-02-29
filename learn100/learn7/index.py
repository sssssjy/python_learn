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