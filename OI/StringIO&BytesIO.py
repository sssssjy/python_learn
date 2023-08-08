#!/usr/bin/env python3
#coding=utf-8 

# stringIO: 在内存中读取文件

from io import StringIO, BytesIO
f = StringIO()
f.write('hello')
f.write(' www')
print(f.getvalue())

f1 = StringIO('Hello\nIt\'s\nMe!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

f2 = BytesIO()
f2.write('中文'.encode('utf-8'))
print(f2.getvalue())