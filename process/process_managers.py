# 进程：Process
# 线程：Thread
# managers：实现分布式进程
import random
import queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


# 继承BaseManage
class QueueManager(BaseManager):
    pass


def get_task_func():
    return task_queue


def get_result_func():
    return result_queue


# 把两个queue注册到网络上 并使用callable关联
QueueManager.register('get_task_queue', callable=get_task_func)
QueueManager.register('get_result_queue', callable=get_result_func)
# 绑定端口 设置验证码abc
manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

if __name__ == '__main__':
    # 启动queue
    manager.start()
    # 获得通过网络访问的queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放入任务
    for i in range(10):
        n = random.randint(0, 10000)
        print('put task %s...' % n)
        task.put(n)
    # 从result中读取
    for i in range(10):
        r = result.get(timeout=10)
        print('result: %s' % r)
    # 关闭
    manager.shutdown()
    print('master exit')
