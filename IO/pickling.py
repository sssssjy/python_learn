# 序列化：把变量从内存中变成可存储或传输的过程
# dumps & loads
import pickle
import json
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


# 序列化class
class Student(object):
    def __init__(self, name, age, score) -> None:
        self.name = name
        self.age = age
        self.score = score


s = Student('name', 12, 4)


# 需要传入一个转换函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(dict):
    return Student(dict['name'], dict['age'], dict['score'])


print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
