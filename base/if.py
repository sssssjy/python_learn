#!/usr/bin/env python3
# coding=utf-8

# if elif else
age = 20
print('your age is:', age)
if age > 18:
    print('adult')
elif age > 12:
    print('teenager')
else:
    print('kid')

birth = input('enter your birth')
if int(birth) > 6:
    print('your birth is late')
else:
    print('your birth is early')

height = 1.75
weight = 80.5
bmi = weight / (height**2)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
