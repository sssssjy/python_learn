"""
分支结构(选择结构)
if elif else
"""

username = input('请输入名称')
password = input('请输入密码')

# python 使用缩进来表示代码结构
if username == 'admin' and password == '123456':
    print('success')
else:
    print('error')

# 英寸与厘米互相转换
value = int(input('请输入数字'))
type_1 = input('请输入类型')
if (type_1 == 'in' or type_1 == '英寸'):
    print(f"{value}英寸转换为厘米的结果为{value * 2.54}")
elif (type_1 == 'cm' or type_1 == '厘米'):
    print(f"{value}厘米转换为英寸的结果为{value / 2.54}")
else:
    print('请输入正确的参数')

# 百分制转换为等级制
# 要求：如果输入的成绩在90分以上（含90分）输出A；
# 80分-90分（不含90分）输出B；
# 70分-80分（不含80分）输出C；
# 60分-70分（不含70分）输出D；
# 60分以下输出E。
score = int(input('请输入分数'))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')
