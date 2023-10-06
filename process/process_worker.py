import time
import sys
from queue import Queue
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass


# 该manager只能从网络获取queue 所以只注册名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接服务器 连接process_managers.py
server_addr = '127.0.0.1'
print('server connect %s' % server_addr)
# 验证端口和验证码
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接
m.connect()
# 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列获取任务 并写入result中
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n**2)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')

print('worker end')
