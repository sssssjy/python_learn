#!/usr/bin/env python3
#coding=utf-8 

import types
class Animal(object):
    def run(self):
        print('animal is running')

class Dog(Animal):
    def run(sef):
        print('dog is running')

class Cat(Animal):
    def run(self):
        print('cat is running')


dog = Dog()
cat = Cat()

dog.run()
cat.run()

#type 获取对象信息
print(type(123)) #<class 'int'>
print(type(None)) #<class 'NoneType'>
print(type(abs)) #<class 'builtin_function_or_method'>

# 判断对象是否为函数 types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x * x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

# 判断继承 isinstance
# 能用type判断的 基本可以用isinstance判断
# 判断是某些类型中的一种
# 优先使用isinstance
print(isinstance([1, 2, 3], (list, tuple)))

#dir() 获取一个对象的所有属性和方法 返回一个包含字符串的list
print(dir(list))
#当用len获取数组的长度时 其内部为调用__len__方法 因此以下等价
len([1, 2, 3])
[1, 2, 3].__len__()

print(len([1, 2, 3]), [1, 2, 3].__len__())

#自定义__len__方法 使class可调用len
class MyDog(object):
    def __len__(self):
        return 13
    
dog = MyDog()
print(len(dog))


# getattr setattr hasattr
class MyObject(object):
    def __init__(self) -> None:
        self.x = 9

    def power(self):
        return self.x * self.x
    
obj = MyObject()

print(hasattr(obj, 'x')) #obj 有x属性吗
print(hasattr(obj, 'y'))

setattr(obj, 'y', 33) #给obj添加y属性 值为33
print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))

print(getattr(obj, 'dd', 404)) #返回属性 否则返回默认值404

def readImage(fp):
    if hasattr(fp, 'read'):
        return fp.read()
    return None

# 实例属性和类属性

# 类属性
# 归Student类所有 类的所有实例都能访问到
# class Student(object):
#     name = 'Student'

# stu = Student()
# print(stu.name) #Student
# stu.name = 'stu'
# print(stu.name) #stu
# del stu.name
# print(stu.name) #Student

class Student(object):
    count = 0

    def __init__(self, name) -> None:
        self.name = name
        Student.count += 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')