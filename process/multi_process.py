import os
from multiprocessing import Process, Pool, Queue
import random
import time
import subprocess

# linux/unix 提供了fork函数：调用一次 返回两次
# 操作系统把当前进程（父）复制了一份（子） 分别在父进程和子进程返回
# 子进程永远返回0 父进程返回子进程的id

# 对于父进程：
#     os.getpid()获取自身id
#     os.fork() 返回子进程id

# 对于子进程：
#     os.getpid() 获取自身id
#     os.getppid() 获取父进程id

# print('Processing (%s) Start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('child process %s and parent process is %s' % (os.getpid(), os.getppid()))
# else:
#     print('%s create child process %s' % (os.getpid(), pid))


# Process 跨平台启动子进程方式
# def run_proc(name):
#     print('run chlid process %s (%s)' % (name, os.getpid()))


# if (__name__ == '__main__'):
#     print('parent process %s' % os.getpid())
#     p = Process(target=run_proc, args=('test',))  # 执行函数 与 参数
#     print('child process will start...')
#     p.start()
#     p.join()  # 等待子进程结束
#     print('child process end')


# 批量创建子进程 Pool
# def long_time_task(name):
#     print('run task %s (%s)' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('task %s runs %.2f seconds' % (name, end - start))


# if __name__ == '__main__':
#     print('parent process %s running...' % os.getpid())
#     p = Pool(4)  # 最多同时进行4个进程 默认是电脑的cpu数量
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('waiting for all task finish...')
#     p.close()
#     p.join()
#     print('all task finished')

# 控制子进程的输入输出 subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('code', r)

# # 输入 communicate
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('code', p.returncode)


# 进程间通信 Process Queue Pipes
# put get
def write(q):
    print('process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)


if __name__ == '__main__':
    q = Queue()
    # 读写两进程进行通信
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # 强制结束
    pr.terminate()
