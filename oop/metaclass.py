#!/usr/bin/env python3
# coding=utf-8

# python 动态语言
# 函数和类的定义 不是编译时定义的 而是运行时动态创建的

from typing import Any
from hello import Hello

h = Hello()
h.hello()
print(type(Hello))  # <class 'type'>
print(type(h))  # <class 'hello.Hello'>


# type函数可以返回对象的类型 也可以创建出新的类型
# type(class的名称, 继承的父类集合, class的方法名称和函数绑定)
def fn(self, name='world'):
    print('Hello %s' % name)


Hello1 = type('Hello1', (object,), dict(hello1=fn))  # 创建Hello class

h1 = Hello1()
h1.hello1()
print(type(Hello1))  # <class 'type'>
print(type(h1))  # <class '__main__.Hello1'>


# metaclass 元类 控制类的创建行为

# 定义一个类 -> 创建类的实例
# 定义一个metaclass -> 创建出类 -> 创建出类的实例

# metaclass 是类的模板 需要从type派生
class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        # __new__(当前准备创建类的对象, 类的名字, 类继承的父类集合, 类的方法集合)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaClass):
    pass


L = MyList()
L.add(1)
print(L)


# 不常用 可能用于ORM
# ORM全称“Object Relational Mapping”，即对象-关系映射
class Field(object):
    def __init__(self, name, column_type) -> None:
        self.name = name
        self.column_type = column_type

    def __str__(self) -> str:
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name) -> None:
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name) -> None:
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        print('Found model : %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("r'Model' object does not have attribute %s" % key)
        
    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s(%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
