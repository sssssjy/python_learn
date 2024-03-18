"""
循环结构
while for...in
"""
# import random

# for-in 循环求和
# range(a, b, step = 1): 构建 a - b-1 范围 前闭后开 步长1
sum = 0
for i in range(101):
    sum += i
print(sum)

range(1, 101)  # 1-100 整数
range(1, 101, 2)  # 1-100 奇数
range(100, 0, -2)  # 100-1 偶数

# for-in 1-100 偶数求和
sum_1 = 0
for i in range(2, 101, 2):
    sum_1 += i
print(sum_1)

# while循环
# 猜数游戏
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入你猜的数'))
#     if number > answer:
#         print('大了')
#     elif number < answer:
#         print('小了')
#     else:
#         print('恭喜你，猜对了')
#         break
# print(f'你一共猜了{counter}次')

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i > j:
#             continue
#         print(f'{i}*{j}={i * j}', end='\t')
#     print()

# 输入一个正整数判断是不是素数。
# a = int(input('请输入一个正整数 判断是否为素数'))
# flag = True
# for i in range(2, a):
#     if a % i == 0:
#         flag = False
#         break
# if flag is True:
#     print(f'{a}是素数')
# else:
#     print(f'{a}不是素数')

# 练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
# b = int(input('输入第一个数'))
# c = int(input('输入第二个数'))

# if c < b:
#     b, c = c, b  # 保证b是较小的那个数

# d = 1
# for i in range(1, b + 1):
#     print(b % i, c % i)
#     if b % i == 0 and c % i == 0:
#         d = i
# print(f'最大公约数为{d}')
# print(f'最小公倍数{b * c // d}')

# 打印三角形
row = int(input('请输入三角形行数'))
for i in range(row):
    for j in range(i + 1):
        print('*', end='')
    print()

print()

for i in range(row, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print()

length = row * 2 - 1
middle = length // 2 if length % 2 == 0 else length // 2 + 1
print(length, middle)
for i in range(row):
    for j in range(length + 1):
        if j >= middle - i - 1 and j <= middle + i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
