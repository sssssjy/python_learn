#!/usr/bin/env python3
# coding=utf-8

# enum: 枚举

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Auguest', 'Sept', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 可使用Month.Jan来引用常量
# value自动赋给成员的int常量 从1开始


# 精确控制枚举
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tues = 2
    Wed = 3
    Thurs = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Fri
print(day1)  # Weekday.Fri
print(day1.value)  # 5


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender: Gender):
        self.name = name
        self.gender = gender
