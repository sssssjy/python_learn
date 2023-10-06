#!/usr/bin/env python3
# coding=utf-8

# for...in
names = ['lily', 'machel', 'senerina']
for name in names:
    print(name)

# range() 生成整数序列 例如 range(5) = [0,1,2,3,4]
# list() 转换为list
sum = 0
sumList = list(range(101))
for number in sumList:
    sum = sum + number

print(sum)

# while
sum1 = 0
maxNum = 99
while maxNum > 0:
    sum1 = sum1 + maxNum
    maxNum = maxNum - 2

print(sum1)

# break
sum2 = 0
maxNum2 = 10
while maxNum2 > 0:
    sum2 = sum2 + maxNum2
    maxNum2 = maxNum2 - 1
    if maxNum2 < 5:
        break

print(sum2)

# continue
sum3 = 0
maxNum3 = 10
while maxNum2 > 0:
    if maxNum2 % 2 == 0:
        continue
    sum2 = sum2 + maxNum2
    maxNum2 = maxNum2 - 1
