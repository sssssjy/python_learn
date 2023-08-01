#!/usr/bin/env python3
#coding=utf-8 

import unittest

from myDict import Dict

# 测试类 继承自 unittest.TestCase
# 以test开头即为测试方法 否则测试时不执行
# assertEqual: 断言期望相等
# assertRaise: 断言期望报错

# setUp tearDown 在每一个测试方法前后被执行
class TestDict(unittest.TestCase):
    def setUp(self) -> None:
        print('setup...')

    def tearDown(self) -> None:
        print('teardown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 测试执行方式：
if __name__ == '__main__':
    unittest.main()

# 或者在命令行添加参数 -m unittest