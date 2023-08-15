# 进程由若干线程组成
import time
import threading


# 主线程：默认进程会启动一个线程
# current_thread()函数:返回当前线程实例
# 主线程name为MainThread
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while (n < 5):
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

# 多进程vs多线程
# 多进程同一个变量 copy存在于每一个进程中 互不影响
# 多线程中 所有变量共享 因此需要Lock 保证变量不被冲突修改
balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# ThreadLocal: 不同线程数据独立
# 创建全局ThreadLocal对象
local_school = threading.local()


def process_stu():
    # 获取当前线程关联的stu
    std = local_school.student
    print('hello %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的stu
    local_school.student = name
    process_stu()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='thread a')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='thread b')
t1.start()
t2.start()
t1.join()
t2.join()
