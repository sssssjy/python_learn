# 序列化：把变量从内存中变成可存储或传输的过程

import pickle, json
d = dict(name='aaa', age='bbb')
# 将任意对象序列化为bytes
print(pickle.dumps(d))

# 将对象序列化后写入一个file-like object中
# with open('/Users/shanjiaying/Documents/pythonwrite.txt', 'wb') as f:
#     pickle.dump(d, f)

# # 反序列化
# with open('/Users/shanjiaying/Documents/pythonwrite.txt', 'rb') as f:
#     d = pickle.load(f)
#     print(d)

# json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
# allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

# 将python对象序列化为json
print(json.dumps(d))  # json str
json_str = json.dumps(d)
print(json.loads(json_str))  # json obj
