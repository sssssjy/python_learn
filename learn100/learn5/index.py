"""
practice 1-4
"""

# 寻找水仙花数。
# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
# 它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：1^3 + 5^3+ 3^3=153。
result_list = []
for i in range(100, 1000):
    a = i // 100
    b = i % 100 // 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        result_list.append(i)
print(result_list)

# 正整数反转
# num_1 = int(input('请输入一个正整数'))
# result_2 = 0
# while num_1 > 0:
#     result_2 = result_2 * 10 + num_1 % 10
#     num_1 = num_1 // 10
# print(result_2)

# 百钱百鸡问题。
# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for x in range(101):
    for y in range(101 - x):
        for z in range(101 - x - y):
            if 5*x + 3*y + z/3 == 100 and x + y + z == 100:
                print(f'公鸡{x}只，母鸡{y}只，小鸡{z}只')

# 生成斐波那契数列的前20个数。
a = 1
b = 1
for i in range(21):
    c = a + b
    a = b
    b = c
    print(f'第{i}个数：{c}')

# 找出10000以内的完美数。
# for i in range(1, 10001):
#     list = []
#     for j in range(1, i):
#         if i % j == 0:
#             list.append(j)
#     if sum(list) == i:
#         print(f'{i}是完美数')

# 输出100以内所有的素数。
for i in range(1, 100):
    flag = True
    for j in (2, i):
        if i % j == 0 and j < i:
            flag = False
            break
    if flag:
        print(f'{i}是素数')
