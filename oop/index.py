#!/usr/bin/env python3
# coding=utf-8

class Student(object):
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 90)

bart.print_score()
lisa.print_score()

# 类Class 和 实例Instance

print(bart)  # bart指向student的一个实例
print(Student)  # Student本身是一个类

# __init__(self)
# self 指向实例本身
# 在类中定义的方法 第一个参数永远是self


# 私有变量 __开头
class PrivateName(object):
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def print_age(self):
        print('%s is now %s years old' % (self.__name, self.__age))

    def get_age(self):
        return self.__age

    def mod_age(self, age):
        self.__age = age


pn1 = PrivateName('selina', 77)
# print(pn1.__age) 报错

print(pn1.get_age())
pn1.mod_age(23)
print(pn1.get_age())


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if (gender == 'male' or gender == 'female'):
            self.__gender = gender
        else:
            raise ValueError('bad gender')


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
